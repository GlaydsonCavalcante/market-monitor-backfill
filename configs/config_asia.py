"""Configuração para China, Japão, Coreia do Sul e Singapura."""

REGIAO_NOME = "ASIA_VANGUARDA"

MONITORAMENTOS = {
    "Comércio Agentico": {
        "zh": [
            '"人工智能" 银行',
            '"代理式商业"',
            '"自主人工智能" 金融',
            '"AI智能体" 银行',
            '"超个性化"',
        ],
        "ja": [
            '"人工知能" 銀行',
            '"エージェンティックコマース"',
            '"自律型AI" 金融',
            '"AIエージェント" 銀行',
            '"ハイパーパーソナライゼーション"',
        ],
        "ko": [
            '"인공지능" 은행',
            '"에이전틱 커머스"',
            '"자율형 AI" 금융',
            '"AI 에이전트" 은행',
            '"초개인화"',
        ],
        "en": [
            '"agentic commerce" Singapore',
            '"autonomous AI" banking Asia',
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
        "ja": [
            '"シルバーエコノミー" 銀行',
            '"人口高齢化" 经济',
            '"人口動態の変化"',
            '"デジタルヘルス"',
            '"アクティブシニア"',
        ],
        "ko": [
            '"실버 이코노미" 은행',
            '"인구 고령화" 경제',
            '"인구통계학적 변화"',
            '"디지털 헬스케어"',
            '"액티브 시니어"',
        ],
        "en": [
            '"silver economy" Asia banking',
            '"longevity economy" Singapore',
        ],
    },
}

MERCADOS_ALVO = [
    {"gl": "CN", "hl": "zh-CN", "lang": "zh"},
    {"gl": "JP", "hl": "ja-JP", "lang": "ja"},
    {"gl": "KR", "hl": "ko-KR", "lang": "ko"},
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
    "en": ["sports", "football", "celebrity", "lottery"],
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
    "ja": [
        "続きを読む",
        "登録",
        "共有",
        "シェア",
        "広告",
        "無断転載を禁じます",
        "写真：",
        "出典：",
        "編集部",
    ],
    "ko": [
        "더 읽기",
        "구독",
        "공유",
        "광고",
        "모든 권리 보유",
        "사진:",
        "출처:",
        "편집국",
    ],
    "en": ["read more", "subscribe", "share", "advertisement"],
}

PERIODO_BUSCA = "1d"
DOMINIOS_PREFERENCIAIS = []
MODELO_EMBEDDING_1024 = "BAAI/bge-m3"
SIMILARIDADE_REDUNDANCIA = 0.73
MAX_WORKERS_PARALELO = 8
TIMEOUT_REQUISICAO = 6
