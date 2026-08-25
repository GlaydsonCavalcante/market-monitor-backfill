"""Configurações e parâmetros gerais de monitoramento."""

# PAÍSES DE EMISSÃO (Região geográfica da fonte/veículo de notícia - ISO 3166-1 alpha-2)
# BR: Brasil (Base)
# US: EUA (Hegemonia atual/Tech)
# GB: Reino Unido (Finanças/Geopolítica)
# PT: Portugal (Europa/Pontes lusófonas)
# ES: Espanha (Europa/Pontes hispânicas)
# CN: China (Superpotência/Tech)
# IN: Índia (Demografia/Crescimento)
# DE: Alemanha (Líder Europeu/Energia)
# JP: Japão (Automação/Envelhecimento)
# AU: Austrália (Minerais críticos/Transição)
# ID: Indonésia (Sudeste Asiático/Recursos)
# NG: Nigéria (Futuro demográfico da África)

PAISES_EMISSAO = ["BR", "US", "GB", "PT", "ES", "CN", "IN", "DE", "JP", "AU", "ID", "NG"]

# IDIOMAS (Língua em que a matéria foi redigida - BCP 47)
# Nota: Corrigido "en-UK" para o padrão oficial "en-GB"
IDIOMAS = [
    "pt-BR", "pt-PT",
    "en-US", "en-GB", "en-IN", "en-NG", "en-AU",
    "es-ES",
    "zh-CN",
    "hi",
    "de",
    "ja",
    "id"
]

# JANELA TEMPORAL DE BUSCA (Operador when: do Google Notícias), Opções válidas:
#   "1d"  -> Últimas 24 horas               "7d"  -> Últimos 7 dias (Recomendado para rotina semanal)
#   "30d" -> Últimos 30 dias (Último mês)   "90d" -> Últimos 3 meses                "1y"  -> Último ano
PERIODO_BUSCA = "1d"

# TERMOS EXCLUÍDOS (Palavras para descartar ruídos e notícias irrelevantes):
TERMOS_EXCLUIDOS = ["esporte", "futebol", "celebridade", "horóscopo", "receita"]

# FONTES / DOMÍNIOS PREFERENCIAIS (Opcional - deixe vazio [] para pesquisar em toda a web):
# Exemplo: ["valor.globo.com", "infomoney.com.br", "finsidersbrasil.com.br"]
DOMINIOS_PREFERENCIAIS = []

# SENSIBILIDADE DE DESDUPLICAÇÃO SEMÂNTICA:
# Valor entre 0.0 e 1.0 (quanto maior, mais parecidos os títulos precisam ser para agrupar)
SIMILARIDADE_REDUNDANCIA = 0.88

# ESTRUTURA DE MONITORAMENTO (Temas e termos de busca):
MONITORAMENTOS = {
    "Comércio Agentico": [
        '"inteligência artificial" bancos',
        '"IA como Orquestradora da Jornada de Compra"',
        '"IA autônoma"',
        'Phygital Omnicanalidade',
        '"Jornadas hiperpersonalizadas"',
        '"Experiências imersivas" "Social Commerce"'
    ],
    "Longevidade": [
        '"reconfiguração demográfica"',
        '"Envelhecimento da população"',
        '"Pacto intergeracional"',
        '"Saúde digital" "medicina personalizada"',
        '"Longevidade ativa" bem-estar "cuidado contínuo"',
        '"Terapias avançadas" "bioengenharia genética"',
    ],
}

"""# Funções de Resolução de URLs, NLP e Extração de Texto"""
# Célula 3: Funções de busca, desduplicação, resolução determinística de URLs e extração
import base64
from datetime import datetime
import json
import os
import random
import re
import time
import urllib.parse
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
from googlenewsdecoder import new_decoderv1
import numpy as np
import pandas as pd
from rapidfuzz import fuzz
import requests
from sentence_transformers import SentenceTransformer
import trafilatura

# Rotação de User-Agents modernos
USER_AGENTS = [
    (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML,"
        " like Gecko) Chrome/124.0.0.0 Safari/537.36"
    ),
    (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
        " (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
    ),
    (
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like"
        " Gecko) Chrome/122.0.0.0 Safari/537.36"
    ),
]


