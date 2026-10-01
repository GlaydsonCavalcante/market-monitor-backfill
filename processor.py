"""
processor.py

Módulo de processamento RSS, desduplicação, extração resiliente com validação
factual, fallback em espelhos de cluster e vetorização em lote com BAAI/bge-m3.
"""

import asyncio
import base64
from datetime import datetime
import math
import os
import random
import re
import time
from typing import Dict, List, Optional, Tuple
import urllib.parse
import xml.etree.ElementTree as ET
from zoneinfo import ZoneInfo

from bs4 import BeautifulSoup
import googlenewsdecoder
import numpy as np
from playwright.async_api import async_playwright
import requests
from sentence_transformers import SentenceTransformer
import trafilatura

FUSO_BRASILIA = ZoneInfo("America/Sao_Paulo")

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
]

TAMANHO_MINIMO_TEXTO = 150

DOMINIOS_MIDIA = {
    "youtube.com", "youtu.be", "spotify.com", "open.spotify.com",
    "soundcloud.com", "vimeo.com", "globoplay.globo.com", "podcasts.apple.com"
}
DOMINIOS_FECHADOS = {
    "twitter.com", "x.com", "facebook.com", "instagram.com", "linkedin.com"
}

PADROES_ANTIBOT = [
    r"unsanctioned scraping by bots",
    r"instituted a challenge designed to keep them out",
    r"enable javascript and cookies to continue",
    r"checking your browser before accessing",
    r"attention required!? \| cloudflare",
    r"please verify you are a human",
    r"access denied \| \d+ access denied",
    r"access\s+denied",
    r"you\s+don'?t\s+have\s+permission\s+to\s+access",
    r"error\s+loading\s+chunks",
    r"ray id: [a-f0-9]{16}",
    r"incident\s+id:",
    r"pardon our interruption",
    r"verifique se você é humano",
    r"ative o javascript para continuar",
    r"acesso negado",
    r"security check to access",
    r"ddos protection by cloudflare",
    r"block details:.*incident id",
    r"perimeterx",
    r"datadome",
    r"akamai\s*ghost",
    r"403\s+forbidden",
    r"401\s+unauthorized",
    r"acceso\s+denegado",
    r"permiso\s+denegado",
    r"accès\s+refusé",
    r"zugriff\s+verweigert",
    r"página\s+não\s+encontrada",
]
REGEX_ANTIBOT = re.compile("|".join(PADROES_ANTIBOT), re.IGNORECASE)

STOPWORDS_TITULO = {
    "the", "a", "an", "and", "or", "but", "in", "on", "at", "to", "for", "of", "with",
    "by", "from", "up", "about", "into", "over", "after", "o", "a", "os", "as", "um",
    "uma", "de", "da", "do", "em", "para", "com", "por", "sobre", "el", "la", "los",
    "las", "en", "por", "para", "con", "del", "al", "der", "die", "das", "und", "im",
    "le", "les", "des", "pour", "dans", "sur", "que", "is", "are", "was", "were"
}

_EMBEDDER_SINGLETON = None


def get_embedder(model_name: str = "BAAI/bge-m3"):
    """Instancia ou reutiliza o modelo de embeddings em padrão singleton."""
    global _EMBEDDER_SINGLETON
    if _EMBEDDER_SINGLETON is None:
        print(f"Carregando {model_name} (1024d)...", flush=True)
        _EMBEDDER_SINGLETON = SentenceTransformer(model_name)
    return _EMBEDDER_SINGLETON


def extrair_lead_limpo(texto: str, termos_descarte_dict: dict, max_chars: int = 1200) -> str:
    """Higieniza o início do texto removendo termos indesejados e chamadas comerciais."""
    if not texto or texto in ("[CONTEUDO_BLOQUEADO]", ""):
        return ""
    todos_descartes = [t.lower() for lista in termos_descarte_dict.values() for t in lista]
    linhas_validas = []
    for linha in texto.split("\n"):
        l = linha.strip()
        if len(l) < 25:
            continue
        if any(termo in l.lower() for termo in todos_descartes):
            continue
        linhas_validas.append(l)
    return " ".join(linhas_validas)[:max_chars].strip()


