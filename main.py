"""
main.py

Orquestrador do pipeline regional com injeção dinâmica em memória via Rclone,
busca delimitada por intervalo MMAAAA (sem depender dos configs) e gravação
direta no Google Drive corporativo.
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
import calendar
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


def parse_mmaaaa(tag: str, is_end: bool = False) -> str:
    """
    Converte string no formato MMAAAA (ex: '102021') em data YYYY-MM-DD.
    Se for fim de período, calcula o primeiro dia do mês subsequente para corte estrito no Google.
    """
    tag = tag.strip().replace("/", "").replace("-", "")
    if len(tag) != 6 or not tag.isdigit():
        raise ValueError(f"Formato inválido para MMAAAA: '{tag}'. Esperado 6 dígitos (ex: 102021).")

    mes = int(tag[:2])
    ano = int(tag[2:])

    if not (1 <= mes <= 12):
        raise ValueError(f"Mês inválido: {mes}. Deve estar entre 01 e 12.")

    if not is_end:
        return f"{ano:04d}-{mes:02d}-01"
    else:
        if mes == 12:
            return f"{ano + 1:04d}-01-01"
        else:
            return f"{ano:04d}-{mes + 1:02d}-01"


def carregar_modulo_config(caminho_ou_shard: str):
    """
    Carrega a configuração dinamicamente na memória RAM via Rclone streaming
    ou arquivo local, tolerando múltiplos encodings.
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


def executar_pipeline(caminho_ou_shard: str, inicio_mmaaaa: str = None, fim_mmaaaa: str = None) -> None:
    cfg = carregar_modulo_config(caminho_ou_shard)
    regiao = getattr(cfg, "REGIAO_NOME", "GLOBAL").lower()
    agora_bsb = datetime.now(FUSO_BRASILIA)
    ts = agora_bsb.strftime("%Y%m%d_%H%M%S")

    # Determinação do filtro temporal absoluto
    if inicio_mmaaaa and fim_mmaaaa:
        d_after = parse_mmaaaa(inicio_mmaaaa, is_end=False)
        d_before = parse_mmaaaa(fim_mmaaaa, is_end=True)
        filtro_data = f"after:{d_after} before:{d_before}"
        rotulo_periodo = f"{inicio_mmaaaa}_{fim_mmaaaa}"
    else:
        filtro_data = "when:1d"
        rotulo_periodo = ts

    nome_json = f"noticias_{regiao}_{rotulo_periodo}.json"

    raw_articles = []
    print(
        f"Iniciando varredura [{regiao.upper()}] | Janela: {filtro_data} | Fuso: Brasília...",
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
            termos_excluidos = getattr(cfg, "TERMOS_EXCLUIDOS", {}).get(lang, [])
            dominios = getattr(cfg, "DOMINIOS_PREFERENCIAIS", [])
            timeout_req = getattr(cfg, "TIMEOUT_REQUISICAO", 6)

            for termo in termos:
                # Constrói query explicitamente com o filtro after/before ou when:1d
                query = processor.build_rss_query(
                    base_term=termo,
                    excluded_terms=termos_excluidos,
                    period=None,  # Desativa o parâmetro antigo
                    preferred_domains=dominios,
                )
                query_final = f"{query} {filtro_data}".strip()

                itens = processor.fetch_rss_feed(
                    query_final, hl=hl, gl=gl, timeout=timeout_req
                )
                for item in itens:
                    item["tema"] = tema
                    item["termo_origem"] = termo
                    item["pais_emissao"] = gl
                    item["idioma"] = hl
                    raw_articles.append(item)

    print(f"Total bruto coletado: {len(raw_articles)} matérias.", flush=True)

    # 2. Agrupamento Semântico
    clusters = processor.cluster_articles(
        raw_articles,
        model_name=getattr(cfg, "MODELO_EMBEDDING_1024", "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"),
        similarity_threshold=getattr(cfg, "SIMILARIDADE_REDUNDANCIA", 0.73),
        regiao_prefix=regiao,
    )
    print(f"Clusters consolidados: {len(clusters)}", flush=True)

    # 3. Extração Concorrente de Rede com Autocura (Cascata Primária + Espelhos)
    timeout_req = getattr(cfg, "TIMEOUT_REQUISICAO", 6)

    def worker(cluster_item):
        time.sleep(random.uniform(0.1, 0.3))
        return processor.process_cluster_with_fallback(cluster_item, timeout=timeout_req)

    processed_results = []
    max_workers = getattr(cfg, "MAX_WORKERS_PARALELO", 8)
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        futuros = {executor.submit(worker, c): c for c in clusters}
        for futuro in concurrent.futures.as_completed(futuros):
            res = futuro.result()
            processed_results.append(res)

    sucessos_estagio1 = sum(1 for r in processed_results if r["status_extracao"] == "SUCESSO")
    print(f">> Estágio 1 (HTTP) concluído: {sucessos_estagio1}/{len(clusters)} extraídos com sucesso.", flush=True)

    # 3.2 Estágio 2: Headless Browser Playwright Stealth
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

    # 4. Gravação local provisória
    json_formatado = json.dumps(processed_results, ensure_ascii=False, indent=2)
    with open(nome_json, "w", encoding="utf-8") as f:
        f.write(json_formatado)

    # 5. Cópia imediata para o Google Drive corporativo (dados brutos)
    print(f">> Transmitindo {nome_json} para Google Drive (dados brutos)...", flush=True)
    res_drive = subprocess.run(["rclone", "copyto", nome_json, f"gdrive_dados:{nome_json}"], capture_output=True)
    if res_drive.returncode == 0:
        print(f"✓ Arquivo {nome_json} gravado com sucesso no Google Drive.", flush=True)
    else:
        print(f"⚠️ Alerta: Falha ao gravar no Drive via Python: {res_drive.stderr.decode('utf-8', errors='replace')}", flush=True)

    sucessos = sum(1 for r in processed_results if r["status_extracao"] == "SUCESSO")
    bloqueados = len(processed_results) - sucessos

    # 6. Telemetria
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

    enviar_telegram(
        regiao_nome=regiao,
        arquivos=[nome_json],
        total_brutas=len(raw_articles),
        total_clusters=len(clusters),
        total_processadas=len(processed_results),
        sucessos=sucessos,
        bloqueados=bloqueados,
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Orquestrador de Monitoramento Regional")
    parser.add_argument("--config", type=str, default=None, help="Caminho do arquivo local")
    parser.add_argument("--shard", type=str, default=None, help="Nome do shard no Google Drive")
    parser.add_argument("--inicio_mmaaaa", type=str, default=None, help="Mês/Ano inicial (ex: 102021)")
    parser.add_argument("--fim_mmaaaa", type=str, default=None, help="Mês/Ano final (ex: 092026)")
    args = parser.parse_args()

    alvo = args.shard if args.shard else args.config
    if not alvo:
        raise ValueError("É necessário informar --shard ou --config.")

    executar_pipeline(
        caminho_ou_shard=alvo,
        inicio_mmaaaa=args.inicio_mmaaaa,
        fim_mmaaaa=args.fim_mmaaaa,
    )
