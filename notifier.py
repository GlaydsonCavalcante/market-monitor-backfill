"""Módulo de despacho consolidado via Telegram."""

from datetime import datetime
import os
import requests


def enviar_telegram(
    regiao_nome: str,
    arquivos: list,
    total_brutas: int,
    total_clusters: int,
    total_processadas: int,
    sucessos: int,
    bloqueados: int,
) -> None:
  bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
  chat_ids_raw = os.getenv("TELEGRAM_CHAT_ID")

  if not bot_token or not chat_ids_raw:
    print(
        "TELEGRAM_BOT_TOKEN ou TELEGRAM_CHAT_ID ausentes no ambiente.",
        flush=True,
    )
    return

  chat_ids = [c.strip() for c in chat_ids_raw.split(",") if c.strip()]
  url_doc = f"https://api.telegram.org/bot{bot_token}/sendDocument"
  url_msg = f"https://api.telegram.org/bot{bot_token}/sendMessage"
  taxa_sucesso = (
      (sucessos / total_processadas * 100) if total_processadas > 0 else 0
  )

  resumo_msg = (
      f"📊 <b>RELATÓRIO REGIONAL: {regiao_nome.upper()}</b>\n\n"
      f"📅 <b>Data:</b> {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n"
      f"📥 <b>Matérias Brutas:</b> {total_brutas}\n"
      f"🧩 <b>Clusters Únicos:</b> {total_clusters}\n"
      f"⚡ <b>Textos Extraídos:</b> {sucessos} ({taxa_sucesso:.1f}%)\n"
      f"🔒 <b>Bloqueadas / Manuais:</b> {bloqueados}\n\n"
      "📎 <i>Anexos: JSON (ingestão Fase 2).</i>"
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
      try:
        with open(caminho, "rb") as doc:
          requests.post(
              url_doc,
              data={"chat_id": chat_id},
              files={"document": doc},
              timeout=60,
          )
      except Exception as err:
        print(f"Erro ao despachar {caminho} para {chat_id}: {err}", flush=True)
