"""
main.py

Orquestrador do pipeline de monitoramento diário com injeção dinâmica em memória
de configurações protegidas via Google Drive/Rclone e carimbo temporal de Brasília.
"""

import os
import sys
import time
from zoneinfo import ZoneInfo

# Configuração prioritária do fuso horário de Brasília (UTC-3)
os.environ["TZ"] = "America/Sao_Paulo"
if hasattr(time, "tzset"):
    time.tzset()

FUSO_BRASILIA = ZoneInfo("America/Sao_Paulo")

import argparse
import concurrent.futures
from datetime import datetime
import importlib.util
import json
import random
import re
import subprocess
import types

from notifier import enviar_telegram
import processor


def carregar_modulo_config(caminho_ou_shard: str):
    """
    Carrega a configuração dinamicamente na memória RAM.
    Lê do disco se for caminho local ou faz streaming do Google Drive via Rclone.
    Suporta fallback de encoding (UTF-8, UTF-8-BOM, UTF-16, Latin-1) sem gravar arquivos.
    """
    if os.path.exists(caminho_ou_shard):
        spec = importlib.util.spec_from_file_location("config_modulo", caminho_ou_shard)
        modulo = importlib.util.module_from_spec(spec)
        sys.modules["config_modulo"] = modulo
        spec.loader.exec_module(modulo)
        return modulo

    nome_arquivo = (
        f"config_{caminho_ou_shard}.py"
        if not caminho_ou_shard.endswith(".py")
        else caminho_ou_shard
    )
    comando = ["rclone", "cat", f"gdrive_config:{nome_arquivo}"]

    proc = subprocess.run(comando, capture_output=True)
    if proc.returncode != 0:
        erro_msg = proc.stderr.decode("utf-8", errors="replace")
        raise RuntimeError(
            f"Falha ao ler {nome_arquivo} do Google Drive via Rclone.\nDetalhes: {erro_msg}"
        )

    conteudo_codigo = None
    for enc in ["utf-8-sig", "utf-8", "utf-16", "latin-1"]:
        try:
            conteudo_codigo = proc.stdout.decode(enc)
            break
        except UnicodeDecodeError:
            continue

    if conteudo_codigo is None:
        raise ValueError(f"Não foi possível decodificar o arquivo {nome_arquivo}.")

    modulo = types.ModuleType("config_modulo")
    modulo.__file__ = f"<gdrive_config:{nome_arquivo}>"
    sys.modules["config_modulo"] = modulo
    exec(conteudo_codigo, modulo.__dict__)

    return modulo
    

def registrar_step_summary(regiao: str, total_brutas: int, total_clusters: int, sucessos: int, bloqueados: int) -> None:
    """
    Registra tabela de métricas operacionais no GitHub Step Summary.
    A gravação ocorre apenas se a variável GITHUB_STEP_SUMMARY estiver definida no ambiente.
    """
    caminho_summary = os.getenv("GITHUB_STEP_SUMMARY")
    if not caminho_summary:
        return

    taxa = (sucessos / (sucessos + bloqueados) * 100) if (sucessos + bloqueados) > 0 else 0.0
    agora = datetime.now(FUSO_BRASILIA).strftime("%d/%m/%Y %H:%M:%S")

    markdown = (
        f"### 📊 Monitoramento Regional: {regiao.upper()}\n\n"
        f"**Data/Hora Execução:** {agora} (Horário de Brasília)\n\n"
        f"| Métrica | Valor |\n"
        f"| :--- | :--- |\n"
        f"| Matérias Brutas Coletadas | {total_brutas} |\n"
        f"| Clusters Consolidados | {total_clusters} |\n"
        f"| Textos Extraídos com Sucesso | {sucessos} |\n"
        f"| Bloqueadas / Falhas | {bloqueados} |\n"
        f"| Taxa de Eficácia | {taxa:.1f}% |\n\n"
        f"---\n"
    )

    with open(caminho_summary, "a", encoding="utf-8") as f:
        f.write(markdown)


