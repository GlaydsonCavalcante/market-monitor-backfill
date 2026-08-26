"""Configuração para América Latina, Brasil, Portugal e Espanha."""

REGIAO_NOME = "LATAM_IBERIA"

MONITORAMENTOS = {
    "Reinvencao do Consumo": {
        "pt": [
            '("reinvenção do consumo" OR "comportamento do consumidor" OR "futuro do consumo") ("jornada de compra" OR phygital OR omnicanalidade)',
            '("agentic commerce" OR "comércio agêntico" OR "shopping agents" OR "autonomous commerce" OR "pagamentos agênticos")',
            '("IA conversacional" OR "comércio conversacional" OR "voice commerce" OR "predictive commerce" OR hiperpersonalização)',
            '("frictionless commerce" OR "embedded commerce" OR "unified commerce" OR "pagamentos invisíveis")',
            '("social commerce" OR "live commerce" OR "creator commerce" OR "TikTok Shop" OR "WhatsApp commerce")',
            '("realidade aumentada" OR "virtual try-on" OR "experiências imersivas" OR "autonomia do consumidor")',
            '("soberania dos dados" OR "identidade digital" OR "fadiga digital" OR "dark patterns" OR "manipulação algorítmica")',
            '("experiências autênticas" OR "humanização do atendimento" OR "busca pelo analógico")',
        ],
        "es": [
            '("reinvención del consumo" OR "comportamiento del consumidor" OR "futuro del consumo") ("viaje de compra" OR omnicanalidad OR phygital)',
            '("comercio agéntico" OR "agentic commerce" OR "agentes de compra" OR "comercio autónomo" OR "pagos agénticos")',
            '("IA conversacional" OR "comercio conversacional" OR "comercio predictivo" OR hiperpersonalización)',
            '("comercio unificado" OR "embedded commerce" OR "pagos invisibles" OR "comercio sin fricción")',
            '("social commerce" OR "live commerce" OR "creator commerce" OR "TikTok Shop" OR "WhatsApp commerce")',
            '("realidad aumentada" OR "probador virtual" OR "experiencias inmersivas" OR "autonomía del consumidor")',
            '("soberanía de datos" OR "identidad digital" OR "fatiga digital" OR "patrones oscuros" OR "manipulación algorítmica")',
            '("experiencias auténticas" OR "humanización del servicio" OR "búsqueda de lo analógico")',
        ],
    },
    "Nubank": {
        "pt": [
            '("Nubank" OR "Nu Holdings" OR "Nu Pagamentos" OR "Nu Financeira" OR "Nubank N.A.") (lucro OR ROE OR ARPAC OR inadimplência OR "carteira de crédito")',
            '("Nubank" OR "Nu Holdings") ("modelos de crédito" OR "precificação de crédito" OR NuFormer OR "inteligência artificial")',
            '("Nubank" OR "Nu Holdings") (Ultravioleta OR Croma OR "alta renda" OR "mass affluent")',
            '("Nubank" OR "Nu Holdings") ("Nu Empresas" OR NuCel OR "Nubank Shopping" OR marketplace OR investimentos OR seguros)',
            '("Nubank" OR "Nu Holdings") ("conta global" OR "Open Finance" OR "licença bancária" OR "parceria com Wise")',
            '("Nu México" OR "Nu Colombia" OR ("Nubank" AND (México OR Colômbia OR "Estados Unidos")))',
            '("Nubank" OR "Nu Holdings") (aquisições OR fraudes OR privacidade OR segurança)',
        ],
        "es": [
            '("Nu México" OR "Nu Colombia" OR "Nubank" OR "Nu Holdings") (ganancias OR ROE OR ARPAC OR morosidad OR "cartera de crédito")',
            '("Nu México" OR "Nu Colombia" OR "Nubank") ("modelos de crédito" OR NuFormer OR "inteligencia artificial" OR hiperpersonalización)',
            '("Nu México" OR "Nu Colombia" OR "Nubank") ("licencia bancaria" OR expansión OR adquisiciones OR inversiones)',
            '("Nu México" OR "Nu Colombia" OR "Nubank") (fraudes OR privacidad OR seguridad OR "Open Finance")',
        ],
    },
    "PicPay": {
        "pt": [
            '("PicPay" OR "PicPay Bank" OR "PicPay Empresas" OR "PicPay Card") (ChatGPT OR "IA conversacional" OR "interface bancária")',
            '("PicPay" OR "PicPay Bank") ("Open Finance" OR "agregador financeiro" OR "carteira digital" OR "Pix parcelado")',
            '("PicPay" OR "PicPay Bank") ("crédito consignado" OR "Limite Garantido" OR Cofrinhos OR investimentos OR seguros)',
            '("PicPay Empresas" OR ("PicPay" AND (maquininha OR "PicPay Tap" OR adquirência OR "capital de giro" OR marketplace)))',
            '("PicPay" OR "PicPay Bank") (IPO OR Nasdaq OR lucro OR resultados OR inadimplência OR fraudes OR viagens)',
        ],
        "es": [
            '("PicPay" OR "PicPay Bank") (ChatGPT OR "inteligencia artificial" OR "Open Finance" OR billetera OR Pix)',
            '("PicPay" OR "PicPay Bank") (IPO OR Nasdaq OR resultados OR crédito OR adquirencia OR fraude)',
        ],
    },
    "Wise": {
        "pt": [
            '("Wise" OR "TransferWise" OR "Wise Platform" OR "Wise Business" OR "Conta Wise" OR "Rende+") ("remessas internacionais" OR "cross-border" OR "pagamentos transfronteiriços")',
            '("Wise" OR "Wise Platform") (Pix OR SPB OR SPI OR "Banking as a Service" OR parcerias OR "conta multimoeda")',
            '("Wise" OR "TransferWise") ("taxa comercial" OR tarifas OR velocidade OR "Wise Empresas" OR fornecedores)',
            '("Wise" OR "TransferWise") (licenças OR expansão OR fraudes OR compliance OR PLD OR AML)',
        ],
        "es": [
            '("Wise" OR "TransferWise" OR "Wise Platform" OR "Wise Business" OR "Cuenta Wise") ("remesas internacionales" OR "cross-border" OR "pagos transfronterizos")',
            '("Wise" OR "Wise Platform") ("Banking as a Service" OR alianzas OR "cuenta multidivisa" OR tarifas OR licencias)',
            '("Wise" OR "TransferWise") ("Wise Empresas" OR freelancers OR fraude OR compliance OR "lavado de dinero")',
        ],
    },
    "Nomad": {
        "pt": [
            '("Nomad Global" OR "Nomad Fintech" OR "Conta Nomad" OR "Nomad Wealth") ("conta internacional" OR dólar OR euro OR câmbio)',
            '("Nomad Global" OR "Nomad Fintech") ("Nomad Explorer" OR "Visa Infinite" OR "Nomad Pass" OR "Nomad Lounge")',
            '("Nomad Global" OR "Nomad Fintech") ("Nomad Trips" OR "Nomad Chip" OR eSIM OR passagens OR "seguro viagem")',
            '("Nomad Global" OR "Nomad Wealth" OR "Nomad Fintech") ("Investir para Viajar" OR investimentos OR ações OR ETFs OR REITs OR licenças)',
        ],
        "es": [
            '("Nomad Global" OR "Nomad Fintech") ("cuenta internacional" OR dólar OR transferencias OR "Nomad Pass" OR "Nomad Lounge")',
            '("Nomad Global" OR "Nomad Wealth" OR "Nomad Fintech") (inversiones OR ETFs OR acciones OR licencias OR "seguro de viaje")',
        ],
    },
    "Revolut": {
        "pt": [
            '("Revolut" OR "Revolut Bank" OR "Revolut Brasil" OR "Revolut Business" OR "Revolut Pay") (Brasil OR Pix OR "Open Finance" OR "conta remunerada")',
            '("Revolut" OR "Revolut Ultra") ("RevPoints" OR milhas OR investimentos OR ações OR criptomoedas OR EURR OR "conta multimoeda")',
            '("Revolut" OR "Revolut Research") ("modelos fundacionais" OR PRAGMA OR "inteligência artificial" OR "licença bancária")',
            '("Revolut") ("América Latina" OR México OR Colômbia OR Argentina OR Peru OR compliance OR fraudes)',
        ],
        "es": [
            '("Revolut" OR "Revolut Bank" OR "Revolut Ultra" OR "Revolut Business" OR "Revolut Pay") ("América Latina" OR México OR Colombia OR Argentina OR Perú)',
            '("Revolut" OR "Revolut Ultra") (RevPoints OR inversiones OR criptomonedas OR EURR OR "cuenta multidivisa" OR crédito)',
            '("Revolut" OR "Revolut Research") ("inteligencia artificial" OR PRAGMA OR "licencias bancarias" OR compliance OR fraude)',
        ],
    },
}

