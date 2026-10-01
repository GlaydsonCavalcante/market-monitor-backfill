"""Orquestrador do pipeline com injeção dinâmica de configuração regional."""

import time
from zoneinfo import ZoneInfo

os.environ["TZ"] = "America/Sao_Paulo"
if hasattr(time, "tzset"):
    time.tzset()

FUSO_BRASILIA = ZoneInfo("America/Sao_Paulo")

import argparse
import concurrent.futures
from datetime import datetime
import importlib.util
import json
import os
import random
import re
import sys
from notifier import enviar_telegram
import pandas as pd
import processor
import subprocess
import types
from zoneinfo import ZoneInfo

FUSO_BRASILIA = ZoneInfo("America/Sao_Paulo")


def carregar_modulo_config(caminho_ou_shard: str):
    """
    Carrega a configuração dinamicamente na memória RAM.
    Lê do disco se for caminho local ou faz streaming do Google Drive via Rclone.
    Suporta fallback de encoding (UTF-8, UTF-8-BOM, UTF-16) sem gravar arquivos.
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

    # Decodificação tolerante a múltiplos encodings
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

ts = datetime.now(FUSO_BRASILIA).strftime("%Y%m%d_%H%M%S")

def executar_pipeline(caminho_config: str) -> None:
  cfg = carregar_modulo_config(caminho_config)
  regiao = getattr(cfg, "REGIAO_NOME", "GLOBAL").lower()
  ts = datetime.now().strftime("%Y%m%d_%H%M%S")

  nome_json = f"noticias_{regiao}_{ts}.json"
  # nome_excel = f"noticias_{regiao}_{ts}.xlsx"

  raw_articles = []
  print(
      f"Iniciando varredura regional [{regiao.upper()}] em"
      f" {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}...",
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

  # 2. Agrupamento Semântico no dia com prefixo regional para unicidade relacional
  clusters = processor.cluster_articles(
      raw_articles,
      model_name=cfg.MODELO_EMBEDDING_1024,
      similarity_threshold=cfg.SIMILARIDADE_REDUNDANCIA,
      regiao_prefix=regiao,
  )
  print(f"Clusters consolidados: {len(clusters)}", flush=True)
  
  # 3. Extração Concorrente de Rede
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
    for i, futuro in enumerate(concurrent.futures.as_completed(futuros), 1):
      res = futuro.result()
      processed_results.append(res)

  sucessos_estagio1 = sum(1 for r in processed_results if r["status_extracao"] == "SUCESSO")
  print(f">> Estágio 1 (HTTP) concluído: {sucessos_estagio1}/{len(clusters)} extraídos com sucesso.", flush=True)

  # 3.2 Estágio 2: Headless Browser Playwright (apenas para quem ficou bloqueado)
  bloqueados_indices = [i for i, r in enumerate(processed_results) if r["status_extracao"] != "SUCESSO"]
  if bloqueados_indices:
    print(f">> Estágio 2: Ativando Playwright Stealth para {len(bloqueados_indices)} matérias protegidas...", flush=True)
    itens_para_pw = [processed_results[i] for i in bloqueados_indices]
    itens_recuperados = processor.executar_fallback_playwright(itens_para_pw)
    
    # Atualiza a lista principal com os resgates do Playwright
    for pos, idx_original in enumerate(bloqueados_indices):
      processed_results[idx_original] = itens_recuperados[pos]

  for i, res in enumerate(processed_results, 1):
    status_ico = "✅" if res["status_extracao"] == "SUCESSO" else "🔒"
    print(f"[{i}/{len(clusters)}] {status_ico} {res['titulo'][:60]}...", flush=True)
    
  # # 4. Vetorização 1024d em Lote (Batching BGE-M3)
  # processor.gerar_vetores_em_lote(
  #     processed_results=processed_results,
  #     termos_descarte_dict=cfg.TERMOS_DESCARTE_TEXTO,
  #     model_name=cfg.MODELO_EMBEDDING_1024,
  # )

  # 5. Exporta o JSON com vetor_1024 compactado em linha única
  json_formatado = json.dumps(processed_results, ensure_ascii=False, indent=2)
  json_compactado = re.sub(
      r'("vetor_1024":\s*\[)([\s\d.,eE+-]+)(\])',
      lambda m: m.group(1) + " ".join(m.group(2).split()) + m.group(3),
      json_formatado,
  )
  
  with open(nome_json, "w", encoding="utf-8") as f:
      f.write(json_compactado)

  # linhas_excel = []
  # for r in processed_results:
  #   linhas_excel.append({
  #       "ID_Cluster": r.get("id_cluster"),
  #       "Tema": r.get("tema"),
  #       "Título": r.get("titulo"),
  #       "Fonte": r.get("fonte_utilizada"),
  #       "Data_Notícia": r.get("data_noticia"),
  #       "Idioma": r.get("idioma"),
  #       "URL_Canônica": r.get("url_utilizada"),
  #       "Status_Extração": r.get("status_extracao"),
  #       "Texto_Completo": (
  #           r.get("texto_completo")[:3000] if r.get("texto_completo") else ""
  #       ),
  #       "URLs_Espelho": ", ".join(r.get("urls_espelho_disponiveis", [])),
  #   })
  # df_excel = pd.DataFrame(linhas_excel)
  # df_excel.to_excel(nome_excel, index=False, engine="openpyxl")

  sucessos = sum(1 for r in processed_results if r["status_extracao"] == "SUCESSO")
  bloqueados = len(processed_results) - sucessos

  # 6. Despacho Telegram
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