def build_rss_query(
    base_term: str,
    excluded_terms: list,
    period: str,
    preferred_domains: list,
) -> str:
    """Monta a query combinando termo, período, fontes e termos excluídos."""
    parts = [base_term]
    if period:
        parts.append(f"when:{period}")
    if preferred_domains:
        sites_query = " OR ".join(
            [f"site:{domain}" for domain in preferred_domains]
        )
        parts.append(f"({sites_query})")
    if excluded_terms:
        parts.extend([f"-{term}" for term in excluded_terms])
    return " ".join(parts)


def fetch_rss_feed(query: str, hl: str, gl: str) -> list:
    """Consulta o Google News RSS e extrai metadados dos artigos."""
    encoded_query = urllib.parse.quote(query)
    ceid = f"{hl.upper()}:{gl.upper()}"
    url = f"https://news.google.com/rss/search?q={encoded_query}&hl={hl}&gl={gl}&ceid={ceid}"

    headers = {"User-Agent": random.choice(USER_AGENTS)}
    try:
        response = requests.get(url, headers=headers, timeout=12)
        if response.status_code != 200:
            return []

        root = ET.fromstring(response.content)
        feed_items = []

        for item in root.findall(".//channel/item"):
            title = (
                item.find("title").text
                if item.find("title") is not None
                else ""
            )
            link = (
                item.find("link").text if item.find("link") is not None else ""
            )
            pub_date = (
                item.find("pubDate").text
                if item.find("pubDate") is not None
                else ""
            )
            source = (
                item.find("source").text
                if item.find("source") is not None
                else "Google News"
            )
            snippet = (
                item.find("description").text
                if item.find("description") is not None
                else ""
            )

            feed_items.append({
                "titulo": title.strip(),
                "link": link.strip(),
                "data_noticia": pub_date.strip(),
                "fonte": source.strip(),
                "snippet": snippet.strip(),
            })
        return feed_items
    except Exception:
        return []


def cluster_articles(
    raw_articles: list, similarity_threshold: float = 0.88
) -> list:
    """Agrupa notícias similares em clusters via embeddings multilingues e fuzzy matching."""
    if not raw_articles:
        return []

    print("Carregando modelo de similaridade semântica para agrupamento...")
    model = SentenceTransformer(
        "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
    )

    titles = [a["titulo"] for a in raw_articles]
    embeddings = model.encode(
        titles, convert_to_numpy=True, normalize_embeddings=True
    )

    clusters = []
    visited = set()

    for i in range(len(raw_articles)):
        if i in visited:
            continue

        cluster_members = [raw_articles[i]]
        visited.add(i)

        for j in range(i + 1, len(raw_articles)):
            if j in visited:
                continue

            fuzzy_sim = fuzz.token_set_ratio(titles[i], titles[j]) / 100.0
            cosine_sim = float(np.dot(embeddings[i], embeddings[j]))

            # Critério duplo para evitar agrupar notícias distintas sobre o mesmo tema geral
            if (
                cosine_sim >= similarity_threshold and fuzzy_sim >= 0.80
            ) or fuzzy_sim >= 0.92:
                cluster_members.append(raw_articles[j])
                visited.add(j)

        primary = cluster_members[0]
        # Limita espelhos a no máximo 2 para evitar sobrecarga de requisições
        mirrors = [
            m["link"]
            for m in cluster_members[1:3]
            if m["link"] != primary["link"]
        ]

        clusters.append({
            "id_cluster": (
                f"CLUS_{datetime.now().strftime('%Y%m%d')}_{len(clusters) + 1:04d}"
            ),
            "tema": primary["tema"],
            "termo_origem": primary["termo_origem"],
            "titulo": primary["titulo"],
            "data_noticia": primary["data_noticia"],
            "fonte_principal": primary["fonte"],
            "url_primaria": primary["link"],
            "urls_espelho": mirrors,
            "snippet": primary["snippet"],
            "pais_emissao": primary["pais_emissao"],
            "idioma": primary["idioma"],
        })
    return clusters


def decode_token_offline(token: str) -> str:
    """Extrai a URL real diretamente dos bytes do protobuf em base64 (sem requisições externas)."""
    try:
        padded = token + "=" * (-len(token) % 4)
        raw_bytes = base64.urlsafe_b64decode(padded)
        matches = re.findall(
            rb"https?://[a-zA-Z0-9_\-\.\/\?\=\&\%\#\:\@]+", raw_bytes
        )
        for url_bytes in matches:
            url_str = url_bytes.decode("utf-8", errors="ignore")
            if (
                "google.com" not in url_str
                and "schema.org" not in url_str
                and len(url_str) > 15
            ):
                return url_str
    except Exception:
        pass
    return None