def classificar_url_terminal(url: str) -> Optional[str]:
    """Identifica URLs de redes fechadas, plataformas de mídia ou homepages."""
    if not url or not isinstance(url, str):
        return None
    try:
        parsed = urllib.parse.urlparse(url.lower())
        netloc = parsed.netloc.replace("www.", "")
        if any(netloc == d or netloc.endswith("." + d) for d in DOMINIOS_MIDIA):
            return "CONTEUDO_MIDIA"
        if any(netloc == d or netloc.endswith("." + d) for d in DOMINIOS_FECHADOS):
            return "PLATAFORMA_FECHADA"
        path = parsed.path.strip("/")
        if not path or path in ["index.html", "index.php", "home", "noticias", "economia", "politica"]:
            if not parsed.query:
                return "REDIRECT_HOMEPAGE"
    except Exception:
        pass
    return None


def validar_integridade_factual(titulo: str, texto: Optional[str]) -> Tuple[bool, str]:
    """Valida densidade textual, bloqueios de infraestrutura e sobreposição léxica de substantivos."""
    if not texto or len(texto.strip()) < TAMANHO_MINIMO_TEXTO:
        return False, "TEXTO_MUITO_CURTO"

    amostra = texto[:2500]
    if REGEX_ANTIBOT.search(amostra):
        return False, "ERRO_SCRAPING_BLOQUEIO_CDN"

    tokens_titulo = [
        t.lower() for t in re.findall(r"\b[a-zA-Z0-9\u00C0-\u00FF]{4,}\b", titulo or "")
        if t.lower() not in STOPWORDS_TITULO
    ]

    if len(tokens_titulo) >= 3:
        texto_lower = texto.lower()
        if not any(token in texto_lower for token in tokens_titulo):
            return False, "SEM_SOBREPOSICAO_TITULO_CORPO"

    return True, "APTO"


def decode_token_offline(token: str) -> Optional[str]:
    """Decodifica URLs base64 do Google News de forma local."""
    try:
        padded = token + "=" * (-len(token) % 4)
        raw_bytes = base64.urlsafe_b64decode(padded)
        matches = re.findall(rb"https?://[a-zA-Z0-9_\-\.\/\?\=\&\%\#\:\@]+", raw_bytes)
        for url_bytes in matches:
            url_str = url_bytes.decode("utf-8", errors="ignore")
            if "google.com" not in url_str and "schema.org" not in url_str and len(url_str) > 15:
                return url_str
    except Exception:
        pass
    return None


def resolve_publisher_url(google_news_url: str) -> str:
    """Decodifica URL do Google News combinando rotina offline e RPC."""
    if not google_news_url or "news.google.com" not in google_news_url:
        return google_news_url

    clean_url = google_news_url.split("?")[0].strip()
    match = re.search(r"/articles/([^/?&]+)", clean_url)
    if match:
        extracted = decode_token_offline(match.group(1))
        if extracted and "google.com" not in extracted:
            return extracted

    try:
        res = googlenewsdecoder.decoderv1(google_news_url, interval=0.1)
        if isinstance(res, dict) and res.get("status"):
            decoded = res.get("decoded_url")
            if decoded and decoded.startswith("http") and "news.google.com" not in decoded:
                return decoded
    except Exception:
        pass

    return google_news_url


def build_rss_query(base_term: str, excluded_terms: list, period: str, preferred_domains: list) -> str:
    """Monta a string de busca para o feed RSS."""
    parts = [base_term]
    if period:
        parts.append(f"when:{period}")
    if preferred_domains:
        sites_query = " OR ".join([f"site:{domain}" for domain in preferred_domains])
        parts.append(f"({sites_query})")
    if excluded_terms:
        parts.extend([f"-{term}" for term in excluded_terms])
    return " ".join(parts)


def fetch_rss_feed(query: str, hl: str, gl: str, timeout: int = 6) -> list:
    """Consulta o RSS do Google News retornando as entradas estruturadas."""
    encoded_query = urllib.parse.quote(query)
    ceid = f"{hl.upper()}:{gl.upper()}"
    url = f"https://news.google.com/rss/search?q={encoded_query}&hl={hl}&gl={gl}&ceid={ceid}"
    headers = {"User-Agent": random.choice(USER_AGENTS)}
    try:
        response = requests.get(url, headers=headers, timeout=timeout)
        if response.status_code != 200:
            return []
        root = ET.fromstring(response.content)
        feed_items = []
        for item in root.findall(".//channel/item"):
            feed_items.append({
                "titulo": (item.find("title").text or "").strip(),
                "link": (item.find("link").text or "").strip(),
                "data_noticia": (item.find("pubDate").text or "").strip(),
                "fonte": (item.find("source").text or "Google News").strip() if item.find("source") is not None else "Google News",
                "snippet": (item.find("description").text or "").strip(),
            })
        return feed_items
    except Exception:
        return []


