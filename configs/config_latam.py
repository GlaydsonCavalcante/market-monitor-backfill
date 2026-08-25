"""Configuração para América Latina, Brasil, Portugal e Espanha."""

REGIAO_NOME = "LATAM_IBERIA"

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
        "es": [
            '"inteligencia artificial" bancos',
            '"comercio agéntico"',
            '"IA autónoma" finanzas',
            '"agentes de IA" bancos',
            '"jornadas hiperpersonalizadas"',
            '"experiencias inmersivas"',
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
        "es": [
            '"economía plateada" bancos',
            '"envejecimiento de la población"',
            '"reconfiguración demográfica"',
            '"salud digital"',
            '"longevidad activa"',
            '"terapias avanzadas"',
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
        "esporte",
        "futebol",
        "celebridade",
        "horóscopo",
        "receita",
        "novela",
        "sorteio",
        "loto",
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
    ],
}

PERIODO_BUSCA = "1d"
DOMINIOS_PREFERENCIAIS = []
MODELO_EMBEDDING_1024 = "BAAI/bge-m3"
SIMILARIDADE_REDUNDANCIA = 0.73
MAX_WORKERS_PARALELO = 8
TIMEOUT_REQUISICAO = 6
