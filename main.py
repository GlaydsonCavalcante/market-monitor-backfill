"""Orquestrador principal do pipeline de monitoramento de mercado."""

import concurrent.futures
from datetime import datetime
import json
import os
import random
import time

import config
from notifier import enviar_telegram
import processor


def executar_pipeline() -> None:
    """Executa o ciclo completo: coleta, agrupamento, extração e notificação."""
    nome_arquivo_saida = f"noticias_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    raw_articles = []

    print(f"Iniciando varredura RSS em {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}...", flush=True)
    for tema, termos in config.MONITORAMENTOS.items():
        print(f">> Tema em processamento: {tema}", flush=True)
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

    print(f"Iniciando extração de conteúdo em paralelo ({len(clusters)} clusters)...", flush=True)

    def worker(cluster_item):
        time.sleep(random.uniform(0.4, 1.0))
        return processor.process_cluster_with_fallback(cluster_item)

    processed_results = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=config.MAX_WORKERS_PARALELO) as executor:
        futuros = {executor.submit(worker, c): c for c in clusters}
        for i, futuro in enumerate(concurrent.futures.as_completed(futuros), 1):
            res = futuro.result()
            processed_results.append(res)
            status_ico = "✅" if res["status_extracao"] == "SUCESSO" else "🔒"
            print(f"[{i}/{len(clusters)}] {status_ico} {res['titulo'][:60]}...", flush=True)

    with open(nome_arquivo_saida, "w", encoding="utf-8") as f:
        json.dump(processed_results, f, ensure_ascii=False, indent=2)

    sucessos = sum(1 for r in processed_results if r["status_extracao"] == "SUCESSO")
    bloqueados = len(processed_results) - sucessos

    enviar_telegram(
        caminho_arquivo=nome_arquivo_saida,
        total_brutas=len(raw_articles),
        total_clusters=len(clusters),
        total_processadas=len(processed_results),
        sucessos=sucessos,
        bloqueados=bloqueados,
    )


if __name__ == "__main__":
    executar_pipeline()