def resolve_publisher_url(google_news_url: str) -> str:
    """Resolve a URL direta do portal com decodificação offline e fallbacks seguros."""
    if not google_news_url or "news.google.com" not in google_news_url:
        return google_news_url

    clean_url = google_news_url.split("?")[0].strip()
    match = re.search(r"/articles/([^/?&]+)", clean_url)
    token = match.group(1) if match else None

    # 1. Tentativa offline direta (imune a rate limit)
    if token:
        extracted = decode_token_offline(token)
        if extracted:
            return extracted

    # 2. Tentativa via googlenewsdecoder
    try:
        res = new_decoderv1(google_news_url)
        if res.get("status") and res.get("decoded_url"):
            decoded = res["decoded_url"]
            if decoded.startswith("http") and "news.google.com" not in decoded:
                return decoded
    except Exception:
        pass

    # 3. Fallback via requisição direta ao link
    try:
        headers = {"User-Agent": random.choice(USER_AGENTS)}
        resp = requests.get(google_news_url, headers=headers, timeout=6)
        if resp.status_code == 200:
            soup = BeautifulSoup(resp.text, "html.parser")
            canonical = soup.find("link", rel="canonical")
            if (
                canonical
                and canonical.get("href")
                and "google.com" not in canonical["href"]
            ):
                return canonical["href"]
            for a in soup.find_all("a", href=True):
                href = a["href"]
                if href.startswith("http") and "google.com" not in href:
                    return href
    except Exception:
        pass

    return google_news_url


def scrape_article_text(url: str) -> tuple:
    """Extrai o texto integral diretamente no domínio do veículo jornalístico."""
    real_url = resolve_publisher_url(url)

    # Se a URL não foi decodificada e manteve o link do Google, aborta para não ler página vazia
    if "news.google.com" in real_url:
        return None, "FALHA_DECODIFICACAO_URL", real_url

    try:
        headers = {
            "User-Agent": random.choice(USER_AGENTS),
            "Accept": (
                "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
            ),
            "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7,es;q=0.6",
        }
        html_content = None

        resp = requests.get(real_url, headers=headers, timeout=12)
        if resp.status_code == 200:
            html_content = resp.text
        else:
            return None, f"FALHA_HTTP_{resp.status_code}", real_url

        if not html_content:
            return None, "FALHA_CONTEUDO_VAZIO", real_url

        # Extração primária com trafilatura
        text = trafilatura.extract(
            html_content,
            include_comments=False,
            include_tables=False,
            include_links=False,
            output_format="txt",
        )

        # Fallback com BeautifulSoup para portais com markup específico
        if not text or len(text.strip()) < 150:
            soup = BeautifulSoup(html_content, "html.parser")
            for tag in soup(
                ["script", "style", "nav", "header", "footer", "aside", "form"]
            ):
                tag.decompose()
            paragraphs = [
                p.get_text().strip()
                for p in soup.find_all("p")
                if len(p.get_text().strip()) > 35
            ]
            text = "\n\n".join(paragraphs)

        if text and len(text.strip()) > 150:
            return text.strip(), "SUCESSO", real_url
        return None, "CONTEUDO_INSUFICIENTE", real_url

    except Exception as exc:
        return None, f"ERRO_EXCEPTION: {str(exc)}", real_url


