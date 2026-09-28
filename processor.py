"""Módulo de processamento RSS, desduplicação e vetorização em lote com BAAI/bge-m3."""

import base64
from datetime import datetime
import random
import re
import urllib.parse
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
import googlenewsdecoder
import numpy as np
import requests
from sentence_transformers import SentenceTransformer
import trafilatura
import math
import time
import asyncio
from playwright.async_api import async_playwright

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

_EMBEDDER_SINGLETON = None


def get_embedder(model_name: str = "BAAI/bge-m3"):
  global _EMBEDDER_SINGLETON
  if _EMBEDDER_SINGLETON is None:
    print(f"Carregando {model_name} (1024d)...", flush=True)
    _EMBEDDER_SINGLETON = SentenceTransformer(model_name)
  return _EMBEDDER_SINGLETON


def extrair_lead_limpo(
    texto: str, termos_descarte_dict: dict, max_chars: int = 1200
) -> str:
  if not texto or texto == "[CONTEUDO_BLOQUEADO]":
    return ""
  todos_descartes = [
      t.lower() for lista in termos_descarte_dict.values() for t in lista
  ]
  linhas_validas = []
  for linha in texto.split("\n"):
    l = linha.strip()
    if len(l) < 25:
      continue
    if any(termo in l.lower() for termo in todos_descartes):
      continue
    linhas_validas.append(l)
  return " ".join(linhas_validas)[:max_chars].strip()


def build_rss_query(
    base_term: str,
    excluded_terms: list,
    period: str,
    preferred_domains: list,
) -> str:
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


