"""Configuração para Estados Unidos, Reino Unido, Austrália e Canadá."""

REGIAO_NOME = "ANGLO_GLOBAL"

MONITORAMENTOS = {
    "Comércio Agentico": {
        "en": [
            '"artificial intelligence" banks',
            '"agentic commerce"',
            '"autonomous AI" banking',
            '"agentic AI" finance',
            '"hyper-personalized journeys"',
            '"social commerce" banking',
            '"autonomous agents" payments',
        ]
    },
    "Longevidade": {
        "en": [
            '"silver economy" banking',
            '"aging population" economy',
            '"longevity economy" finance',
            '"demographic shift" banking',
            '"digital health" "personalized medicine"',
            '"active longevity" finance',
            '"advanced therapies" bioengineering',
        ]
    },
}

MERCADOS_ALVO = [
    {"gl": "US", "hl": "en-US", "lang": "en"},
    {"gl": "GB", "hl": "en-GB", "lang": "en"},
    {"gl": "AU", "hl": "en-AU", "lang": "en"},
    {"gl": "CA", "hl": "en-CA", "lang": "en"},
]

TERMOS_EXCLUIDOS = {
    "en": [
        "sports",
        "football",
        "soccer",
        "celebrity",
        "horoscope",
        "recipe",
        "lottery",
        "gossip",
        "sweepstakes",
    ]
}

TERMOS_DESCARTE_TEXTO = {
    "en": [
        "read more",
        "subscribe",
        "share",
        "advertisement",
        "all rights reserved",
        "photo:",
        "credit:",
        "see also",
        "editor",
        "click here",
        "newsletter",
        "sponsored",
    ]
}

PERIODO_BUSCA = "1d"
DOMINIOS_PREFERENCIAIS = []
MODELO_EMBEDDING_1024 = "BAAI/bge-m3"
SIMILARIDADE_REDUNDANCIA = 0.73
MAX_WORKERS_PARALELO = 8
TIMEOUT_REQUISICAO = 6
