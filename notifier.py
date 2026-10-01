"""
notifier.py

Módulo de despacho consolidado via Telegram para a esteira de Backfill Histórico:
- Sanitização de credenciais de ambiente (remoção de aspas, espaços e prefixos).
- Validação estrutural do padrão do token do BotFather (<id>:<hash>).
- Envio de sumário executivo regional em HTML no fuso oficial de Brasília.
- Despacho de anexos com nome e MIME type explícitos.
- Interrupção estrita (raise) em qualquer código HTTP divergente de 200.
"""

from datetime import datetime
import os
import re
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
    """
    Despacha relatório de telemetria da carga histórica para os chats configurados.
    Interrompe a execução imediatamente caso as credenciais sejam inválidas ou a API recuse a entrega.
    """
    raw_token = os.getenv("TELEGRAM_BOT_TOKEN", "").strip().strip('"').strip("'")
    chat_ids_raw = os.getenv("TELEGRAM_CHAT_ID", "").strip().strip('"').strip("'")

    if not raw_token:
        raise ValueError("A variável de ambiente TELEGRAM_BOT_TOKEN não foi definida.")
    if not chat_ids_raw:
        raise ValueError("A variável de ambiente TELEGRAM_CHAT_ID não foi definida.")

    # Remove eventual prefixo 'bot' acidental
    bot_token = raw_token[3:] if raw_token.lower().startswith("bot") else raw_token

    # Validação estrutural do padrão oficial do Telegram: <id_numerico>:<hash_alfanumerico>
    if not re.match(r"^\d{8,11}:[A-Za-z0-9_-]{30,}$", bot_token):
        raise ValueError(
            f"Formato inválido em TELEGRAM_BOT_TOKEN. "
            f"Comprimento: {len(bot_token)} caracteres. Esperado padrão '<id>:<hash>' do @BotFather."
        )

    chat_ids = [c.strip() for c in chat_ids_raw.split(",") if c.strip()]
    url_msg = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    url_doc = f"https://api.telegram.org/bot{bot_token}/sendDocument"

    taxa_sucesso = (sucessos / total_processadas * 100) if total_processadas > 0 else 0.0
    agora_bsb = datetime.now(FUSO_BRASILIA).strftime("%d/%m/%Y %H:%M:%S")

    resumo_msg = (
        f"📊 <b>CARGA HISTÓRICA (BACKFILL): {regiao_nome.upper()}</b>\n\n"
        f"📅 <b>Data/Hora (BSB):</b> {agora_bsb}\n"
        f"📥 <b>Matérias Mapeadas:</b> {total_brutas}\n"
        f"🧩 <b>Clusters Formados:</b> {total_clusters}\n"
        f"⚡ <b>Textos Extraídos:</b> {sucessos} ({taxa_sucesso:.1f}%)\n"
        f"🔒 <b>Bloqueadas / Pendentes:</b> {bloqueados}\n\n"
        f"💾 <i>Status: Persistido no Google Drive via Rclone.</i>"
    )

    for chat_id in chat_ids:
        # 1. Envio da telemetria em HTML
        resp_msg = requests.post(
            url_msg,
            json={"chat_id": chat_id, "text": resumo_msg, "parse_mode": "HTML"},
            timeout=30,
        )
        if resp_msg.status_code != 200:
            raise RuntimeError(
                f"Falha ao enviar mensagem Telegram para {chat_id} (HTTP {resp_msg.status_code}): {resp_msg.text}"
            )

        # 2. Envio de anexos (limitado aos 5 primeiros arquivos para evitar HTTP 429 Rate Limit)
        for caminho in arquivos[:5]:
            if not os.path.exists(caminho):
                continue
            nome_arquivo = os.path.basename(caminho)
            with open(caminho, "rb") as doc:
                resp_doc = requests.post(
                    url_doc,
                    data={"chat_id": chat_id},
                    files={"document": (nome_arquivo, doc, "application/json")},
                    timeout=60,
                )
                if resp_doc.status_code != 200:
                    raise RuntimeError(
                        f"Falha ao enviar documento {nome_arquivo} para {chat_id} (HTTP {resp_doc.status_code}): {resp_doc.text}"
                    )