def fetch_rss_feed(
    query: str, hl: str, gl: str, timeout: int = 6
) -> list:
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
      title = item.find("title").text if item.find("title") is not None else ""
      link = item.find("link").text if item.find("link") is not None else ""
      pub_date = (
          item.find("pubDate").text if item.find("pubDate") is not None else ""
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


def decode_token_offline(token: str) -> str:
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
    """Decodifica URLs do Google News combinando método offline e RPC atualizado."""
    if not google_news_url or "news.google.com" not in google_news_url:
        return google_news_url

    # 1. Tentativa offline via regex e base64
    clean_url = google_news_url.split("?")[0].strip()
    match = re.search(r"/articles/([^/?&]+)", clean_url)
    if match:
        extracted = decode_token_offline(match.group(1))
        if extracted and "google.com" not in extracted:
            return extracted

    # 2. Resolução via biblioteca googlenewsdecoder atualizada
    try:
        res = googlenewsdecoder.decoderv1(google_news_url, interval=0.1)
        if isinstance(res, dict) and res.get("status"):
            decoded = res.get("decoded_url")
            if decoded and decoded.startswith("http") and "news.google.com" not in decoded:
                return decoded
    except Exception as exc:
        print(f"[AVISO] Falha ao decodificar via RPC: {exc}", flush=True)

    return google_news_url


PADROES_ANTIBOT = [
    r"unsanctioned scraping by bots",
    r"attention required!? \| cloudflare",
    r"please verify you are a human",
    r"access denied",
    r"verifique se você é humano",
    r"ative o javascript",
    r"ddos protection by cloudflare",
]
REGEX_ANTIBOT = re.compile("|".join(PADROES_ANTIBOT), re.IGNORECASE)

def scrape_article_text(url: str, timeout: int = 5) -> tuple:
    """Extrai conteúdo textual da matéria via HTTP rápido com verificação anti-bot."""
    real_url = resolve_publisher_url(url)
    if "news.google.com" in real_url:
        return None, "FALHA_DECODIFICACAO_URL", real_url

    headers = {
        "User-Agent": random.choice(USER_AGENTS),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7,es;q=0.6",
    }
    
    # Requisição direta sem mascarar falhas de rede críticas
    resp = requests.get(real_url, headers=headers, timeout=(3.0, float(timeout)), allow_redirects=True)
    if resp.status_code != 200:
        return None, f"FALHA_HTTP_{resp.status_code}", resp.url

    html_content = resp.text
    if not html_content:
        return None, "HTML_VAZIO", resp.url

    # Validação anti-bot imediata
    if REGEX_ANTIBOT.search(html_content[:5000]):
        return None, "BLOQUEIO_ANTIBOT", resp.url

    # Extração primária via Trafilatura
    text = trafilatura.extract(
        html_content,
        include_comments=False,
        include_tables=False,
        include_links=False,
        output_format="txt",
    )

    # Extração secundária via BeautifulSoup caso o Trafilatura não atinja o tamanho mínimo
    if not text or len(text.strip()) < 150:
        soup = BeautifulSoup(html_content, "html.parser")
        for tag in soup(["script", "style", "nav", "header", "footer", "aside", "form"]):
            tag.decompose()
        paragraphs = [p.get_text().strip() for p in soup.find_all("p") if len(p.get_text().strip()) > 35]
        text = "\n\n".join(paragraphs)

    if text and len(text.strip()) >= 150 and not REGEX_ANTIBOT.search(text):
        return text.strip(), "SUCESSO", resp.url

    return None, "CONTEUDO_INSUFICIENTE", resp.url

def cluster_articles(
    raw_articles: list,
    model_name: str = "BAAI/bge-m3",
    similarity_threshold: float = 0.73,
) -> list:
  if not raw_articles:
    return []
  embedder = get_embedder(model_name)
  titulos = [a["titulo"] for a in raw_articles]
  embeddings = embedder.encode(
      titulos,
      batch_size=64,
      show_progress_bar=False,
      convert_to_numpy=True,
      normalize_embeddings=True,
  )

  clusters = []
  visited = set()
  total = len(raw_articles)

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
    mirrors = [
        m["link"] for m in cluster_members[1:3] if m["link"] != primary["link"]
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


def process_cluster_with_fallback(
    cluster: dict, timeout: int = 6
) -> dict:
  urls_to_try = [cluster["url_primaria"]] + cluster["urls_espelho"]
  historico = []
  espelhos_decodificados = [
      resolve_publisher_url(e) for e in cluster["urls_espelho"]
  ]
  primeira_url_decodificada = None

  for link in urls_to_try:
    texto, status, final_url = scrape_article_text(link, timeout=timeout)
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
        extrair_lead_limpo(
            texto, termos_descarte_dict=termos_descarte_dict, max_chars=1200
        )
        if r.get("status_extracao") == "SUCESSO"
        else ""
    )
    trecho_final = f"{r['titulo']}. {lead}".strip() if lead else r["titulo"]
    textos_para_vetorizar.append(trecho_final)

  total_lotes = math.ceil(total_itens / batch_size)
  print(
      f"\nIniciando vetorização de {total_itens} matérias com {model_name}...",
      flush=True,
  )
  print(
      f"Configuração: {total_lotes} lotes de até {batch_size} itens.",
      flush=True,
  )

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
    print(
        f"  >> [Lote {lote_atual_num:02d}/{total_lotes:02d}]"
        f" {itens_processados}/{total_itens} ({pct:.1f}%) vetorizados em"
        f" {tempo_lote:.2f}s",
        flush=True,
    )

  for i, r in enumerate(processed_results):
    r["vetor_1024"] = vetores_finais[i]

  tempo_total = time.time() - inicio_vetorizacao
  print(
      f"Vetorização finalizada com sucesso! Tempo total: {tempo_total:.2f}s\n",
      flush=True,
  )

async def _navegar_playwright_item(context, item: dict) -> dict:
    """Abre a URL (mesmo do Google News) no Chromium, resolve redirecionamentos e extrai o texto."""
    url_alvo = item.get("url_utilizada") or item.get("url_primaria") or ""
    page = None
    try:
        page = await context.new_page()
        await page.add_init_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        # Aborta imagens e fontes para economizar CPU e tempo
        await page.route(
            "**/*",
            lambda r: r.abort() if r.request.resource_type in ["image", "media", "font", "stylesheet"] else r.continue_()
        )
        await page.goto(url_alvo, wait_until="domcontentloaded", timeout=6000)

        # Transpõe muralhas de consentimento do Google
        if "consent.google" in page.url or "google.com" in page.url:
            for sel in ["button:has-text('Aceitar tudo')", "button:has-text('Concordo')", "button:has-text('Accept all')"]:
                try:
                    btn = page.locator(sel).first
                    if await btn.is_visible(timeout=800):
                        await btn.click()
                        break
                except Exception:
                    pass
            try:
                await page.wait_for_url(lambda u: "google" not in u, timeout=4000)
            except Exception:
                pass

        html_content = await page.content()
        url_real = page.url

        # Extração de texto do DOM renderizado
        text = trafilatura.extract(html_content, include_comments=False, include_tables=False, output_format="txt")
        if not text or len(text.strip()) < 150:
            soup = BeautifulSoup(html_content, "html.parser")
            for tag in soup(["script", "style", "nav", "header", "footer", "aside"]):
                tag.decompose()
            paragrafos = [p.get_text().strip() for p in soup.find_all("p") if len(p.get_text().strip()) > 35]
            text = "\n\n".join(paragrafos)

        if text and len(text.strip()) >= 150 and not REGEX_ANTIBOT.search(text):
            item["texto_completo"] = text.strip()
            item["status_extracao"] = "SUCESSO"
            item["url_utilizada"] = url_real
            item["motivo_bloqueio"] = None
            item["necessita_extracao_manual"] = False
    except Exception as e:
        item["motivo_bloqueio"] = f"TIMEOUT_PLAYWRIGHT: {type(e).__name__}"
    finally:
        if page:
            await page.close()
    return item


async def processar_bloqueados_playwright(itens_bloqueados: list) -> list:
    """Executa o pool concorrente do Playwright com semáforo restrito para os itens pendentes."""
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
                    return await asyncio.wait_for(_navegar_playwright_item(context, item), timeout=10.0)
                except asyncio.TimeoutError:
                    item["motivo_bloqueio"] = "DEADLOCK_TIMEOUT"
                    return item

        resultados = await asyncio.gather(*[_safe_run(item) for item in itens_bloqueados])
        await context.close()
        await browser.close()
        return resultados


def executar_fallback_playwright(itens_bloqueados: list) -> list:
    """Interface síncrona para chamar o pool assíncrono do Playwright."""
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        return loop.run_until_complete(processar_bloqueados_playwright(itens_bloqueados))
    finally:
        loop.close()