MERCADOS_ALVO = [
    {"gl": "BR", "hl": "pt-BR", "lang": "pt"},
    {"gl": "PT", "hl": "pt-PT", "lang": "pt"},
    {"gl": "ES", "hl": "es-ES", "lang": "es"},
    {"gl": "MX", "hl": "es-419", "lang": "es"},
    {"gl": "AR", "hl": "es-419", "lang": "es"},
    {"gl": "CL", "hl": "es-419", "lang": "es"},
    {"gl": "CO", "hl": "es-419", "lang": "es"},
]

TERMOS_EXCLUIDOS = {
    "pt": [
        "promoção",
        "promocoes",
        "cupom",
        "cupons",
        "sorteio",
        "como abrir conta",
        "passo a passo",
        "reclamação",
        "reclame aqui",
        "cotação diária",
        "horóscopo",
        "futebol",
        "esporte",
    ],
    "es": [
        "promoción",
        "promociones",
        "cupón",
        "cupones",
        "sorteo",
        "cómo abrir cuenta",
        "paso a paso",
        "quejas",
        "reclamos",
        "cotización diaria",
        "horóscopo",
        "fútbol",
        "deportes",
    ],
}

TERMOS_DESCARTE_TEXTO = {
    "pt": [
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
        "patrocinado",
        "como abrir sua conta",
    ],
    "es": [
        "leer más",
        "suscríbete",
        "suscribirse",
        "compartir",
        "publicidad",
        "todos los derechos reservados",
        "foto:",
        "crédito:",
        "ver también",
        "redacción",
        "haz clic aquí",
        "patrocinado",
    ],
}

PERIODO_BUSCA = "1d"
DOMINIOS_PREFERENCIAIS = []
MODELO_EMBEDDING_1024 = "BAAI/bge-m3"
SIMILARIDADE_REDUNDANCIA = 0.73
MAX_WORKERS_PARALELO = 8
TIMEOUT_REQUISICAO = 6
