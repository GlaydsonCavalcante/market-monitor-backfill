"""Configuração de termos categorizados por idioma e mercados-alvo."""

# 1. Termos organizados por família linguística
MONITORAMENTOS = {
    "Comércio Agentico": {
        "pt": [
            '"inteligência artificial" bancos',
            '"comércio agêntico"',
            '"IA autônoma" finanças',
            '"IA como Orquestradora da Jornada de Compra"',
            "Phygital Omnicanalidade",
            '"Jornadas hiperpersonalizadas"',
            '"Experiências imersivas" "Social Commerce"',
        ],
        "en": [
            '"artificial intelligence" banks',
            '"agentic commerce"',
            '"autonomous AI" banking',
            '"agentic AI" finance',
            '"hyper-personalized journeys"',
            '"social commerce" banking',
        ],
        "es": [
            '"inteligencia artificial" bancos',
            '"comercio agéntico"',
            '"IA autónoma" finanzas',
            '"agentes de IA" bancos',
            '"jornadas hiperpersonalizadas"',
        ],
        "fr": [
            '"intelligence artificielle" banque',
            '"commerce agentique"',
            '"IA autonome" finance',
            '"agents IA" banque',
        ],
        "de": [
            '"Künstliche Intelligenz" Banken',
            '"Agentic Commerce"',
            '"autonome KI" Finanzen',
            '"KI-Agenten" Banken',
        ],
        "zh": [
            '"人工智能" 银行',
            '"代理式商业"',
            '"自主人工智能" 金融',
            '"AI智能体" 银行',
        ],
        "ja": [
            '"人工知能" 銀行',
            '"エージェンティックコマース"',
            '"自律型AI" 金融',
            '"AIエージェント" 銀行',
        ],
        "ko": [
            '"인공지능" 은행',
            '"에이전틱 커머스"',
            '"자율형 AI" 금융',
            '"AI 에이전트" 은행',
        ],
        "hi": [
            '"आर्टिफिशियल इंटेलिजेंस" बैंक',
            '"एजेंटिक कॉमर्स"',
            '"स्वायत्त एआई" वित्त',
        ],
    },
    "Longevidade": {
        "pt": [
            '"reconfiguração demográfica"',
            '"envelhecimento da população"',
            '"economia prateada" bancos',
            '"pacto intergeracional"',
            '"saúde digital" "medicina personalizada"',
            '"longevidade ativa" bem-estar',
            '"terapias avançadas" "bioengenharia genética"',
        ],
        "en": [
            '"silver economy" banking',
            '"aging population" economy',
            '"longevity economy" finance',
            '"demographic shift" banking',
            '"digital health" "personalized medicine"',
            '"active longevity" finance',
        ],
        "es": [
            '"economía plateada" bancos',
            '"envejecimiento de la población"',
            '"reconfiguración demográfica"',
            '"salud digital"',
            '"longevidad activa"',
        ],
        "fr": [
            '"économie argentée" banque',
            '"vieillissement de la population"',
            '"transition démographique"',
            '"santé numérique"',
        ],
        "de": [
            '"Silberwirtschaft" Banken',
            '"Überalterung der Bevölkerung"',
            '"demografischer Wandel" Finanzen',
            '"digitale Gesundheit"',
        ],
        "zh": [
            '"银发经济" 银行',
            '"人口老龄化" 经济',
            '"人口结构重塑"',
            '"数字医疗"',
        ],
        "ja": [
            '"シルバーエコノミー" 銀行',
            '"人口高齢化" 経済',
            '"人口動態の変化"',
            '"デジタルヘルス"',
        ],
        "ko": [
            '"실버 이코노미" 은행',
            '"인구 고령화" 경제',
            '"인구통계학적 변화"',
            '"디지털 헬스케어"',
        ],
        "hi": [
            '"सिल्वर इकोनॉमी" बैंक',
            '"जनसंख्या का वृद्ध होना"',
            '"डिजिटल स्वास्थ्य"',
        ],
    },
}

