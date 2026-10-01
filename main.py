"""
main.py

Orquestrador iterativo: processa tema por tema, mês por mês.
Divide o mês em subjanelas semanais para mitigar o teto do Google News RSS,
grava e envia cada arquivo diretamente para o Google Drive corporativo:
noticias_raw_<AAAA>_<MM>_<tema>.json
"""

import os
import sys
import time
from zoneinfo import ZoneInfo

os.environ["TZ"] = "America/Sao_Paulo"
if hasattr(time, "tzset"):
    time.tzset()

FUSO_BRASILIA = ZoneInfo("America/Sao_Paulo")

import argparse
import calendar
import concurrent.futures
from datetime import datetime, timedelta
import importlib.util
import json
import random
import re
import subprocess
import types

from notifier import enviar_telegram
import processor


def gerar_meses_entre(inicio_mmaaaa: str, fim_mmaaaa: str) -> list:
    """Gera lista de tuplas (ano, mes) entre duas marcas MMAAAA inclusivas."""
    ini = inicio_mmaaaa.strip().replace("/", "")
    fim = fim_mmaaaa.strip().replace("/", "")
    m_ini, a_ini = int(ini[:2]), int(ini[2:])
    m_fim, a_fim = int(fim[:2]), int(fim[2:])

    meses = []
    dt_atual = datetime(a_ini, m_ini, 1)
    dt_fim = datetime(a_fim, m_fim, 1)

    while dt_atual <= dt_fim:
        meses.append((dt_atual.year, dt_atual.month))
        # Avança 1 mês
        ultimo_dia = calendar.monthrange(dt_atual.year, dt_atual.month)[1]
        dt_atual = dt_atual + timedelta(days=ultimo_dia)
        dt_atual = dt_atual.replace(day=1)

    return meses


def gerar_subjanelas_mes(ano: int, mes: int) -> list:
    """Divide um mês em 4 janelas para contornar o teto de 100 itens do RSS."""
    ultimo_dia = calendar.monthrange(ano, mes)[1]
    cortes = [
        (1, 7),
        (8, 14),
        (15, 21),
        (22, ultimo_dia)
    ]
    janelas = []
    for d_ini, d_fim in cortes:
        dt_ini = f"{ano:04d}-{mes:02d}-{d_ini:02d}"
        if d_fim == ultimo_dia:
            # Próximo dia para before exclusivo
            if mes == 12:
                dt_fim = f"{ano+1:04d}-01-01"
            else:
                dt_fim = f"{ano:04d}-{mes+1:02d}-01"
        else:
            dt_fim = f"{ano:04d}-{mes:02d}-{d_fim+1:02d}"
        janelas.append(f"after:{dt_ini} before:{dt_fim}")
    return janelas


def carregar_modulo_config(caminho_ou_shard: str):
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
        raise RuntimeError(f"Falha ao ler {nome_arquivo} do Google Drive: {erro_msg}")

    conteudo = None
    for enc in ["utf-8-sig", "utf-8", "utf-16", "latin-1"]:
        try:
            conteudo = proc.stdout.decode(enc)
            break
        except UnicodeDecodeError:
            continue

    if conteudo is None:
        raise ValueError(f"Não foi possível decodificar {nome_arquivo}.")

    modulo = types.ModuleType("config_modulo")
    modulo.__file__ = f"<gdrive_config:{nome_arquivo}>"
    sys.modules["config_modulo"] = modulo
    exec(conteudo, modulo.__dict__)
    return modulo


def listar_ficheiros_existentes_drive() -> set:
    """
    Obtém a lista com os nomes exatos de todos os ficheiros existentes
    na pasta de dados brutos do Google Drive.
    """
    comando = ["rclone", "lsf", "gdrive_dados:", "--files-only"]
    proc = subprocess.run(comando, capture_output=True, text=True)
    if proc.returncode != 0:
        raise RuntimeError(
            f"Falha ao aceder ao inventário do Google Drive via Rclone: {proc.stderr}"
        )
    
    # Retorna o conjunto de nomes de ficheiros (ex: {'noticias_raw_2021_10_ifood.json', ...})
    return set(f.strip() for f in proc.stdout.splitlines() if f.strip())