def process_cluster_with_fallback(cluster: dict) -> dict:
    """Processa o cluster decodificando URLs e gravando links finais dos publishers."""
    urls_to_try = [cluster["url_primaria"]] + cluster["urls_espelho"]
    historico = []

    # Decodifica previamente todos os links espelho
    espelhos_decodificados = [
        resolve_publisher_url(espelho) for espelho in cluster["urls_espelho"]
    ]

    primeira_url_decodificada = None

    for link in urls_to_try:
        texto, status, final_url = scrape_article_text(link)

        if primeira_url_decodificada is None:
            primeira_url_decodificada = final_url

        historico.append({
            "url_original_rss": link,
            "url_canonica_decodificada": final_url,
            "status": status,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        })

        if status == "SUCESSO":
            return {
                "id_cluster": cluster["id_cluster"],
                "tema": cluster["tema"],
                "termo_origem": cluster["termo_origem"],
                "titulo": cluster["titulo"],
                "data_noticia": cluster["data_noticia"],
                "idioma": cluster["idioma"],
                "fonte_utilizada": cluster["fonte_principal"],
                "url_utilizada": final_url,
                "urls_espelho_disponiveis": espelhos_decodificados,
                "status_extracao": "SUCESSO",
                "texto_completo": texto,
                "motivo_bloqueio": None,
                "necessita_extracao_manual": False,
                "historico_tentativas": historico,
            }

    # Em caso de bloqueio, garante a URL canônica decodificada registrada
    return {
        "id_cluster": cluster["id_cluster"],
        "tema": cluster["tema"],
        "termo_origem": cluster["termo_origem"],
        "titulo": cluster["titulo"],
        "data_noticia": cluster["data_noticia"],
        "idioma": cluster["idioma"],
        "fonte_utilizada": cluster["fonte_principal"],
        "url_utilizada": (
            primeira_url_decodificada
            if primeira_url_decodificada
            else cluster["url_primaria"]
        ),
        "urls_espelho_disponiveis": espelhos_decodificados,
        "status_extracao": "BLOQUEADO",
        "texto_completo": "[CONTEUDO_BLOQUEADO]",
        "motivo_bloqueio": (
            f"Acesso protegido ou indisponível em todas as {len(urls_to_try)}"
            " fontes testadas."
        ),
        "necessita_extracao_manual": True,
        "historico_tentativas": historico,
    }

"""# Execução do Motor e Exportação"""

import concurrent.futures
from datetime import datetime
import json
import os
import random
import time
import requests

RAW_LAKE_FILE = "lake_raw_noticias.json"
FINAL_OUTPUT_JSON = (
    f"noticias_processadas_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
)

MAX_WORKERS_PARALELO = globals().get("MAX_WORKERS_PARALELO", 4)


def enviar_telegram(
    caminho_arquivo: str,
    total_brutas: int,
    total_clusters: int,
    total_processadas: int,
    sucessos: int,
    bloqueados: int,
) -> None:
    """Dispara o arquivo final gerado e o resumo da execução para o Telegram.

    Args:
        caminho_arquivo: Caminho do arquivo JSON consolidado.
        total_brutas: Quantidade total de matérias brutas coletadas via RSS.
        total_clusters: Quantidade de clusters únicos gerados pela IA.
        total_processadas: Total de registros finais processados.
        sucessos: Matérias com texto integral extraído com sucesso.
        bloqueados: Matérias bloqueadas por paywall ou proteção.
    """
    bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
    chat_ids_raw = os.getenv("TELEGRAM_CHAT_ID")

    if not bot_token or not chat_ids_raw:
        print("TELEGRAM_BOT_TOKEN ou TELEGRAM_CHAT_ID ausentes no ambiente.")
        return

    chat_ids = [c.strip() for c in chat_ids_raw.split(",") if c.strip()]
    url = f"https://api.telegram.org/bot{bot_token}/sendDocument"

    # Montagem do relatório com o mesmo padrão exibido em tela
    taxa_sucesso = (
        (sucessos / total_processadas * 100) if total_processadas > 0 else 0
    )
    resumo_msg = (
        "<b>RELATÓRIO DE MONITORAMENTO DE MERCADO</b>\n\n"
        f"• <b>Data/Hora:</b> {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n"
        f"• <b>Matérias Brutas Coletadas:</b> {total_brutas}\n"
        f"• <b>Clusters Únicos (Deduplicação):</b> {total_clusters}\n"
        f"• <b>Total de Notícias Únicas:</b> {total_processadas}\n"
        f"• <b>Textos Completos Extraídos:</b> {sucessos} ({taxa_sucesso:.1f}%)\n"
        f"• <b>Necessitam Busca Manual (Bloqueadas):</b> {bloqueados}\n"
        f"• <b>Arquivo Gerado:</b> <code>{os.path.basename(caminho_arquivo)}</code>"
    )

    for chat_id in chat_ids:
        with open(caminho_arquivo, "rb") as doc:
            payload = {
                "chat_id": chat_id,
                "caption": resumo_msg,
                "parse_mode": "HTML",
            }
            files = {"document": doc}
            resp = requests.post(url, data=payload, files=files, timeout=60)
            resp.raise_for_status()
            print(f"Relatório e anexo entregues para: {chat_id}")


