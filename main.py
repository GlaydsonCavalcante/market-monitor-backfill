"""Orquestrador do ciclo: varredura, clustering, extração e exportação JSON/Excel."""

import concurrent.futures
from datetime import datetime
import json
import os
import random
import time
import config
from notifier import enviar_telegram
import pandas as pd
import processor


def executar_pipeline() -> None:
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    nome_json = f"noticias_{ts}.json"
    nome_excel = f"noticias_{ts}.xlsx"

    raw_articles = []
    print(
        f"Iniciando varredura RSS em {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}...",
        flush=True,
    )

    for tema, termos in config.MONITORAMENTOS.items():
        for termo in termos:
            for gl in config.PAISES_EMISSAO:
                for hl in config.IDIOMAS:
                    query = processor.build_rss_query(
                        termo,
                        config.TERMOS_EXCLUIDOS,
                        config.PERIODO_BUSCA,
                        config.DOMINIOS_PREFERENCIAIS,
                    )
                    itens = processor.fetch_rss_feed(query, hl=hl, gl=gl)
                    for item in itens:
                        item["tema"] = tema
                        item["termo_origem"] = termo
                        item["pais_emissao"] = gl
                        item["idioma"] = hl
                        raw_articles.append(item)

    print(f"Total bruto coletado: {len(raw_articles)} matérias.", flush=True)

    clusters = processor.cluster_articles(
        raw_articles,
        similarity_threshold=config.SIMILARIDADE_REDUNDANCIA,
    )

    def worker(cluster_item):
        time.sleep(random.uniform(0.4, 1.0))
        return processor.process_cluster_with_fallback(cluster_item)

    processed_results = []
    with concurrent.futures.ThreadPoolExecutor(
        max_workers=config.MAX_WORKERS_PARALELO
    ) as executor:
        futuros = {executor.submit(worker, c): c for c in clusters}
        for i, futuro in enumerate(concurrent.futures.as_completed(futuros), 1):
            res = futuro.result()
            processed_results.append(res)
            status_ico = (
                "✅" if res["status_extracao"] == "SUCESSO" else "🔒"
            )
            print(
                f"[{i}/{len(clusters)}] {status_ico} {res['titulo'][:60]}...",
                flush=True,
            )

    # 1. Arquivo JSON estruturado para a Fase 2 (com vetores 1024d)
    with open(nome_json, "w", encoding="utf-8") as f:
        json.dump(processed_results, f, ensure_ascii=False, indent=2)

    # 2. Planilha Excel de leitura imediata (sem vetores brutos)
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
                r.get("texto_completo")[:3000]
                if r.get("texto_completo")
                else ""
            ),
            "URLs_Espelho": ", ".join(r.get("urls_espelho_disponiveis", [])),
        })
    df_excel = pd.DataFrame(linhas_excel)
    df_excel.to_excel(nome_excel, index=False, engine="openpyxl")

    sucessos = sum(
        1 for r in processed_results if r["status_extracao"] == "SUCESSO"
    )
    bloqueados = len(processed_results) - sucessos

    # 3. Despacho Telegram
    enviar_telegram(
        arquivos=[nome_json, nome_excel],
        total_brutas=len(raw_articles),
        total_clusters=len(clusters),
        total_processadas=len(processed_results),
        sucessos=sucessos,
        bloqueados=bloqueados,
    )


if __name__ == "__main__":
    executar_pipeline()