def scrape_article_text(url: str, timeout: int = 5) -> Tuple[Optional[str], str, str]:
    """Extrai texto da matéria via requisição HTTP rápida com tratamento de bloqueios."""
    real_url = resolve_publisher_url(url)
    if "news.google.com" in real_url:
        return None, "FALHA_DECODIFICACAO_URL", real_url

    cat_term = classificar_url_terminal(real_url)
    if cat_term:
        return None, cat_term, real_url

    headers = {
        "User-Agent": random.choice(USER_AGENTS),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7,es;q=0.6",
    }
    try:
        resp = requests.get(real_url, headers=headers, timeout=(2.5, float(timeout)), allow_redirects=True)
    except requests.exceptions.RequestException as e:
        return None, f"FALHA_CONEXAO_{type(e).__name__}", real_url

    if resp.status_code != 200:
        return None, f"FALHA_HTTP_{resp.status_code}", resp.url

    html_content = resp.text
    if not html_content:
        return None, "HTML_VAZIO", resp.url

    text = trafilatura.extract(html_content, include_comments=False, include_tables=False, output_format="txt")
    if not text or len(text.strip()) < TAMANHO_MINIMO_TEXTO:
        soup = BeautifulSoup(html_content, "html.parser")
        for tag in soup(["script", "style", "nav", "header", "footer", "aside", "form"]):
            tag.decompose()
        paragraphs = [p.get_text().strip() for p in soup.find_all("p") if len(p.get_text().strip()) > 35]
        text = "\n\n".join(paragraphs)

    return (text.strip() if text else None), "SUCESSO", resp.url