# ==========================================
# EXECUÇÃO PRINCIPAL (FLUXO COMPLETO)
# ==========================================
if __name__ == "__main__":
    RAW_LAKE_FILE = "lake_raw_noticias.json"
    CHECKPOINT_FILE = "checkpoint_processamento.json"
    FINAL_OUTPUT_JSON = (
        f"noticias_processadas_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    )

    # 1. Coleta RSS
    raw_articles = []
    if os.path.exists(RAW_LAKE_FILE):
        print(f"Carregando registros brutos de '{RAW_LAKE_FILE}'...")
        with open(RAW_LAKE_FILE, "r", encoding="utf-8") as f:
            raw_articles = json.load(f)
    else:
        print(
            f"Iniciando varredura RSS em {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}..."
        )
        for tema, termos in MONITORAMENTOS.items():
            print(f">> Tema: {tema}")
            for termo in termos:
                for gl in PAISES_EMISSAO:
                    for hl in IDIOMAS:
                        q = build_rss_query(
                            termo,
                            TERMOS_EXCLUIDOS,
                            PERIODO_BUSCA,
                            DOMINIOS_PREFERENCIAIS,
                        )
                        itens = fetch_rss_feed(q, hl=hl, gl=gl)
                        for item in itens:
                            item["tema"] = tema
                            item["termo_origem"] = termo
                            item["pais_emissao"] = gl
                            item["idioma"] = hl
                            raw_articles.append(item)

        with open(RAW_LAKE_FILE, "w", encoding="utf-8") as f:
            json.dump(raw_articles, f, ensure_ascii=False, indent=2)
        print(f"Coleta concluída: {len(raw_articles)} matérias no lake.")

    # 2. Deduplicação Semântica (Criação da variável 'clusters')
    clusters = cluster_articles(
        raw_articles,
        similarity_threshold=globals().get("SIMILARIDADE_REDUNDANCIA", 0.88),
    )
    print(
        f"Deduplicação concluída: {len(raw_articles)} matérias agrupadas em {len(clusters)} clusters.\n"
    )

    # 3. Extração Multithread com Persistência
    checkpoint_data = {}
    if os.path.exists(CHECKPOINT_FILE):
        with open(CHECKPOINT_FILE, "r", encoding="utf-8") as f:
            checkpoint_data = json.load(f)

    clusters_pendentes = [
        c for c in clusters if c["id_cluster"] not in checkpoint_data
    ]
    print(
        f"Iniciando extração ({len(clusters_pendentes)} pendentes de {len(clusters)} totais)..."
    )

    def worker_extracao(cluster_item):
        time.sleep(random.uniform(0.4, 1.0))
        return process_cluster_with_fallback(cluster_item)

    with concurrent.futures.ThreadPoolExecutor(
        max_workers=MAX_WORKERS_PARALELO
    ) as executor:
        futuros = {
            executor.submit(worker_extracao, c): c for c in clusters_pendentes
        }

        for i, futuro in enumerate(concurrent.futures.as_completed(futuros), 1):
            try:
                resultado = futuro.result()
                c_id = resultado["id_cluster"]
                checkpoint_data[c_id] = resultado

                status_icon = (
                    "✅" if resultado["status_extracao"] == "SUCESSO" else "🔒"
                )
                print(
                    f"[{i}/{len(clusters_pendentes)}] {status_icon} {resultado['titulo'][:60]}..."
                )

                if i % 10 == 0 or i == len(clusters_pendentes):
                    with open(CHECKPOINT_FILE, "w", encoding="utf-8") as f:
                        json.dump(
                            checkpoint_data, f, ensure_ascii=False, indent=2
                        )
            except Exception:
                pass

    # 4. Consolidação e Envio do Relatório
    processed_results = list(checkpoint_data.values())

    with open(FINAL_OUTPUT_JSON, "w", encoding="utf-8") as f:
        json.dump(processed_results, f, ensure_ascii=False, indent=2)

    sucessos = sum(
        1 for r in processed_results if r["status_extracao"] == "SUCESSO"
    )
    bloqueados = len(processed_results) - sucessos

    enviar_telegram(
        caminho_arquivo=FINAL_OUTPUT_JSON,
        total_brutas=len(raw_articles),
        total_clusters=len(clusters),
        total_processadas=len(processed_results),
        sucessos=sucessos,
        bloqueados=bloqueados,
    )
