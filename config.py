"""Módulo de configuração e parâmetros de negócio para monitoramento de mercado."""

# Estrutura de monitoramento: Temas e termos de busca associados
MONITORAMENTOS = {
    "Comércio Agentico": [
        '"inteligência artificial" bancos',
        '"IA como Orquestradora da Jornada de Compra"',
        '"IA autônoma"',
        'Phygital Omnicanalidade',
        '"Jornadas hiperpersonalizadas"',
        '"Experiências imersivas" "Social Commerce"'
    ],
    "Longevidade": [
        '"reconfiguração demográfica"',
        '"Envelhecimento da população"',
        '"Pacto intergeracional"',
        '"Saúde digital" "medicina personalizada"',
        '"Longevidade ativa" bem-estar "cuidado contínuo"',
        '"Terapias avançadas" "bioengenharia genética"',
    ],
}

# Países de emissão das notícias (ISO 3166-1 alpha-2)
PAISES_EMISSAO = [
    "BR", "US", "GB", "PT", "ES", "CN", "IN", "DE", "JP", "AU", "ID", "NG"
]

# Idiomas para consulta (BCP 47)
IDIOMAS = [
    "pt-BR", "pt-PT",
    "en-US", "en-GB", "en-IN", "en-NG", "en-AU",
    "es-ES",
    "zh-CN",
    "hi",
    "de",
    "ja",
    "id"
]

# Janela temporal de busca (operador when do Google Notícias)
PERIODO_BUSCA = "1d"

# Palavras para exclusão e redução de ruído
TERMOS_EXCLUIDOS = ["esporte", "futebol", "celebridade", "horóscopo", "receita"]

# Domínios preferenciais (deixe vazio [] para pesquisar em toda a web)
DOMINIOS_PREFERENCIAIS = []

# Sensibilidade da IA para agrupamento semântico (0.0 a 1.0)
SIMILARIDADE_REDUNDANCIA = 0.88

# Quantidade de requisições paralelas
MAX_WORKERS_PARALELO = 4

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
]