def executar_pipeline(caminho_ou_shard: str, inicio_mmaaaa: str = None, fim_mmaaaa: str = None) -> None:
    cfg = carregar_modulo_config(caminho_ou_shard)
    regiao = getattr(cfg, "REGIAO_NOME", "GLOBAL").lower()

    # 1. Carrega o catálogo real do Google Drive no arranque do shard
    print(">> Mapeando inventário de arquivos pré-existentes no Google Drive...", flush=True)
    ficheiros_validos_drive = listar_ficheiros_existentes_drive()
    print(f"   Total de arquivos mapeados em 'dados_brutos': {len(ficheiros_validos_drive)}", flush=True)

    # Definição do escopo temporal
    if inicio_mmaaaa and fim_mmaaaa:
        meses_alvo = gerar_meses_entre(inicio_mmaaaa, fim_mmaaaa)
    else:
        agora = datetime.now(FUSO_BRASILIA)
        meses_alvo = [(agora.year, agora.month)]

    print(f"\n=======================================================", flush=True)
    print(f"SHARD: [{regiao.upper()}] | MESES: {len(meses_alvo)} no escopo", flush=True)
    print(f"=======================================================\n", flush=True)

    mercados = cfg.MERCADOS_ALVO
    timeout_req = getattr(cfg, "TIMEOUT_REQUISICAO", 6)
    max_workers = getattr(cfg, "MAX_WORKERS_PARALELO", 8)
    dominios = getattr(cfg, "DOMINIOS_PREFERENCIAIS", [])

    total_geral_extraidas = 0

    # 2. Laço Mês a Mês
    for ano, mes in meses_alvo:
        subjanelas = gerar_subjanelas_mes(ano, mes)
        tag_mes = f"{ano:04d}_{mes:02d}"

        # 3. Laço Tema a Tema
        for tema, dict_idiomas in cfg.MONITORAMENTOS.items():
            tema_slug = processor.normalizar_nome_tema(tema)
            nome_arquivo_drive = f"noticias_raw_{tag_mes}_{tema_slug}.json"

            # -------------------------------------------------------------
            # TRAVA DE SEGURANÇA: Só busca se o arquivo já existir no Drive
            # -------------------------------------------------------------
            if nome_arquivo_drive not in ficheiros_validos_drive:
                print(f"⚠️ [IGNORADO] {nome_arquivo_drive} não existe no Drive. Criação bloqueada.", flush=True)
                continue

            print(f"\n>> Processando: {nome_arquivo_drive}...", flush=True)
            raw_artigos_tema = []

            # 4. Fatiamento em 4 subjanelas semanais
            for filtro_janela in subjanelas:
                for mercado in mercados:
                    gl = mercado["gl"]
                    hl = mercado["hl"]
                    lang = mercado["lang"]

                    termos = dict_idiomas.get(lang, [])
                    excluidos = getattr(cfg, "TERMOS_EXCLUIDOS", {}).get(lang, [])

                    for termo in termos:
                        query_base = processor.build_rss_query(termo, excluidos, dominios)
                        query_final = f"{query_base} {filtro_janela}".strip()

                        itens = processor.fetch_rss_feed(query_final, hl=hl, gl=gl, timeout=timeout_req)
                        for item in itens:
                            item["tema"] = tema
                            item["termo_origem"] = termo
                            item["pais_emissao"] = gl
                            item["idioma"] = hl
                            raw_artigos_tema.append(item)

            if not raw_artigos_tema:
                print(f"   Nenhuma matéria encontrada para {tema} em {tag_mes}.", flush=True)
                continue

            # 5. Agrupamento Semântico Leve
            prefixo = f"CLUS_{tag_mes}_{tema_slug[:4].upper()}"
            clusters = processor.cluster_articles_rapido(raw_artigos_tema, similarity_threshold=80.0, prefixo_id=prefixo)

            # 6. Raspagem Concorrente em Cascata
            def worker(c):
                time.sleep(random.uniform(0.05, 0.2))
                return processor.process_cluster_with_fallback(c, timeout=timeout_req)

            processed_results = []
            with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
                futuros = {executor.submit(worker, c): c for c in clusters}
                for f in concurrent.futures.as_completed(futuros):
                    processed_results.append(f.result())

            bloqueados = [i for i, r in enumerate(processed_results) if r["status_extracao"] != "SUCESSO"]
            if bloqueados:
                itens_pw = [processed_results[i] for i in bloqueados]
                recuperados = processor.executar_fallback_playwright(itens_pw)
                for pos, idx_orig in enumerate(bloqueados):
                    processed_results[idx_orig] = recuperados[pos]

            sucessos = sum(1 for r in processed_results if r["status_extracao"] == "SUCESSO")
            total_geral_extraidas += sucessos
            print(f"   Resultado: {sucessos}/{len(clusters)} textos extraídos com sucesso.", flush=True)

            # -------------------------------------------------------------
            # 7. Gravação Local e Sobrescrita Direta no Google Drive
            # -------------------------------------------------------------
            with open(nome_arquivo_drive, "w", encoding="utf-8") as f:
                json.dump(processed_results, f, ensure_ascii=False, indent=2)

            res = subprocess.run(
                ["rclone", "copyto", nome_arquivo_drive, f"gdrive_dados:{nome_arquivo_drive}"],
                capture_output=True
            )
            if res.returncode == 0:
                print(f"   ✓ Arquivo existente atualizado no Drive: {nome_arquivo_drive}", flush=True)
            else:
                print(f"   ⚠️ Falha ao atualizar {nome_arquivo_drive}: {res.stderr.decode('utf-8', errors='replace')}", flush=True)

    print(f"\nFinalizada a execução do Shard [{regiao.upper()}]. Total de matérias atualizadas: {total_geral_extraidas}\n", flush=True)
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Orquestrador Histórico por Shard")
    parser.add_argument("--config", type=str, default=None)
    parser.add_argument("--shard", type=str, default=None)
    parser.add_argument("--inicio_mmaaaa", type=str, default=None, help="Ex: 102021")
    parser.add_argument("--fim_mmaaaa", type=str, default=None, help="Ex: 092026")
    args = parser.parse_args()

    alvo = args.shard if args.shard else args.config
    if not alvo:
        raise ValueError("Informe --shard ou --config.")

    executar_pipeline(
        caminho_ou_shard=alvo,
        inicio_mmaaaa=args.inicio_mmaaaa,
        fim_mmaaaa=args.fim_mmaaaa,
    )
