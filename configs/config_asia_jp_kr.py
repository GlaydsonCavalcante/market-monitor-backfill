"""Configuração para Japão e Coreia do Sul."""

REGIAO_NOME = "ASIA_JP_KR"

MONITORAMENTOS = {
    "Comércio Agentico": {
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
    },
    "Longevidade": {
        "ja": [
            '"シルバーエコノミー" 銀行',
            '"人口高齢化" 経済',
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
    },
}

MERCADOS_ALVO = [
    {"gl": "JP", "hl": "ja-JP", "lang": "ja"},
    {"gl": "KR", "hl": "ko-KR", "lang": "ko"},
]

TERMOS_EXCLUIDOS = {
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
}

TERMOS_DESCARTE_TEXTO = {
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
}

PERIODO_BUSCA = "1d"
DOMINIOS_PREFERENCIAIS = []
MODELO_EMBEDDING_1024 = "BAAI/bge-m3"
SIMILARIDADE_REDUNDANCIA = 0.73
MAX_WORKERS_PARALELO = 8
TIMEOUT_REQUISICAO = 5
