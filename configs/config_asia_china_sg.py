"""Configuração para China e Singapura."""

REGIAO_NOME = "ASIA_CN_SG"

MONITORAMENTOS = {
    "Comércio Agentico": {
        "zh": [
            '"人工智能" 银行',
            '"代理式商业"',
            '"自主人工智能" 金融',
            '"AI智能体" 银行',
            '"超个性化"',
        ],
        "en": [
            '"agentic commerce" Singapore',
            '"autonomous AI" banking Asia',
            '"AI agents" finance Singapore',
        ],
    },
    "Longevidade": {
        "zh": [
            '"银发经济" 银行',
            '"人口老龄化" 经济',
            '"人口结构重塑"',
            '"数字医疗"',
            '"积极老龄化"',
        ],
        "en": [
            '"silver economy" Asia banking',
            '"longevity economy" Singapore',
            '"digital health" Singapore',
        ],
    },
}

MERCADOS_ALVO = [
    {"gl": "CN", "hl": "zh-CN", "lang": "zh"},
    {"gl": "SG", "hl": "en-SG", "lang": "en"},
]

TERMOS_EXCLUIDOS = {
    "zh": [
        "体育",
        "足球",
        "明星",
        "八卦",
        "星座",
        "食谱",
        "彩票",
    ],
    "en": ["sports", "football", "celebrity", "lottery", "gossip"],
}

TERMOS_DESCARTE_TEXTO = {
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
    ],
    "en": ["read more", "subscribe", "share", "advertisement"],
}

PERIODO_BUSCA = "1d"
DOMINIOS_PREFERENCIAIS = []
MODELO_EMBEDDING_1024 = "BAAI/bge-m3"
SIMILARIDADE_REDUNDANCIA = 0.73
MAX_WORKERS_PARALELO = 8
TIMEOUT_REQUISICAO = 5
