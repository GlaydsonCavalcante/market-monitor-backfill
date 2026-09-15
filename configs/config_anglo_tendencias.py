"""Configuração de monitoramento de Megatendências e Cenários de Futuro para países de língua inglesa (EUA, Reino Unido, Canadá e Austrália)."""

REGIAO_NOME = "ANGLO_TENDENCIAS"

MONITORAMENTOS = {
    "Reinvencao do Consumo": {
        "en": [
            '("reinvention of consumption" OR "future of consumption" OR "consumer behavior") ("customer journey" OR "non-linear journey" OR "continuous journey")',
            '("agentic commerce" OR "shopping agents" OR "AI shopping" OR "autonomous commerce" OR "agentic payments")',
            '("conversational AI" OR "conversational commerce" OR "voice commerce" OR "anticipatory consumption" OR "predictive commerce")',
            '("hyperpersonalization" OR "real-time recommendation" OR "context-aware commerce" OR "next best offer")',
            '("omnichannel" OR phygital OR "unified commerce" OR "embedded commerce" OR "frictionless commerce" OR "invisible payments")',
            '("social commerce" OR "live commerce" OR "live shopping" OR "creator commerce" OR "shoppable content" OR "TikTok Shop" OR "WhatsApp commerce")',
            '("immersive experiences" OR "augmented reality retail" OR "virtual try-on" OR "consumer autonomy")',
            '("consumer privacy" OR "data sovereignty" OR "digital identity" OR "digital fatigue" OR "personalization fatigue")',
            '("dark patterns" OR "algorithmic manipulation" OR "search for analog" OR "authentic experiences" OR "humanized customer service")',
        ]
    },
    "Reconfiguracao Demografica": {
        "en": [
            '("demographic reconfiguration" OR "demographic transition" OR "demographic shift" OR "population aging" OR "aging population" OR "aged society" OR "super-aged society" OR longevity OR "demographic winter" OR "population decline" OR "demographic dividend" OR "dependency ratio" OR "age structure" OR "population pyramid" OR "demographic dynamics")',
            '("falling birth rate" OR "declining birth rates" OR "fertility rate collapse" OR "low fertility" OR "demographic crisis" OR "fewer children" OR "delayed childbearing" OR "smaller families" OR childfree OR infertility OR "assisted reproduction" OR "pro-natalist policies")',
            '("longevity economy" OR "active aging" OR "healthy aging" OR "silver economy" OR "silver market" OR "generation silver" OR "60+" OR "80+" OR centenarians OR supercentenarians OR "life expectancy" OR "life extension" OR "Aging tech" OR "AgeTech" OR "longevity medicine" OR "cellular rejuvenation" OR geroscience)',
            '("labor shortage" OR "worker shortage" OR "aging workforce" OR "workforce aging" OR "reskilling" OR "lifelong learning" OR "non-linear careers" OR "second careers" OR "working post-retirement" OR "delayed retirement" OR "multigenerational workforce" OR "care economy")',
            '("pension reform" OR "pension sustainability" OR "pension crisis" OR "retirement systems" OR "intergenerational pact" OR "social protection" OR "economic dependency" OR "private pension" OR "retirement planning" OR "longevity income" OR "wealth decumulation")',
            '("long-term care" OR "care economy" OR caregivers OR "home care" OR "digital health" OR "remote patient monitoring" OR telemedicine OR "preventive healthcare" OR "healthy aging" OR "chronic diseases" OR dementia OR Alzheimer)',
            '("single-person households" OR "living alone" OR "new family arrangements" OR "sandwich generation" OR loneliness OR "social isolation" OR "delayed marriage" OR "declining marriage rates")',
            '("international migration" OR "migratory flows" OR "skilled immigration" OR "climate refugees" OR "human mobility" OR "labor migration" OR urbanization OR "Africa population growth" OR "Sub-Saharan Africa dividend")',
            '("age-friendly cities" OR "senior living" OR "intergenerational communities" OR "accessible housing" OR "urban accessibility" OR "inclusive mobility" OR "urban aging")',
            '("financial planning for longevity" OR "wealth transfer" OR "estate planning" OR inheritance OR "income protection" OR "care insurance" OR "longevity insurance" OR "private pension funds" OR "retirement investments" OR "multigenerational wealth management" OR "senior market")',
            '("who will fund longevity" OR "pension system collapse" OR "global worker shortage" OR "100-year life" OR "working until 70" OR "shrinking workforce" OR "war for talent" OR "automation labor shortage" OR "migration as demographic solution" OR "intergenerational pact sustainability")',
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
