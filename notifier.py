"""
notifier.py

Módulo de despacho consolidado via Telegram com carimbo temporal
sincronizado no fuso horário oficial de Brasília (America/Sao_Paulo).
"""

from datetime import datetime
import os
from zoneinfo import ZoneInfo
import requests

FUSO_BRASILIA = ZoneInfo("America/Sao_Paulo")


def enviar_telegram(
    regiao_nome: str,
    arquivos: list,
    total_brutas: int,
    total_clusters: int,
    total_processadas: int,
    sucessos: int,
    bloqueados: int,
) -> None:
    """Envia sumário da execução regional e anexa arquivos JSON para os chats configurados."""
    bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
    chat_ids_raw = os.getenv("TELEGRAM_CHAT_ID")

    if not bot_token or not chat_ids_raw:
        print("[TELEGRAM] TELEGRAM_BOT_TOKEN ou TELEGRAM_CHAT_ID ausentes no ambiente.", flush=True)
        return

    chat_ids = [c.strip() for c in chat_ids_raw.split(",") if c.strip()]
    url_doc = f"https://api.telegram.org/bot{bot_token}/sendDocument"
    url_msg = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    taxa_sucesso = (sucessos / total_processadas * 100) if total_processadas > 0 else 0.0
    agora_bsb = datetime.now(FUSO_BRASILIA).strftime("%d/%m/%Y %H:%M:%S")

    resumo_msg = (
        f"📊 <b>RELATÓRIO REGIONAL: {regiao_nome.upper()}</b>\n\n"
        f"📅 <b>Data/Hora (BSB):</b> {agora_bsb}\n"
        f"📥 <b>Matérias Brutas:</b> {total_brutas}\n"
        f"🧩 <b>Clusters Únicos:</b> {total_clusters}\n"
        f"⚡ <b>Textos Extraídos:</b> {sucessos} ({taxa_sucesso:.1f}%)\n"
        f"🔒 <b>Bloqueadas / Manuais:</b> {bloqueados}\n\n"
        f"📎 <i>Anexos: JSON (ingestão Fase 2).</i>"
    )

    for chat_id in chat_ids:
        requests.post(
            url_msg,
            json={"chat_id": chat_id, "text": resumo_msg, "parse_mode": "HTML"},
            timeout=30,
        )
        for caminho in arquivos:
            if not os.path.exists(caminho):
                continue
            with open(caminho, "rb") as doc:
                requests.post(
                    url_doc,
                    data={"chat_id": chat_id},
                    files={"document": doc},
                    timeout=60,
                )
