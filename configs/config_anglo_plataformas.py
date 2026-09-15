"""Configuração de monitoramento de Grandes Plataformas e Ecossistemas para países de língua inglesa (EUA, Reino Unido, Canadá e Austrália)."""

REGIAO_NOME = "ANGLO_PLATAFORMAS"

MONITORAMENTOS = {
    "Mercado Livre": {
        "en": [
            '("Mercado Libre" OR "MercadoLibre" OR "MELI" OR "Mercado Envios" OR "Mercado Ads" OR "Mercado Shops" OR "Mercado Play" OR "Meli+") (GMV OR "gross merchandise volume" OR "e-commerce market share" OR "third-party sellers" OR "retail media" OR "live commerce")',
            '("Mercado Libre" OR "MercadoLibre" OR "Mercado Envios") (fulfillment OR "distribution centers" OR "last mile logistics" OR "same-day delivery" OR "next-day delivery" OR "dedicated logistics network")',
            '("Mercado Libre" OR "MercadoLibre" OR "Mercado Ads") ("retail media network" OR "ad monetization" OR "traffic monetization" OR "digital advertising")',
            '("Mercado Libre" OR "MercadoLibre" OR "Mercado Creditos" OR "Mercado Créditos") ("merchant credit" OR "SME working capital" OR "embedded lending" OR "seller financing" OR NPL)',
            '("Mercado Libre" OR "MercadoLibre" OR "Meli+") ("loyalty program" OR membership OR subscription OR "subscriber benefits")',
            '("Mercado Libre" OR "MercadoLibre" OR "MELI") ("artificial intelligence" OR "conversational search" OR "AI shopping agents" OR "logistics automation" OR hyperpersonalization)',
            '("Mercado Libre" OR "MercadoLibre" OR "MELI") ("new verticals" OR M&A OR acquisitions OR "strategic partnerships" OR "Latin America expansion")',
            '("Mercado Libre" OR "MercadoLibre" OR "MELI") ("marketplace regulation" OR "Amazon competition" OR "cross-border tax" OR fraud OR "counterfeit products")',
        ]
    },
    "Amazon": {
        "en": [
            '("Amazon" OR "Amazon Marketplace" OR "Amazon.com") (marketplace OR "third-party sellers" OR "marketplace sellers" OR FBA OR "Fulfillment by Amazon")',
            '("Amazon") ("fulfillment centers" OR "logistics robotics" OR "same-day delivery" OR "ultra-fast delivery" OR "last mile" OR "drone delivery" OR "warehouse automation")',
            '("AWS" OR "Amazon Web Services" OR ("Amazon" AND "cloud computing")) ("cloud infrastructure" OR "generative AI" OR "data centers" OR "data sovereignty")',
            '("Amazon" OR "AWS") ("Amazon Bedrock" OR "AI agents" OR "smart assistants" OR "Alexa+" OR Alexa OR "generative AI models")',
            '("Amazon Ads" OR ("Amazon" AND ("retail media" OR "retail media network" OR "ad revenue")))',
            '("Amazon Prime" OR ("Amazon" AND (membership OR "Prime ecosystem" OR "streaming video" OR loyalty)))',
            '("Amazon Pharmacy" OR ("Amazon" AND (telehealth OR telemedicine OR "digital health" OR "health tech")))',
            '("Amazon" OR "AWS") ("new verticals" OR fintech OR "embedded finance" OR M&A OR acquisitions)',
            '("Amazon" OR "AWS") (antitrust OR "digital market regulation" OR "FTC lawsuit" OR "data privacy" OR taxation OR "monopoly investigation")',
        ]
    },
    "iFood": {
        "en": [
            '("iFood" OR "iFood Card") (delivery OR "quick commerce" OR "instant delivery" OR "last mile delivery" OR "urban logistics")',
            '("iFood" OR "iFood Mercado") ("dark stores" OR "digital convenience" OR "grocery delivery" OR "on-demand retail")',
            '("iFood Pago" OR "Conta Digital iFood" OR ("iFood" AND ("restaurant credit" OR "merchant financing" OR "receivables advance" OR "embedded finance" OR "restaurant banking")))',
            '("iFood") ("restaurant digitalization" OR "restaurant management" OR "restaurant ERP" OR "merchant ecosystem")',
            '("iFood Ads" OR ("iFood" AND ("retail media" OR "audience monetization" OR "delivery ads")))',
            '("iFood Beneficios" OR "iFood Benefícios" OR ("iFood" AND ("meal vouchers" OR "food vouchers" OR "flexible corporate benefits")))',
            '("iFood") ("logistics AI" OR "demand forecasting" OR "smart routing algorithms" OR "conversational AI")',
            '("iFood") ("gig economy" OR "platform economy" OR "delivery riders" OR "labor relations" OR "app-based workers")',
            '("iFood") ("new categories" OR fintech OR healthcare OR "super app")',
            '("iFood") ("gig worker regulation" OR "labor compliance" OR "Rappi competition" OR "99Food competition" OR "food safety")',
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
        "coupon", "coupons", "promo code", "discount", "giveaway", "sweepstakes",
        "how to open an account", "step by step tutorial", "daily stock movement",
        "daily exchange rate", "market close summary", "customer complaints",
        "best account ranking", "sponsored review", "sports", "football", "soccer",
        "celebrity", "horoscope", "recipe",
    ]
}

TERMOS_DESCARTE_TEXTO = {
    "en": [
        "read more", "subscribe", "share", "advertisement", "all rights reserved",
        "photo:", "credit:", "see also", "editor", "click here", "newsletter",
        "sponsored", "how to open an account", "step by step guide", "terms and conditions apply",
    ]
}

PERIODO_BUSCA = "1d"
DOMINIOS_PREFERENCIAIS = []
MODELO_EMBEDDING_1024 = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
SIMILARIDADE_REDUNDANCIA = 0.73
MAX_WORKERS_PARALELO = 8
TIMEOUT_REQUISICAO = 6
