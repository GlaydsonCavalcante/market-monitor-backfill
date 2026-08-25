"""Orquestrador do pipeline com injeção dinâmica de configuração regional."""

import argparse
import concurrent.futures
from datetime import datetime
import importlib.util
import json
import os
import random
import sys
import time
from notifier import enviar_telegram
import pandas as pd
import processor


def carregar_modulo_config(caminho_config: str):
  """Carrega dinamicamente o arquivo de configuração passado por argumento."""
  if not os.path.exists(caminho_config):
    raise FileNotFoundError(
        f"Arquivo de configuração não encontrado: {caminho_config}"
    )
  spec = importlib.util.spec_from_file_location("config_modulo", caminho_config)
  modulo = importlib.util.module_from_spec(spec)
  sys.modules["config_modulo"] = modulo
  spec.loader.exec_module(modulo)
  return modulo


def executar_pipeline(caminho_config: str) -> None:
  cfg = carregar_modulo_config(caminho_config)
  regiao = getattr(cfg, "REGIAO_NOME", "GLOBAL").lower()
  ts = datetime.now().strftime("%Y%m%d_%H%M%S")

  nome_json = f"noticias_{regiao}_{ts}.json"
  nome_excel = f"noticias_{regiao}_{ts}.xlsx"

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

  # 2. Agrupamento Semântico no dia com BGE-M3
  clusters = processor.cluster_articles(
      raw_articles,
      model_name=cfg.MODELO_EMBEDDING_1024,
      similarity_threshold=cfg.SIMILARIDADE_REDUNDANCIA,
  )
  print(f"Clusters consolidados: {len(clusters)}", flush=True)

  # 3. Extração Concorrente de Rede
  def worker(cluster_item):
    time.sleep(random.uniform(0.1, 0.3))
    return processor.process_cluster_with_fallback(
        cluster_item, timeout=cfg.TIMEOUT_REQUISICAO
    )

  processed_results = []
  max_workers = getattr(cfg, "MAX_WORKERS_PARALELO", 8)
  with concurrent.futures.ThreadPoolExecutor(
      max_workers=max_workers
  ) as executor:
    futuros = {executor.submit(worker, c): c for c in clusters}
    for i, futuro in enumerate(concurrent.futures.as_completed(futuros), 1):
      res = futuro.result()
      processed_results.append(res)
      status_ico = "✅" if res["status_extracao"] == "SUCESSO" else "🔒"
      print(
          f"[{i}/{len(clusters)}] {status_ico} {res['titulo'][:60]}...",
          flush=True,
      )

  # 4. Vetorização 1024d em Lote (Batching BGE-M3)
  processor.gerar_vetores_em_lote(
      processed_results=processed_results,
      termos_descarte_dict=cfg.TERMOS_DESCARTE_TEXTO,
      model_name=cfg.MODELO_EMBEDDING_1024,
  )

  # 5. Exportação JSON e Excel
  with open(nome_json, "w", encoding="utf-8") as f:
    json.dump(processed_results, f, ensure_ascii=False, indent=2)

  linhas_excel = []
  for r in processed_results:
    linhas_excel.append({
        "ID_Cluster": r.get("id_cluster"),
        "Tema": r.get("tema"),
        "Título": r.get("titulo"),
        "Fonte": r.get("fonte_utilizada"),
        "Data_Notícia": r.get("data_noticia"),
        "Idioma": r.get("idioma"),
        "URL_Canônica": r.get("url_utilizada"),
        "Status_Extração": r.get("status_extracao"),
        "Texto_Completo": (
            r.get("texto_completo")[:3000] if r.get("texto_completo") else ""
        ),
        "URLs_Espelho": ", ".join(r.get("urls_espelho_disponiveis", [])),
    })
  df_excel = pd.DataFrame(linhas_excel)
  df_excel.to_excel(nome_excel, index=False, engine="openpyxl")

  sucessos = sum(
      1 for r in processed_results if r["status_extracao"] == "SUCESSO"
  )
  bloqueados = len(processed_results) - sucessos

  # 6. Despacho Telegram
  enviar_telegram(
      regiao_nome=regiao,
      arquivos=[nome_json, nome_excel],
      total_brutas=len(raw_articles),
      total_clusters=len(clusters),
      total_processadas=len(processed_results),
      sucessos=sucessos,
      bloqueados=bloqueados,
  )


if __name__ == "__main__":
  parser = argparse.ArgumentParser(
      description="Orquestrador de Monitoramento Regional"
  )
  parser.add_argument(
      "--config",
      type=str,
      default="configs/config_latam.py",
      help="Caminho do arquivo de configuração regional",
  )
  args = parser.parse_args()

  executar_pipeline(args.config)
