"""Configuração para Estados Unidos, Reino Unido, Austrália e Canadá."""

REGIAO_NOME = "ANGLO_GLOBAL"

MONITORAMENTOS = {
    "Reinvencao do Consumo": {
        "en": [
            '("future of consumption" OR "consumer behavior" OR "customer journey") ("unified commerce" OR omnichannel OR phygital)',
            '("agentic commerce" OR "shopping agents" OR "AI shopping" OR "autonomous commerce" OR "agentic payments")',
            '("conversational AI" OR "conversational commerce" OR "voice commerce" OR "predictive commerce" OR hyperpersonalization)',
            '("frictionless commerce" OR "invisible payments" OR "embedded commerce" OR "real-time recommendation")',
            '("social commerce" OR "live shopping" OR "creator commerce" OR "TikTok Shop" OR "WhatsApp commerce")',
            '("augmented reality" OR "virtual try-on" OR "immersive experiences" OR "consumer autonomy")',
            '("data sovereignty" OR "digital identity" OR "digital fatigue" OR "dark patterns" OR "algorithmic manipulation")',
            '("authentic experiences" OR "human-centric customer service" OR "search for analog")',
        ]
    },
    "Nubank": {
        "en": [
            '("Nubank" OR "Nu Holdings" OR "Nu México" OR "Nu Colombia") (earnings OR ROE OR ARPAC OR "credit portfolio" OR NPL)',
            '("Nubank" OR "Nu Holdings") ("AI credit models" OR NuFormer OR "artificial intelligence" OR hyperpersonalization)',
            '("Nubank" OR "Nu Holdings") (Ultravioleta OR "mass affluent" OR "Nu Business" OR NuCel OR marketplace)',
            '("Nubank" OR "Nu Holdings") ("banking license" OR "global account" OR "Wise partnership" OR "US expansion")',
            '("Nubank" OR "Nu Holdings") (acquisitions OR fraud OR privacy OR security)',
        ]
    },
    "PicPay": {
        "en": [
            '("PicPay" OR "PicPay Bank") (ChatGPT OR "conversational banking" OR "conversational AI" OR "Open Finance")',
            '("PicPay" OR "PicPay Bank") ("digital wallet" OR Pix OR "payroll loans" OR "merchant acquiring" OR Tap)',
            '("PicPay" OR "PicPay Bank") (IPO OR Nasdaq OR earnings OR profitability OR expansion OR fraud)',
        ]
    },
    "Wise": {
        "en": [
            '("Wise" OR "TransferWise" OR "Wise Platform" OR "Wise Business") ("cross-border payments" OR "international remittances")',
            '("Wise" OR "Wise Platform") ("Banking as a Service" OR "multi-currency account" OR "direct integration" OR FX)',
            '("Wise" OR "Wise Platform") (partnerships OR "enterprise payments" OR "fee transparency" OR "speed of transfers")',
            '("Wise" OR "TransferWise") ("banking licenses" OR expansion OR fraud OR compliance OR AML)',
        ]
    },
    "Nomad": {
        "en": [
            '("Nomad Global" OR "Nomad Fintech" OR "Nomad Wealth") ("global account" OR FX OR "cross-border" OR fintech)',
            '("Nomad Global" OR "Nomad Fintech") ("Nomad Explorer" OR "Nomad Pass" OR "Nomad Lounge" OR "eSIM" OR travel)',
            '("Nomad Global" OR "Nomad Wealth") (investments OR "US stocks" OR ETFs OR REITs OR "travel planning AI")',
        ]
    },
    "Revolut": {
        "en": [
            '("Revolut" OR "Revolut Bank" OR "Revolut Ultra" OR "Revolut Business" OR "Revolut Pay") (expansion OR "Latin America" OR Brazil)',
            '("Revolut" OR "Revolut Ultra") (RevPoints OR "interest accounts" OR crypto OR EURR OR "multi-currency account")',
            '("Revolut" OR "Revolut Research") ("foundation models" OR PRAGMA OR "artificial intelligence" OR "banking license")',
            '("Revolut" OR "Revolut Bank") (compliance OR "regulatory restrictions" OR fraud OR "financial crime prevention")',
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
        "coupon",
        "coupons",
        "promo code",
        "discount",
        "how to open an account",
        "step by step tutorial",
        "daily stock movement",
        "daily exchange rate",
        "customer complaints",
        "best account ranking",
        "sports",
        "football",
        "horoscope",
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
        "how to open an account",
    ]
}

PERIODO_BUSCA = "1d"
DOMINIOS_PREFERENCIAIS = []
MODELO_EMBEDDING_1024 = "BAAI/bge-m3"
SIMILARIDADE_REDUNDANCIA = 0.73
MAX_WORKERS_PARALELO = 8
TIMEOUT_REQUISICAO = 6
