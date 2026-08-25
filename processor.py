"""Módulo de processamento RSS, desduplicação e vetorização em lote com BAAI/bge-m3."""

import base64
from datetime import datetime
import random
import re
import urllib.parse
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
from config import MODELO_EMBEDDING_1024, USER_AGENTS
from googlenewsdecoder import new_decoderv1
import numpy as np
import requests
from sentence_transformers import SentenceTransformer
import trafilatura

_EMBEDDER_SINGLETON = None


def get_embedder():
    """Carrega o modelo BGE-M3 em memória (Singleton)."""
    global _EMBEDDER_SINGLETON
    if _EMBEDDER_SINGLETON is None:
        print(f"Carregando {MODELO_EMBEDDING_1024} (1024d)...", flush=True)
        _EMBEDDER_SINGLETON = SentenceTransformer(MODELO_EMBEDDING_1024)
    return _EMBEDDER_SINGLETON


def extrair_lead_limpo(texto: str, max_chars: int = 1200) -> str:
    """Higieniza o texto raspado removendo anúncios e chamadas de navegação."""
    if not texto or texto == "[CONTEUDO_BLOQUEADO]":
        return ""

    termos_descarte = [
        "leia mais",
        "inscreva-se",
        "compartilhe",
        "publicidade",
        "todos os direitos reservados",
        "foto:",
        "crédito:",
        "veja também",
        "redação",
        "clique aqui",
        "newsletter",
    ]

    linhas_validas = []
    for linha in texto.split("\n"):
        l = linha.strip()
        if len(l) < 25:
            continue
        if any(termo in l.lower() for termo in termos_descarte):
            continue
        linhas_validas.append(l)

    texto_higienizado = " ".join(linhas_validas)
    return texto_higienizado[:max_chars].strip()


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


def fetch_rss_feed(query: str, hl: str, gl: str) -> list:
    encoded_query = urllib.parse.quote(query)
    ceid = f"{hl.upper()}:{gl.upper()}"
    url = f"https://news.google.com/rss/search?q={encoded_query}&hl={hl}&gl={gl}&ceid={ceid}"
    headers = {"User-Agent": random.choice(USER_AGENTS)}
    try:
        response = requests.get(url, headers=headers, timeout=8)
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
    if not google_news_url or "news.google.com" not in google_news_url:
        return google_news_url
    clean_url = google_news_url.split("?")[0].strip()
    match = re.search(r"/articles/([^/?&]+)", clean_url)
    token = match.group(1) if match else None
    if token:
        extracted = decode_token_offline(token)
        if extracted:
            return extracted
    try:
        res = new_decoderv1(google_news_url)
        if res.get("status") and res.get("decoded_url"):
            decoded = res["decoded_url"]
            if decoded.startswith("http") and "news.google.com" not in decoded:
                return decoded
    except Exception:
        pass
    return google_news_url


def scrape_article_text(url: str) -> tuple:
    real_url = resolve_publisher_url(url)
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
        resp = requests.get(real_url, headers=headers, timeout=7)
        if resp.status_code != 200:
            return None, f"FALHA_HTTP_{resp.status_code}", real_url
        html_content = resp.text
        text = trafilatura.extract(
            html_content,
            include_comments=False,
            include_tables=False,
            include_links=False,
            output_format="txt",
        )
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


def cluster_articles(raw_articles: list, similarity_threshold: float = 0.73) -> list:
    """Agrupa matérias redundantes da coleta utilizando BGE-M3."""
    if not raw_articles:
        return []
    embedder = get_embedder()
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


def process_cluster_with_fallback(cluster: dict) -> dict:
    """Processa a extração de texto (sem vetorização unitária para não travar a CPU)."""
    urls_to_try = [cluster["url_primaria"]] + cluster["urls_espelho"]
    historico = []
    espelhos_decodificados = [
        resolve_publisher_url(e) for e in cluster["urls_espelho"]
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


def gerar_vetores_em_lote(processed_results: list) -> None:
    """Calcula os vetores 1024d de todos os clusters de uma só vez em matriz vetorial paralela."""
    embedder = get_embedder()
    textos_para_vetorizar = []

    for r in processed_results:
        texto = r.get("texto_completo", "")
        lead = (
            extrair_lead_limpo(texto, max_chars=1200)
            if r.get("status_extracao") == "SUCESSO"
            else ""
        )
        trecho_final = f"{r['titulo']}. {lead}".strip() if lead else r["titulo"]
        textos_para_vetorizar.append(trecho_final)

    print(
        f"Vetorizando {len(textos_para_vetorizar)} itens em lote com BGE-M3...",
        flush=True,
    )
    vetores = embedder.encode(
        textos_para_vetorizar,
        batch_size=32,
        show_progress_bar=False,
        convert_to_numpy=True,
        normalize_embeddings=True,
    )

    for i, r in enumerate(processed_results):
        r["vetor_1024"] = vetores[i].tolist()
    print("Vetorização em lote concluída com sucesso.", flush=True)
