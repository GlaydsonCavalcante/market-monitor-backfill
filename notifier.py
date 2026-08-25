"""Módulo responsável pela formatação de relatórios e envio de mensagens via Telegram."""

from datetime import datetime
import os
import requests


def enviar_telegram(
    caminho_arquivo: str,
    total_brutas: int,
    total_clusters: int,
    total_processadas: int,
    sucessos: int,
    bloqueados: int,
) -> None:
    """Envia o arquivo consolidado e o sumário analítico para os destinatários."""
    bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
    chat_ids_raw = os.getenv("TELEGRAM_CHAT_ID")

    if not bot_token or not chat_ids_raw:
        print("TELEGRAM_BOT_TOKEN ou TELEGRAM_CHAT_ID ausentes no ambiente.", flush=True)
        return

    chat_ids = [c.strip() for c in chat_ids_raw.split(",") if c.strip()]
    url = f"https://api.telegram.org/bot{bot_token}/sendDocument"

    taxa_sucesso = (sucessos / total_processadas * 100) if total_processadas > 0 else 0
    resumo_msg = (
        "📊 <b>RELATÓRIO DE MONITORAMENTO DE MERCADO</b>\n\n"
        f"• <b>Data:</b> {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n"
        f"• <b>Matérias Brutas:</b> {total_brutas}\n"
        f"• <b>Clusters Únicos:</b> {total_clusters}\n"
        f"• <b>Total Processado:</b> {total_processadas}\n"
        f"• <b>Textos Extraídos:</b> {sucessos} ({taxa_sucesso:.1f}%)\n"
        f"• <b>Bloqueadas / Manuais:</b> {bloqueados}\n"
        f"• <b>Arquivo:</b> <code>{os.path.basename(caminho_arquivo)}</code>"
    )

    for chat_id in chat_ids:
        print(f"Despachando relatório para o Chat ID: {chat_id}...", flush=True)
        try:
            with open(caminho_arquivo, "rb") as doc:
                payload = {
                    "chat_id": chat_id,
                    "caption": resumo_msg,
                    "parse_mode": "HTML",
                }
                files = {"document": doc}
                resp = requests.post(url, data=payload, files=files, timeout=60)

                if resp.status_code == 200:
                    print(f"Entrega confirmada para: {chat_id}", flush=True)
                else:
                    print(f"Erro na entrega ({resp.status_code}): {resp.text}", flush=True)
        except Exception as err:
            print(f"Falha de conexão com Telegram para {chat_id}: {err}", flush=True)