# 2. Mercados-Alvo com Roteamento Racional (Sem produto cartesiano)
MERCADOS_ALVO = [
    # América Latina e Península Ibérica
    {"gl": "BR", "hl": "pt-BR", "lang": "pt"},
    {"gl": "PT", "hl": "pt-PT", "lang": "pt"},
    {"gl": "ES", "hl": "es-ES", "lang": "es"},
    # Mundo Anglofônico
    {"gl": "US", "hl": "en-US", "lang": "en"},
    {"gl": "GB", "hl": "en-GB", "lang": "en"},
    {"gl": "AU", "hl": "en-AU", "lang": "en"},
    {"gl": "ZA", "hl": "en-ZA", "lang": "en"},
    {"gl": "NG", "hl": "en-NG", "lang": "en"},
    # Europa Continental
    {"gl": "FR", "hl": "fr-FR", "lang": "fr"},
    {"gl": "DE", "hl": "de-DE", "lang": "de"},
    # Ásia de Vanguarda
    {"gl": "KR", "hl": "ko-KR", "lang": "ko"},
    {"gl": "JP", "hl": "ja-JP", "lang": "ja"},
    {"gl": "CN", "hl": "zh-CN", "lang": "zh"},
    {"gl": "IN", "hl": "en-IN", "lang": "en"},
    {"gl": "IN", "hl": "hi", "lang": "hi"},
]

PERIODO_BUSCA = "1d"
# Termos de exclusão e filtragem de ruído categorizados por idioma
TERMOS_EXCLUIDOS = {
    "pt": [
        "esporte",
        "futebol",
        "celebridade",
        "horóscopo",
        "receita",
        "novela",
        "sorteio",
        "loto",
        "loteria",
    ],
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
    ],
    "es": [
        "deporte",
        "fútbol",
        "celebridad",
        "horóscopo",
        "receta",
        "telenovela",
        "sorteo",
        "lotería",
    ],
    "fr": [
        "sport",
        "football",
        "célébrité",
        "horoscope",
        "recette",
        "loterie",
        "concours",
    ],
    "de": [
        "Sport",
        "Fußball",
        "Promi",
        "Horoskop",
        "Rezept",
        "Lotterie",
        "Gewinnspiel",
    ],
    "zh": [
        "体育",
        "足球",
        "明星",
        "八卦",
        "星座",
        "食谱",
        "彩票",
    ],
    "ja": [
        "スポーツ",
        "サッカー",
        "芸能人",
        "占い",
        "レシピ",
        "宝くじ",
    ],
    "ko": [
        "스포츠",
        "축구",
        "연예인",
        "운세",
        "레시피",
        "복권",
    ],
    "hi": [
        "खेल",
        "फुटबॉल",
        "सेलिब्रिटी",
        "राशिफल",
        "नुस्खा",
        "लॉटरी",
    ],
}
# Termos de descarte para higienização do corpo da matéria raspada (Boilerplate Removal)
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
        "direitos autorais",
    ],
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
        "copyright",
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
        "boletín",
        "patrocinado",
    ],
    "fr": [
        "lire la suite",
        "s'abonner",
        "partager",
        "publicité",
        "tous droits réservés",
        "photo :",
        "crédit :",
        "voir aussi",
        "rédaction",
        "cliquez ici",
        "lettre d'information",
    ],
    "de": [
        "weiterlesen",
        "abonnieren",
        "teilen",
        "werbung",
        "alle rechte vorbehalten",
        "foto:",
        "bild:",
        "siehe auch",
        "redaktion",
        "hier klicken",
        "newsletter",
    ],
    "zh": [
        "阅读更多",
        "订阅",
        "分享",
        "广告",
        "版权所有",
        "图片：",
        "来源：",
        "另请参阅",
        "编辑",
        "点击这里",
    ],
    "ja": [
        "続きを読む",
        "登録",
        "共有",
        "シェア",
        "広告",
        "無断転載を禁じます",
        "写真：",
        "出典：",
        "関連記事",
        "編集部",
        "こちらをクリック",
    ],
    "ko": [
        "더 읽기",
        "구독",
        "공유",
        "광고",
        "모든 권리 보유",
        "사진:",
        "출처:",
        "관련 기사",
        "편집국",
        "여기를 클릭",
    ],
    "hi": [
        "और पढ़ें",
        "सदस्यता लें",
        "शेयर करें",
        "विज्ञापन",
        "सर्वाधिकार सुरक्षित",
        "फोटो:",
        "स्रोत:",
        "यह भी पढ़ें",
    ],
}
DOMINIOS_PREFERENCIAIS = []
MODELO_EMBEDDING_1024 = "BAAI/bge-m3"
SIMILARIDADE_REDUNDANCIA = 0.73
MAX_WORKERS_PARALELO = 4

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
