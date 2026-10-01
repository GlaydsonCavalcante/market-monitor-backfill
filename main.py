"""
main.py

Orquestrador desacoplado em duas fases com idempotência:
- Fase A: Descoberta RSS semanal, formação de clusters e persistência de status PENDENTE.
- Fase B: Raspagem factual resiliente em cascata (Fast HTTP + Playwright Stealth).
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
    ini = inicio_mmaaaa.strip().replace("/", "").replace("-", "")
    fim = fim_mmaaaa.strip().replace("/", "").replace("-", "")
    m_ini, a_ini = int(ini[:2]), int(ini[2:])
    m_fim, a_fim = int(fim[:2]), int(fim[2:])

    meses = []
    dt_atual = datetime(a_ini, m_ini, 1)
    dt_fim = datetime(a_fim, m_fim, 1)

    while dt_atual <= dt_fim:
        meses.append((dt_atual.year, dt_atual.month))
        ultimo_dia = calendar.monthrange(dt_atual.year, dt_atual.month)[1]
        dt_atual = dt_atual + timedelta(days=ultimo_dia)
        dt_atual = dt_atual.replace(day=1)

    return meses


def gerar_subjanelas_mes(ano: int, mes: int) -> list:
    """Divide o mês em 4 subjanelas para contornar o teto de 100 itens do RSS."""
    ultimo_dia = calendar.monthrange(ano, mes)[1]
    cortes = [(1, 7), (8, 14), (15, 21), (22, ultimo_dia)]
    janelas = []
    for d_ini, d_fim in cortes:
        dt_ini = f"{ano:04d}-{mes:02d}-{d_ini:02d}"
        if d_fim == ultimo_dia:
            dt_fim = f"{ano+1:04d}-01-01" if mes == 12 else f"{ano:04d}-{mes+1:02d}-01"
        else:
            dt_fim = f"{ano:04d}-{mes:02d}-{d_fim+1:02d}"
        janelas.append(f"after:{dt_ini} before:{dt_fim}")
    return janelas


def carregar_modulo_config(caminho_ou_shard: str):
    """Carrega dinamicamente a configuração do Google Drive via Rclone streaming."""
    if os.path.exists(caminho_ou_shard):
        spec = importlib.util.spec_from_file_location("config_modulo", caminho_ou_shard)
        modulo = importlib.util.module_from_spec(spec)
        sys.modules["config_modulo"] = modulo
        spec.loader.exec_module(modulo)
        return modulo

    nome_arquivo = f"config_{caminho_ou_shard}.py" if not caminho_ou_shard.endswith(".py") else caminho_ou_shard
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


def carregar_mapa_inventario_drive() -> dict:
    """
    Obtém em uma única chamada de rede os nomes e tamanhos de todos os arquivos
    na pasta 'dados_brutos' do Google Drive via Rclone.
    """
    comando = ["rclone", "lsjson", "gdrive_dados:", "--files-only"]
    proc = subprocess.run(comando, capture_output=True, text=True)
    if proc.returncode != 0:
        raise RuntimeError(f"Falha ao inventariar 'dados_brutos' via Rclone: {proc.stderr}")
    try:
        itens = json.loads(proc.stdout)
        return {item["Name"]: item["Size"] for item in itens}
    except Exception as exc:
        raise RuntimeError(f"Erro ao analisar JSON de retorno do Rclone: {exc}")


def executar_fase_a_descoberta(cfg, regiao: str, meses_alvo: list, mapa_drive: dict) -> int:
    """Executa a Fase A: busca RSS semanal e grava o esqueleto JSON com status PENDENTE."""
    print(f"\n{'='*65}\nINICIANDO FASE A (DESCOBERTA RSS): [{regiao.upper()}]\n{'='*65}", flush=True)
    mercados = cfg.MERCADOS_ALVO
    timeout_req = getattr(cfg, "TIMEOUT_REQUISICAO", 6)
    dominios = getattr(cfg, "DOMINIOS_PREFERENCIAIS", [])
    total_descobertos = 0

    for ano, mes in meses_alvo:
        tag_mes = f"{ano:04d}_{mes:02d}"
        subjanelas = gerar_subjanelas_mes(ano, mes)

        for tema, dict_idiomas in cfg.MONITORAMENTOS.items():
            tema_slug = processor.normalizar_nome_tema(tema)
            nome_arquivo = f"noticias_raw_{tag_mes}_{tema_slug}.json"

            # 1. Trava: Verifica existência prévia do arquivo
            if nome_arquivo not in mapa_drive:
                print(f"⚠️ [IGNORADO] {nome_arquivo} não existe na pasta 'dados_brutos'.", flush=True)
                continue

            # 2. Trava de Idempotência: Se o arquivo já contém dados (> 4 bytes), pula
            tamanho = mapa_drive[nome_arquivo]
            if tamanho > 4:
                print(f"⏭️ [PULANDO FASE A] {nome_arquivo} já possui conteúdo gravado ({tamanho} bytes).", flush=True)
                continue

            print(f">> [FASE A] Descobrindo matérias para: {nome_arquivo}...", flush=True)
            raw_artigos = []

            for filtro_janela in subjanelas:
                for mercado in mercados:
                    gl, hl, lang = mercado["gl"], mercado["hl"], mercado["lang"]
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
                            raw_artigos.append(item)

            if not raw_artigos:
                print(f"   ℹ️ Nenhuma matéria encontrada em {tag_mes} para '{tema}'.", flush=True)
                conteudo_fase_a = [{
                    "status_extracao": "SEM_NOTICIAS_NO_PERIODO",
                    "tema": tema,
                    "ano_mes": tag_mes,
                    "timestamp": datetime.now(FUSO_BRASILIA).strftime("%Y-%m-%d %H:%M:%S")
                }]
            else:
                prefixo = f"CLUS_{tag_mes}_{tema_slug[:4].upper()}"
                clusters = processor.cluster_articles_rapido(raw_artigos, similarity_threshold=80.0, prefixo_id=prefixo)
                conteudo_fase_a = []
                for c in clusters:
                    conteudo_fase_a.append({
                        "id_cluster": c["id_cluster"],
                        "tema": c["tema"],
                        "termo_origem": c["termo_origem"],
                        "titulo": c["titulo"],
                        "data_noticia": c["data_noticia"],
                        "idioma": c["idioma"],
                        "fonte_utilizada": c["fonte_principal"],
                        "url_primaria": c["url_primaria"],
                        "urls_espelho": c["urls_espelho"],
                        "status_extracao": "PENDENTE",
                        "texto_completo": "",
                        "motivo_bloqueio": None,
                        "necessita_extracao_manual": False,
                        "historico_tentativas": []
                    })

            with open(nome_arquivo, "w", encoding="utf-8") as f:
                json.dump(conteudo_fase_a, f, ensure_ascii=False, indent=2)

            res = subprocess.run(["rclone", "copyto", nome_arquivo, f"gdrive_dados:{nome_arquivo}"], capture_output=True, text=True)
            if res.returncode == 0:
                total_descobertos += len(conteudo_fase_a)
                mapa_drive[nome_arquivo] = os.path.getsize(nome_arquivo)
                print(f"   ✓ [FASE A] Gravado no Drive: {nome_arquivo} ({len(conteudo_fase_a)} registros)", flush=True)
            else:
                print(f"   ⚠️ Falha ao enviar {nome_arquivo}: {res.stderr}", flush=True)

    print(f">> Fase A concluída para [{regiao.upper()}]. Total de clusters mapeados: {total_descobertos}\n", flush=True)
    return total_descobertos


def executar_fase_b_extracao(cfg, regiao: str, meses_alvo: list, mapa_drive: dict) -> int:
    """Executa a Fase B: raspagem factual link por link e atualização atômica no Drive."""
    print(f"\n{'='*65}\nINICIANDO FASE B (RASPAGEM FACTUAL RESILIENTE): [{regiao.upper()}]\n{'='*65}", flush=True)
    timeout_req = getattr(cfg, "TIMEOUT_REQUISICAO", 6)
    max_workers = getattr(cfg, "MAX_WORKERS_PARALELO", 8)
    total_sucessos = 0

    for ano, mes in meses_alvo:
        tag_mes = f"{ano:04d}_{mes:02d}"

        for tema, _ in cfg.MONITORAMENTOS.items():
            tema_slug = processor.normalizar_nome_tema(tema)
            nome_arquivo = f"noticias_raw_{tag_mes}_{tema_slug}.json"

            if nome_arquivo not in mapa_drive:
                continue

            tamanho = mapa_drive[nome_arquivo]
            if tamanho <= 4:
                print(f"⚠️ [PULANDO FASE B] {nome_arquivo} está vazio no Drive (Fase A pendente).", flush=True)
                continue

            # Baixa o JSON atualizado do Google Drive
            proc_cat = subprocess.run(["rclone", "cat", f"gdrive_dados:{nome_arquivo}"], capture_output=True)
            if proc_cat.returncode != 0:
                print(f"⚠️ Erro ao ler {nome_arquivo} do Drive: {proc_cat.stderr.decode('utf-8', errors='replace')}", flush=True)
                continue

            try:
                clusters = json.loads(proc_cat.stdout.decode("utf-8"))
            except Exception as exc:
                print(f"⚠️ JSON ilegível em {nome_arquivo}: {exc}", flush=True)
                continue

            if not isinstance(clusters, list) or len(clusters) == 0:
                continue

            if clusters[0].get("status_extracao") == "SEM_NOTICIAS_NO_PERIODO":
                print(f"⏭️ [PULANDO FASE B] {nome_arquivo} marcado como 'SEM_NOTICIAS_NO_PERIODO'.", flush=True)
                continue

            itens_pendentes = [c for c in clusters if c.get("status_extracao") in ["PENDENTE", "CONTEUDO_BLOQUEADO"]]
            if not itens_pendentes:
                print(f"⏭️ [PULANDO FASE B] {nome_arquivo} já se encontra 100% extraído com sucesso.", flush=True)
                continue

            print(f"\n>> [FASE B] Processando {len(itens_pendentes)} clusters pendentes em: {nome_arquivo}...", flush=True)

            # Estágio 1: Fast HTTP em cascata
            def worker(c):
                time.sleep(random.uniform(0.05, 0.2))
                return processor.process_cluster_with_fallback(c, timeout=timeout_req)

            mapa_resolvidos = {}
            with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
                futuros = {executor.submit(worker, c): c for c in itens_pendentes}
                for f in concurrent.futures.as_completed(futuros):
                    res_c = f.result()
                    mapa_resolvidos[res_c["id_cluster"]] = res_c

            # Estágio 2: Playwright Stealth para os que falharam no Estágio 1
            bloqueados = [item for item in mapa_resolvidos.values() if item.get("status_extracao") != "SUCESSO"]
            if bloqueados:
                print(f"   Ativando Playwright Stealth para {len(bloqueados)} matérias retidas...", flush=True)
                recuperados = processor.executar_fallback_playwright(bloqueados)
                for rec in recuperados:
                    mapa_resolvidos[rec["id_cluster"]] = rec

            # Atualiza a coleção original preservando posições
            for idx, c in enumerate(clusters):
                cid = c.get("id_cluster")
                if cid in mapa_resolvidos:
                    clusters[idx] = mapa_resolvidos[cid]

            sucessos_arquivo = sum(1 for c in clusters if c.get("status_extracao") == "SUCESSO")
            total_sucessos += sucessos_arquivo
            print(f"   Resultado Fase B: {sucessos_arquivo}/{len(clusters)} textos válidos em {nome_arquivo}.", flush=True)

            with open(nome_arquivo, "w", encoding="utf-8") as f:
                json.dump(clusters, f, ensure_ascii=False, indent=2)

            res_copy = subprocess.run(["rclone", "copyto", nome_arquivo, f"gdrive_dados:{nome_arquivo}"], capture_output=True, text=True)
            if res_copy.returncode == 0:
                print(f"   ✓ [FASE B] Atualizado no Drive: {nome_arquivo}", flush=True)
            else:
                print(f"   ⚠️ Falha ao salvar Fase B em {nome_arquivo}: {res_copy.stderr}", flush=True)

    print(f">> Fase B concluída para [{regiao.upper()}]. Total de matérias extraídas: {total_sucessos}\n", flush=True)
    return total_sucessos


def executar_pipeline(caminho_ou_shard: str, inicio_mmaaaa: str = None, fim_mmaaaa: str = None, fase: str = "todas") -> None:
    cfg = carregar_modulo_config(caminho_ou_shard)
    regiao = getattr(cfg, "REGIAO_NOME", "GLOBAL").lower()

    print(">> Mapeando inventário unificado de arquivos no Google Drive...", flush=True)
    mapa_drive = carregar_mapa_inventario_drive()
    print(f"   Total de arquivos auditados em 'dados_brutos': {len(mapa_drive)}", flush=True)

    if inicio_mmaaaa and fim_mmaaaa:
        meses_alvo = gerar_meses_entre(inicio_mmaaaa, fim_mmaaaa)
    else:
        agora = datetime.now(FUSO_BRASILIA)
        meses_alvo = [(agora.year, agora.month)]

    print(f"SHARD: [{regiao.upper()}] | JANELA: {len(meses_alvo)} meses no escopo | FASE SELECIONADA: {fase.upper()}\n", flush=True)

    if fase in ["a", "todas"]:
        executar_fase_a_descoberta(cfg, regiao, meses_alvo, mapa_drive)

    if fase in ["b", "todas"]:
        executar_fase_b_extracao(cfg, regiao, meses_alvo, mapa_drive)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Orquestrador Multirregional Resiliente")
    parser.add_argument("--config", type=str, default=None)
    parser.add_argument("--shard", type=str, default=None)
    parser.add_argument("--inicio_mmaaaa", type=str, default=None, help="MMAAAA inicial (ex: 102021)")
    parser.add_argument("--fim_mmaaaa", type=str, default=None, help="MMAAAA final (ex: 092026)")
    parser.add_argument("--fase", type=str, default="todas", choices=["a", "b", "todas"], help="Fase a executar: a, b ou todas")
    args = parser.parse_args()

    alvo = args.shard if args.shard else args.config
    if not alvo:
        raise ValueError("É obrigatório informar --shard ou --config.")

    executar_pipeline(
        caminho_ou_shard=alvo,
        inicio_mmaaaa=args.inicio_mmaaaa,
        fim_mmaaaa=args.fim_mmaaaa,
        fase=args.fase,
    )