def cluster_articles(
    raw_articles: list,
    model_name: str = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2",
    similarity_threshold: float = 0.73,
    regiao_prefix: str = "GLOB",
) -> list:
    """Agrupa matérias semelhantes gerando clusters de notícia com ID regional unívoco."""
    if not raw_articles:
        return []
    embedder = get_embedder(model_name)
    titulos = [a["titulo"] for a in raw_articles]
    embeddings = embedder.encode(titulos, batch_size=64, show_progress_bar=False, convert_to_numpy=True, normalize_embeddings=True)

    clusters = []
    visited = set()
    total = len(raw_articles)
    data_tag = datetime.now(FUSO_BRASILIA).strftime("%Y%m%d")
    # Utiliza o nome completo higienizado da região para eliminar risco de colisão de PK
    shard_tag = re.sub(r"[^\w]", "_", regiao_prefix).upper().strip("_")

    for i in range(total):
        if i in visited:
            continue
        cluster_members = [raw_articles[i]]
        visited.add(i)
        for j in range(i + 1, total):
            if j in visited:
                continue
            cos_sim = float(np.dot(embeddings[i], embeddings[j]))
            if cos_sim >= similarity_threshold:
                cluster_members.append(raw_articles[j])
                visited.add(j)

        primary = cluster_members[0]
        mirrors = [m["link"] for m in cluster_members[1:] if m["link"] != primary["link"]]
        clusters.append({
            "id_cluster": f"CLUS_{data_tag}_{shard_tag}_{len(clusters) + 1:04d}",
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


def process_cluster_with_fallback(cluster: dict, timeout: int = 6) -> dict:
    """
    Estágio 1 (HTTP): Itera exaustivamente pela URL primária e por todas as URLs
    espelho até obter um texto factualmente válido.
    """
    urls_to_try = [cluster["url_primaria"]]
    for esp in cluster.get("urls_espelho", []):
        if esp and esp not in urls_to_try:
            urls_to_try.append(esp)

    historico = []
    espelhos_decodificados = [resolve_publisher_url(e) for e in cluster.get("urls_espelho", [])]
    titulo = cluster.get("titulo", "")
    primeira_url_resolvida = None
    ultimo_motivo = "HTTP_TIMEOUT_OU_BLOQUEIO"

    for link in urls_to_try:
        texto, status_http, final_url = scrape_article_text(link, timeout=timeout)
        if primeira_url_resolvida is None:
            primeira_url_resolvida = final_url

        # 1. Bloqueio ou falha de conexão HTTP
        if status_http != "SUCESSO" or not texto:
            ultimo_motivo = status_http
            historico.append({
                "url_original_rss": link,
                "url_canonica_decodificada": final_url,
                "status": status_http,
                "motivo": status_http,
                "timestamp": datetime.now(FUSO_BRASILIA).strftime("%Y-%m-%d %H:%M:%S"),
            })
            continue

        # 2. Validação Factual Preventiva (Shift-Left)
        apto, motivo = validar_integridade_factual(titulo, texto)
        if not apto:
            ultimo_motivo = motivo
            historico.append({
                "url_original_rss": link,
                "url_canonica_decodificada": final_url,
                "status": f"DESCARTE_FACTUAL_{motivo}",
                "motivo": motivo,
                "timestamp": datetime.now(FUSO_BRASILIA).strftime("%Y-%m-%d %H:%M:%S"),
            })
            continue

        # 3. Sucesso Factual: Interrompe a busca no cluster imediatamente
        historico.append({
            "url_original_rss": link,
            "url_canonica_decodificada": final_url,
            "status": "SUCESSO",
            "motivo": None,
            "timestamp": datetime.now(FUSO_BRASILIA).strftime("%Y-%m-%d %H:%M:%S"),
        })

        return {
            "id_cluster": cluster["id_cluster"],
            "tema": cluster["tema"],
            "termo_origem": cluster["termo_origem"],
            "titulo": titulo,
            "data_noticia": cluster["data_noticia"],
            "idioma": cluster["idioma"],
            "fonte_utilizada": cluster["fonte_principal"],
            "url_utilizada": final_url,
            "url_canonica_resolvida": final_url,
            "urls_espelho_disponiveis": [u for u in espelhos_decodificados if u != final_url],
            "status_extracao": "SUCESSO",
            "texto_completo": texto,
            "motivo_bloqueio": None,
            "necessita_extracao_manual": False,
            "historico_tentativas": historico,
        }

    return {
        "id_cluster": cluster["id_cluster"],
        "tema": cluster["tema"],
        "termo_origem": cluster["termo_origem"],
        "titulo": titulo,
        "data_noticia": cluster["data_noticia"],
        "idioma": cluster["idioma"],
        "fonte_utilizada": cluster["fonte_principal"],
        "url_utilizada": primeira_url_resolvida or cluster["url_primaria"],
        "url_canonica_resolvida": primeira_url_resolvida or cluster["url_primaria"],
        "urls_espelho_disponiveis": espelhos_decodificados,
        "status_extracao": "CONTEUDO_BLOQUEADO",
        "texto_completo": "",
        "motivo_bloqueio": ultimo_motivo,
        "necessita_extracao_manual": True,
        "historico_tentativas": historico,
    }


def gerar_vetores_em_lote(
    processed_results: list,
    termos_descarte_dict: dict,
    model_name: str = "BAAI/bge-m3",
    batch_size: int = 32,
) -> None:
    """Calcula embeddings BGE-M3 com log de progresso em tempo real no console."""
    total_itens = len(processed_results)
    if total_itens == 0:
        return

    embedder = get_embedder(model_name)
    textos_para_vetorizar = []

    for r in processed_results:
        texto = r.get("texto_completo", "")
        lead = (
            extrair_lead_limpo(texto, termos_descarte_dict=termos_descarte_dict, max_chars=1200)
            if r.get("status_extracao") == "SUCESSO"
            else ""
        )
        trecho_final = f"{r['titulo']}. {lead}".strip() if lead else r["titulo"]
        textos_para_vetorizar.append(trecho_final)

    total_lotes = math.ceil(total_itens / batch_size)
    print(f"\nIniciando vetorização de {total_itens} matérias com {model_name}...", flush=True)

    vetores_finais = []
    inicio_vetorizacao = time.time()

    for idx in range(0, total_itens, batch_size):
        lote_atual_num = (idx // batch_size) + 1
        lote_textos = textos_para_vetorizar[idx : idx + batch_size]

        t0 = time.time()
        vetores_lote = embedder.encode(
            lote_textos,
            batch_size=batch_size,
            show_progress_bar=False,
            convert_to_numpy=True,
            normalize_embeddings=True,
        )
        tempo_lote = time.time() - t0
        vetores_finais.extend(vetores_lote.tolist())

        itens_processados = min(idx + batch_size, total_itens)
        pct = (itens_processados / total_itens) * 100
        print(f"  >> [Lote {lote_atual_num:02d}/{total_lotes:02d}] {itens_processados}/{total_itens} ({pct:.1f}%) em {tempo_lote:.2f}s", flush=True)

    for i, r in enumerate(processed_results):
        r["vetor_1024"] = vetores_finais[i]

    tempo_total = time.time() - inicio_vetorizacao
    print(f"Vetorização finalizada com sucesso! Tempo total: {tempo_total:.2f}s\n", flush=True)


async def _navegar_playwright_item(context, item: dict) -> dict:
    """
    Estágio 2 (Playwright Stealth): Percorre todas as candidatas em headless browser.
    Não aborta a busca ao encontrar uma URL terminal; prossegue aos espelhos.
    """
    url_primaria = item.get("url_canonica_resolvida") or item.get("url_utilizada") or ""
    candidatas = [url_primaria] if url_primaria else []
    for esp in item.get("urls_espelho_disponiveis", []):
        if esp not in candidatas and esp.startswith("http"):
            candidatas.append(esp)

    titulo = item.get("titulo", "")
    page = None
    sucesso = False
    ultimo_motivo = "CONTEUDO_CURTO_OU_BLOQUEADO"

    try:
        page = await context.new_page()
        await page.add_init_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

        async def interceptar_recursos(route):
            if route.request.resource_type in ["image", "media", "font", "stylesheet"]:
                await route.abort()
            else:
                await route.continue_()

        await page.route("**/*", interceptar_recursos)

        for url_alvo in candidatas: 
            cat_term = classificar_url_terminal(url_alvo)
            if cat_term:
                ultimo_motivo = cat_term
                continue

            try:
                await page.goto(url_alvo, wait_until="domcontentloaded", timeout=9000)
            except Exception:
                ultimo_motivo = "TIMEOUT_BROWSER"
                continue

            if "consent.google" in page.url or "google.com" in page.url:
                for sel in ["button:has-text('Aceitar tudo')", "button:has-text('Concordo')", "button:has-text('Accept all')"]:
                    try:
                        btn = page.locator(sel).first
                        if await btn.is_visible(timeout=600):
                            await btn.click()
                            break
                    except Exception:
                        pass
                try:
                    await page.wait_for_url(lambda u: "google" not in u, timeout=3000)
                except Exception:
                    pass

            url_real = page.url
            if "google.com" in url_real or "consent.google" in url_real:
                ultimo_motivo = "NAO_REDIRECIONOU_GOOGLE"
                continue

            html_content = await page.content()
            text = trafilatura.extract(html_content, include_comments=False, include_tables=False, output_format="txt")
            if not text or len(text.strip()) < TAMANHO_MINIMO_TEXTO:
                soup = BeautifulSoup(html_content, "html.parser")
                for tag in soup(["script", "style", "nav", "header", "footer", "aside"]):
                    tag.decompose()
                paragraphs = [p.get_text().strip() for p in soup.find_all("p") if len(p.get_text().strip()) > 35]
                text = "\n\n".join(paragraphs)

            apto, motivo = validar_integridade_factual(titulo, text)
            if apto:
                item["texto_completo"] = text.strip()
                item["status_extracao"] = "SUCESSO"
                item["url_utilizada"] = url_real
                item["url_canonica_resolvida"] = url_real
                item["motivo_bloqueio"] = None
                item["necessita_extracao_manual"] = False
                sucesso = True
                break
            else:
                ultimo_motivo = motivo

        if not sucesso:
            item["status_extracao"] = "CONTEUDO_BLOQUEADO"
            item["texto_completo"] = ""
            item["motivo_bloqueio"] = ultimo_motivo

    except Exception as e:
        item["status_extracao"] = "CONTEUDO_BLOQUEADO"
        item["motivo_bloqueio"] = f"ERRO_PLAYWRIGHT: {type(e).__name__}"
    finally:
        if page:
            try:
                await page.close()
            except Exception:
                pass
    return item


async def processar_bloqueados_playwright(itens_bloqueados: list) -> list:
    """Executa pool assíncrono com semáforo restrito de 4 abas para resgate de matérias bloqueadas."""
    if not itens_bloqueados:
        return []
    async with async_playwright() as p:
        browser = await p.chromium.launch(
            headless=True,
            args=["--no-sandbox", "--disable-dev-shm-usage", "--disable-blink-features=AutomationControlled", "--disable-gpu"],
        )
        context = await browser.new_context(user_agent=random.choice(USER_AGENTS), viewport={"width": 1280, "height": 800})
        sem = asyncio.Semaphore(4)

        async def _safe_run(item):
            async with sem:
                try:
                    return await asyncio.wait_for(_navegar_playwright_item(context, item), timeout=18.0)
                except asyncio.TimeoutError:
                    item["status_extracao"] = "CONTEUDO_BLOQUEADO"
                    item["motivo_bloqueio"] = "DEADLOCK_TIMEOUT"
                    return item

        resultados = await asyncio.gather(*[_safe_run(item) for item in itens_bloqueados])
        await context.close()
        await browser.close()
        return resultados


def executar_fallback_playwright(itens_bloqueados: list) -> list:
    """Interface síncrona para acionamento do pool assíncrono do Playwright."""
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        return loop.run_until_complete(processar_bloqueados_playwright(itens_bloqueados))
    finally:
        loop.close()
