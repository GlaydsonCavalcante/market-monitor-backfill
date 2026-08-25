"""Configurações de monitoramento, filtros de busca e modelo vetorial unificado."""

MONITORAMENTOS = {
    "Comércio Agentico": [
        '"inteligência artificial" bancos',
        '"IA como Orquestradora da Jornada de Compra"',
        '"IA autônoma"',
        "Phygital Omnicanalidade",
        '"Jornadas hiperpersonalizadas"',
        '"Experiências imersivas" "Social Commerce"',
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

PAISES_EMISSAO = [
    "BR",
    "US",
    "GB",
    "PT",
    "ES",
    "CN",
    "IN",
    "DE",
    "JP",
    "AU",
    "ID",
    "NG",
]
IDIOMAS = [
    "pt-BR",
    "pt-PT",
    "en-US",
    "en-GB",
    "en-IN",
    "en-NG",
    "en-AU",
    "es-ES",
    "zh-CN",
    "hi",
    "de",
    "ja",
    "id",
]
PERIODO_BUSCA = "1d"
TERMOS_EXCLUIDOS = [
    "esporte",
    "futebol",
    "celebridade",
    "horóscopo",
    "receita",
    "novela",
    "sorteio",
]
DOMINIOS_PREFERENCIAIS = []

# Modelo de Embedding Unificado (1024 dimensões)
MODELO_EMBEDDING_1024 = "BAAI/bge-m3"
SIMILARIDADE_REDUNDANCIA = (
    0.73  # Limiar calibrado para o BGE-M3 (duplicatas do mesmo dia)
)
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