def executar_pipeline(caminho_ou_shard: str) -> None:
    cfg = carregar_modulo_config(caminho_ou_shard)
    regiao = getattr(cfg, "REGIAO_NOME", "GLOBAL").lower()
    agora_bsb = datetime.now(FUSO_BRASILIA)
    ts = agora_bsb.strftime("%Y%m%d_%H%M%S")

    nome_json = f"noticias_{regiao}_{ts}.json"

    raw_articles = []
    print(
        f"Iniciando varredura regional [{regiao.upper()}] em"
        f" {agora_bsb.strftime('%Y-%m-%d %H:%M:%S')} (Horário de Brasília)...",
        flush=True,
    )

    # 1. Varredura RSS direcionada por mercado e idioma
    for tema, dict_idiomas in cfg.MONITORAMENTOS.items():
        print(f">> Tema: {tema}", flush=True)
        for mercado in cfg.MERCADOS_ALVO:
            gl = mercado["gl"]
            hl = mercado["hl"]
            lang = mercado["lang"]

            termos = dict_idiomas.get(lang, [])
            termos_excluidos = cfg.TERMOS_EXCLUIDOS.get(lang, [])

            for termo in termos:
                query = processor.build_rss_query(
                    base_term=termo,
                    excluded_terms=termos_excluidos,
                    period=cfg.PERIODO_BUSCA,
                    preferred_domains=cfg.DOMINIOS_PREFERENCIAIS,
                )
                itens = processor.fetch_rss_feed(
                    query, hl=hl, gl=gl, timeout=cfg.TIMEOUT_REQUISICAO
                )
                for item in itens:
                    item["tema"] = tema
                    item["termo_origem"] = termo
                    item["pais_emissao"] = gl
                    item["idioma"] = hl
                    raw_articles.append(item)

    print(f"Total bruto coletado: {len(raw_articles)} matérias.", flush=True)

    # 2. Agrupamento Semântico no dia com prefixo regional para integridade relacional
    clusters = processor.cluster_articles(
        raw_articles,
        model_name=cfg.MODELO_EMBEDDING_1024,
        similarity_threshold=cfg.SIMILARIDADE_REDUNDANCIA,
        regiao_prefix=regiao,
    )
    print(f"Clusters consolidados: {len(clusters)}", flush=True)

    # 3. Extração Concorrente de Rede com Autocura (Fallback em Espelhos)
    def worker(cluster_item):
        time.sleep(random.uniform(0.1, 0.3))
        return processor.process_cluster_with_fallback(
            cluster_item, timeout=cfg.TIMEOUT_REQUISICAO
        )

    # 3.1 Estágio 1: Fast HTTP (tentativa rápida por conexão direta)
    processed_results = []
    max_workers = getattr(cfg, "MAX_WORKERS_PARALELO", 8)
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        futuros = {executor.submit(worker, c): c for c in clusters}
        for futuro in concurrent.futures.as_completed(futuros):
            res = futuro.result()
            processed_results.append(res)

    sucessos_estagio1 = sum(1 for r in processed_results if r["status_extracao"] == "SUCESSO")
    print(f">> Estágio 1 (HTTP) concluído: {sucessos_estagio1}/{len(clusters)} extraídos com sucesso.", flush=True)

    # 3.2 Estágio 2: Headless Browser Playwright Stealth (resgate de matérias bloqueadas)
    bloqueados_indices = [i for i, r in enumerate(processed_results) if r["status_extracao"] != "SUCESSO"]
    if bloqueados_indices:
        print(f">> Estágio 2: Ativando Playwright Stealth para {len(bloqueados_indices)} matérias...", flush=True)
        itens_para_pw = [processed_results[i] for i in bloqueados_indices]
        itens_recuperados = processor.executar_fallback_playwright(itens_para_pw)

        for pos, idx_original in enumerate(bloqueados_indices):
            processed_results[idx_original] = itens_recuperados[pos]

    for i, res in enumerate(processed_results, 1):
        status_ico = "✅" if res["status_extracao"] == "SUCESSO" else "🔒"
        print(f"[{i}/{len(clusters)}] {status_ico} {res['titulo'][:60]}...", flush=True)

    # 4. Exportação Atômica do JSON estruturado
    json_formatado = json.dumps(processed_results, ensure_ascii=False, indent=2)
    with open(nome_json, "w", encoding="utf-8") as f:
        f.write(json_formatado)

    sucessos = sum(1 for r in processed_results if r["status_extracao"] == "SUCESSO")
    bloqueados = len(processed_results) - sucessos

    # 5. Telemetria em Console e GitHub Step Summary
    taxa_sucesso = (sucessos / len(processed_results) * 100) if processed_results else 0.0
    print("\n" + "=" * 60, flush=True)
    print(f"RELATÓRIO CONSOLIDADO: [{regiao.upper()}]", flush=True)
    print(f"Matérias Brutas : {len(raw_articles)}", flush=True)
    print(f"Clusters        : {len(clusters)}", flush=True)
    print(f"Sucessos        : {sucessos} ({taxa_sucesso:.1f}%)", flush=True)
    print(f"Bloqueios       : {bloqueados}", flush=True)
    print("=" * 60 + "\n", flush=True)

    registrar_step_summary(
        regiao=regiao,
        total_brutas=len(raw_articles),
        total_clusters=len(clusters),
        sucessos=sucessos,
        bloqueados=bloqueados,
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Orquestrador de Monitoramento Regional")
    parser.add_argument(
        "--config",
        type=str,
        default=None,
        help="Caminho do arquivo de configuração local",
    )
    parser.add_argument(
        "--shard",
        type=str,
        default=None,
        help="Nome do shard para carregar diretamente do Google Drive em memória",
    )
    args = parser.parse_args()

    alvo = args.shard if args.shard else args.config
    if not alvo:
        raise ValueError("É necessário informar --shard ou --config.")

    executar_pipeline(alvo)
