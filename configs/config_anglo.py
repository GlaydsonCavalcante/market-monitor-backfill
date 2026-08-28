"""Configuração para Estados Unidos, Reino Unido, Austrália e Canadá."""

REGIAO_NOME = "ANGLO_GLOBAL"

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
    "Nubank": {
        "en": [
            '("Nubank" OR "Nu Holdings" OR "Nu México" OR "Nu Colombia" OR "Nubank N.A.") (earnings OR profit OR ROE OR efficiency OR ARPAC OR "active customers")',
            '("Nubank" OR "Nu Holdings") (principality OR engagement OR "credit portfolio" OR NPL OR delinquency)',
            '("Nubank" OR "Nu Holdings") ("AI credit models" OR "dynamic credit limit" OR "credit pricing" OR NuFormer OR "artificial intelligence")',
            '("Nubank" OR "Nu Holdings") (Croma OR Ultravioleta OR "mass affluent" OR "high income" OR "hyper-personalized experience")',
            '("Nubank" OR "Nu Holdings") ("Nu Business" OR "small businesses" OR NuCel OR "Nubank Shopping" OR marketplace OR investments OR insurance)',
            '("Nubank" OR "Nu Holdings") ("global account" OR "Wise partnership" OR "Open Finance" OR "banking license")',
            '("Nu México" OR "Nu Colombia" OR ("Nubank" AND (Mexico OR Colombia OR "United States")))',
            '("Nubank" OR "Nu Holdings") (acquisitions OR partnerships OR fraud OR complaints OR privacy OR security)',
        ]
    },
    "PicPay": {
        "en": [
            '("PicPay" OR "PicPay Bank" OR "PicPay Card") (ChatGPT OR "PicPay integration" OR "conversational banking" OR "conversational AI")',
            '("PicPay" OR "PicPay Bank") ("Open Finance" OR "financial aggregator" OR "digital wallet" OR Pix OR "payroll loans")',
            '("PicPay" OR "PicPay Bank") ("guaranteed limit" OR "piggy banks" OR investments OR insurance OR "merchant acquiring" OR "PicPay Tap")',
            '("PicPay Empresas" OR ("PicPay" AND ("payment link" OR receivables OR "working capital" OR "business marketplace")))',
            '("PicPay" OR "PicPay Bank") (IPO OR Nasdaq OR earnings OR profit OR delinquency OR travel OR food OR fraud OR privacy OR security)',
        ]
    },
    "Wise": {
        "en": [
            '("Wise" OR "TransferWise" OR "Wise Platform" OR "Wise Business" OR "Wise Account") ("international remittances" OR "cross-border payments")',
            '("Wise" OR "Wise Platform") ("international Pix" OR "global payment infrastructure" OR "direct connection" OR SPB OR SPI)',
            '("Wise" OR "Wise Platform") ("Banking as a Service" OR BaaS OR "bank partnerships" OR "multi-currency account")',
            '("Wise" OR "TransferWise") ("commercial exchange rate" OR "mid-market rate" OR "fee transparency" OR "transfer speed")',
            '("Wise Business" OR "Wise Empresas" OR ("Wise" AND ("supplier payments" OR freelancers OR "corporate cross-border")))',
            '("Wise" OR "TransferWise") ("Interest feature" OR licenses OR "geographical expansion" OR fraud OR compliance OR "anti-money laundering" OR AML)',
        ]
    },
    "Nomad": {
        "en": [
            '("Nomad Global" OR "Nomad Fintech" OR "Nomad Wealth" OR "Nomad Account") ("global account" OR "dollar and euro account" OR FX OR "international card")',
            '("Nomad Global" OR "Nomad Fintech") ("Nomad Explorer" OR "Visa Infinite" OR "Nomad Pass" OR "loyalty benefits" OR "Nomad Lounge")',
            '("Nomad Global" OR "Nomad Fintech") ("Nomad Trips" OR "AI travel planning" OR "hotel and flight bookings" OR "Nomad Chip" OR eSIM OR "travel insurance")',
            '("Nomad Global" OR "Nomad Fintech" OR "Nomad Wealth") ("international cashback" OR "installment dollar" OR "US investments" OR "stocks, ETFs and REITs")',
            '("Nomad Wealth" OR "Nomad Fintech") ("airport lounge experience" OR phygital OR "tourism partnerships" OR lifestyle OR licenses OR brokerage)',
        ]
    },
    "Revolut": {
        "en": [
            '("Revolut" OR "Revolut Bank" OR "Revolut Brazil" OR "Revolut Business" OR "Revolut Pay") ("Brazil expansion" OR Pix OR "Open Finance" OR "high yield account")',
            '("Revolut" OR "Revolut Ultra") ("global cards" OR "loans and credit" OR "premium segment" OR RevPoints OR "loyalty miles")',
            '("Revolut" OR "Revolut Business") ("international investments" OR "stocks and ETFs" OR "crypto and stablecoins" OR EURR OR "multi-currency account" OR "Revolut Pay")',
            '("Revolut Research" OR ("Revolut" AND ("artificial intelligence" OR "financial foundation models" OR PRAGMA)))',
            '("Revolut" OR "Revolut Bank") ("banking licenses" OR "Latin America expansion" OR Mexico OR Colombia OR Argentina OR Peru)',
            '("Revolut" OR "Revolut Bank") (compliance OR "regulatory restrictions" OR fraud OR "financial crime prevention" OR lifestyle)',
        ]
    },
    "Caixa Economica Federal": {
        "en": [
            '("Caixa Econômica Federal" OR "Caixa Economica" OR "CEF" OR "Caixa Habitação" OR "Caixa Seguridade") ("mortgage lending" OR "housing credit" OR "real estate funding" OR SFH OR SBPE OR "Minha Casa Minha Vida" OR LCI OR securitization OR "interest rate cap")',
            '("Caixa Econômica Federal" OR "Caixa Economica" OR "CEF" OR "Caixa Tem") ("social programs" OR "financial inclusion" OR "social benefits" OR "digital welfare" OR "digital government")',
            '("Caixa Econômica Federal" OR "Caixa Economica" OR "CEF" OR "Caixa Tem") ("generative AI" OR "digital service" OR automation OR personalization OR Pix OR "Open Finance" OR "digital wallet")',
            '("Caixa Econômica Federal" OR "Caixa Economica" OR "CEF" OR "Caixa Empresas" OR "Caixa Asset") ("rural credit" OR Pronaf OR "agribusiness financing" OR efficiency OR profitability OR "operational transformation" OR "technological modernization")',
        ]
    },
    "Itau": {
        "en": [
            '("Itaú" OR "Itau" OR "Itaú Unibanco" OR "Itau Unibanco" OR "Itaú BBA" OR "iti") ("generative AI" OR "AI agents" OR "conversational banking" OR "financial copilots" OR "AI investing" OR "personalization at scale" OR IAI)',
            '("Itaú" OR "Itau" OR "Itaú Private" OR "Itaú Asset" OR "Itaú Personnalité") ("wealth management" OR advisory OR "international investments" OR Vanguard OR "global allocation" OR "mass affluent" OR "high income")',
            '("Itaú" OR "Itau" OR "Itaú Unibanco" OR "Rede") ("embedded finance" OR "Banking as a Service" OR BaaS OR APIs OR "Open Finance" OR superapp OR "financial ecosystem")',
            '("Itaú" OR "Itau" OR "Itaú Unibanco" OR "Itaú BBA") ("corporate credit" OR "SME credit" OR "agribusiness credit" OR "green finance" OR ESG OR "regenerative agriculture" OR decarbonization OR "creator economy")',
        ]
    },
    "Bradesco": {
        "en": [
            '("Bradesco" OR "Banco Bradesco" OR "Next" OR "Ágora" OR "Agora") (BIA OR "BIA GenAI" OR "conversational banking" OR "financial assistant" OR "transactional AI" OR "AI-first banking" OR "BIA Tech")',
            '("Bradesco" OR "Banco Bradesco") ("branch closures" OR "cost reduction" OR productivity OR "operational transformation" OR digitalization OR "Meu Bradesco" OR "financial marketplace" OR "Open Finance")',
            '("Bradesco Seguros" OR ("Bradesco" AND ("climate insurance" OR "parametric insurance" OR "climate adaptation" OR "integrated protection")))',
            '("Bradesco" OR "Bradesco Asset" OR "BBI" OR "Inovabra") ("digital assets" OR tokenization OR "digital custody" OR crypto OR "tokenized assets" OR "developer productivity")',
        ]
    },
    "Bank of America": {
        "en": [
            '("Bank of America" OR "BofA" OR "Merrill Lynch" OR "Merrill") ("digital banking" OR "agentic banking" OR "agentic AI" OR "AI agents" OR "autonomous finance" OR "financial copilots")',
            '("BofA Institute" OR "BofA Global Research" OR ("Bank of America" AND ("consumer trends" OR "Gen Z economy" OR "future of banking" OR "US consumer")))',
            '("Bank of America" OR "BofA" OR "BofA Securities") ("real-time payments" OR RTP OR "instant payments" OR "cross-border payments" OR "embedded finance" OR "platform economy" OR "open banking")',
            '("Bank of America" OR "BofA" OR "Merrill") ("asset management" OR "wealth management" OR tokenization OR "tokenized assets" OR "private credit" OR "alternative investments" OR "Jio Financial" OR "Jio Credit" OR "India growth")',
        ]
    },
    "JPMorgan": {
        "en": [
            '("JPMorgan" OR "JPMorgan Chase" OR "Chase" OR "Onyx" OR "Kinexys") (tokenization OR "tokenized deposits" OR "digital assets" OR "asset tokenization" OR "blockchain settlement" OR "institutional blockchain" OR "regulated DeFi" OR "smart contracts")',
            '("JPMorgan" OR "JPMorgan Chase" OR "JP Morgan Payments") ("financial infrastructure" OR "wholesale payments" OR "programmable payments" OR "real-time treasury" OR "cross-border payments" OR "treasury services" OR "corporate payments")',
            '("JPMorgan" OR "JPMorgan Chase" OR "Chase") ("AI banking" OR "generative AI" OR "agentic AI" OR "AI in markets" OR "AI investing" OR "embedded finance" OR "API banking" OR "Banking as a Service" OR BaaS)',
            '("JPMorgan Asset Management" OR ("JPMorgan" AND ("private credit" OR "private markets" OR "alternative assets" OR "institutional investing" OR "digital cash")))',
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
        "giveaway",
        "sweepstakes",
        "how to open an account",
        "step by step tutorial",
        "daily stock movement",
        "daily exchange rate",
        "market close summary",
        "customer complaints",
        "best account ranking",
        "sponsored review",
        "sports",
        "football",
        "soccer",
        "celebrity",
        "horoscope",
        "recipe",
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
        "step by step guide",
        "terms and conditions apply",
    ]
}

PERIODO_BUSCA = "1d"
DOMINIOS_PREFERENCIAIS = []
MODELO_EMBEDDING_1024 = "BAAI/bge-m3"
SIMILARIDADE_REDUNDANCIA = 0.73
MAX_WORKERS_PARALELO = 8
TIMEOUT_REQUISICAO = 6
