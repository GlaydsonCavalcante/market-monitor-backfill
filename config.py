"""Configuração de monitoramento de mercado com termos multilíngues integrados."""

# Estrutura de monitoramento: lista única de termos por tema (PT, EN, ES, FR, DE, ZH, JA, KO, HI)
MONITORAMENTOS = {
    "Comércio Agentico": [
        # Português (Brasil / Portugal)
        '"inteligência artificial" bancos',
        '"comércio agêntico"',
        '"IA autônoma" finanças',
        '"IA como Orquestradora da Jornada de Compra"',
        "Phygital Omnicanalidade",
        '"Jornadas hiperpersonalizadas"',
        '"Experiências imersivas" "Social Commerce"',
        # Inglês (EUA, Reino Unido, Índia, Nigéria, África do Sul, Austrália)
        '"artificial intelligence" banks',
        '"agentic commerce"',
        '"autonomous AI" banking',
        '"agentic AI" finance',
        '"hyper-personalized journeys"',
        '"social commerce" banking',
        # Espanhol (Espanha e América Latina)
        '"inteligencia artificial" bancos',
        '"comercio agéntico"',
        '"IA autónoma" finanzas',
        '"agentes de IA" bancos',
        '"jornadas hiperpersonalizadas"',
        # Francês (França / Europa)
        '"intelligence artificielle" banque',
        '"commerce agentique"',
        '"IA autonome" finance',
        '"agents IA" banque',
        '"parcours hyperpersonnalisés"',
        # Alemão (Alemanha / Europa Central)
        '"Künstliche Intelligenz" Banken',
        '"Agentic Commerce"',
        '"autonome KI" Finanzen',
        '"KI-Agenten" Banken',
        '"hyperpersonalisierte"',
        # Chinês Simplificado (China)
        '"人工智能" 银行',
        '"代理式商业"',
        '"自主人工智能" 金融',
        '"AI智能体" 银行',
        '"超个性化"',
        # Japonês (Japão)
        '"人工知能" 銀行',
        '"エージェンティックコマース"',
        '"自律型AI" 金融',
        '"AIエージェント" 銀行',
        '"ハイパーパーソナライゼーション"',
        # Coreano (Coreia do Sul)
        '"인공지능" 은행',
        '"에이전틱 커머스"',
        '"자율형 AI" 금융',
        '"AI 에이전트" 은행',
        '"초개인화"',
        # Hindi (Índia)
        '"आर्टिफिशियल इंटेलिजेंस" बैंक',
        '"एजेंटिक कॉमर्स"',
        '"स्वायत्त एआई" वित्त',
    ],
    "Longevidade": [
        # Português
        '"reconfiguração demográfica"',
        '"envelhecimento da população"',
        '"economia prateada" bancos',
        '"pacto intergeracional"',
        '"saúde digital" "medicina personalizada"',
        '"longevidade ativa" bem-estar "cuidado contínuo"',
        '"terapias avançadas" "bioengenharia genética"',
        # Inglês
        '"silver economy" banking',
        '"aging population" economy',
        '"longevity economy" finance',
        '"demographic shift" banking',
        '"digital health" "personalized medicine"',
        '"active longevity" finance',
        # Espanhol
        '"economía plateada" bancos',
        '"envejecimiento de la población"',
        '"reconfiguración demográfica"',
        '"salud digital"',
        '"longevidad activa"',
        # Francês
        '"économie argentée" banque',
        '"vieillissement de la population"',
        '"transition démographique"',
        '"santé numérique"',
        '"longévité active"',
        # Alemão
        '"Silberwirtschaft" Banken',
        '"Überalterung der Bevölkerung"',
        '"demografischer Wandel" Finanzen',
        '"digitale Gesundheit"',
        '"aktive Langlebigkeit"',
        # Chinês Simplificado
        '"银发经济" 银行',
        '"人口老龄化" 经济',
        '"人口结构重塑"',
        '"数字医疗"',
        '"积极老龄化"',
        # Japonês
        '"シルバーエコノミー" 銀行',
        '"人口高齢化" 経済',
        '"人口動態の変化"',
        '"デジタルヘルス"',
        '"アクティブシニア"',
        # Coreano
        '"실버 이코노미" 은행',
        '"인구 고령화" 경제',
        '"인구통계학적 변화"',
        '"디지털 헬스케어"',
        '"액티브 시니어"',
        # Hindi
        '"सिल्वर इकोनॉमी" बैंक',
        '"जनसंख्या का वृद्ध होना"',
        '"डिजिटल स्वास्थ्य"',
    ],
}

# Países de emissão expandidos (ISO 3166-1 alpha-2)
PAISES_EMISSAO = [
    "BR",  # Brasil
    "US",  # Estados Unidos
    "GB",  # Reino Unido
    "PT",  # Portugal
    "ES",  # Espanha
    "FR",  # França
    "DE",  # Alemanha
    "KR",  # Coreia do Sul
    "JP",  # Japão
    "CN",  # China
    "IN",  # Índia
    "ZA",  # África do Sul
    "NG",  # Nigéria
    "AU",  # Austrália
    "ID",  # Indonésia
]

# Idiomas para consulta (BCP 47)
IDIOMAS = [
    "pt-BR",
    "pt-PT",
    "en-US",
    "en-GB",
    "en-IN",
    "en-NG",
    "en-ZA",
    "en-AU",
    "es-ES",
    "fr-FR",
    "de-DE",
    "ko-KR",
    "ja-JP",
    "zh-CN",
    "hi",
    "id",
]

# Janela temporal de busca
PERIODO_BUSCA = "1d"

# Palavras para exclusão e redução de ruído
TERMOS_EXCLUIDOS = [
    "esporte",
    "futebol",
    "celebridade",
    "horóscopo",
    "receita",
    "novela",
    "sorteio",
    "loto",
]

# Domínios preferenciais (vazio para pesquisar toda a web)
DOMINIOS_PREFERENCIAIS = []

# Modelo de Embedding Unificado (1024 dimensões)
MODELO_EMBEDDING_1024 = "BAAI/bge-m3"

# Limiar de similaridade para deduplicação no mesmo dia
SIMILARIDADE_REDUNDANCIA = 0.73

# Quantidade de requisições paralelas
MAX_WORKERS_PARALELO = 5

# Rotação de User-Agents
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
