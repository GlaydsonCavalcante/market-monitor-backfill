"""Configuração para França, Alemanha, Itália e Suíça."""

REGIAO_NOME = "EUROPA_CONTINENTAL"

MONITORAMENTOS = {
    "Comércio Agentico": {
        "fr": [
            '"intelligence artificielle" banque',
            '"commerce agentique"',
            '"IA autonome" finance',
            '"agents IA" banque',
            '"parcours hyperpersonnalisés"',
        ],
        "de": [
            '"Künstliche Intelligenz" Banken',
            '"Agentic Commerce"',
            '"autonome KI" Finanzen',
            '"KI-Agenten" Banken',
            '"hyperpersonalisierte"',
        ],
        "it": [
            '"intelligenza artificiale" banche',
            '"commercio agentico"',
            '"IA autonoma" finanza',
            '"agenti IA" banche',
        ],
    },
    "Longevidade": {
        "fr": [
            '"économie argentée" banque',
            '"vieillissement de la population"',
            '"transition démographique"',
            '"santé numérique"',
            '"longévité active"',
        ],
        "de": [
            '"Silberwirtschaft" Banken',
            '"Überalterung der Bevölkerung"',
            '"demografischer Wandel" Finanzen',
            '"digitale Gesundheit"',
            '"aktive Langlebigkeit"',
        ],
        "it": [
            '"economia d\'argento" banche',
            '"invecchiamento della popolazione"',
            '"transizione demografica"',
            '"salute digitale"',
        ],
    },
}

MERCADOS_ALVO = [
    {"gl": "FR", "hl": "fr-FR", "lang": "fr"},
    {"gl": "DE", "hl": "de-DE", "lang": "de"},
    {"gl": "IT", "hl": "it-IT", "lang": "it"},
    {"gl": "CH", "hl": "de-CH", "lang": "de"},
    {"gl": "CH", "hl": "fr-CH", "lang": "fr"},
]

TERMOS_EXCLUIDOS = {
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
    "it": [
        "sport",
        "calcio",
        "celebrità",
        "oroscopo",
        "ricetta",
        "lotteria",
    ],
}

TERMOS_DESCARTE_TEXTO = {
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
    ],
    "it": [
        "leggi di più",
        "iscriviti",
        "condividi",
        "pubblicità",
        "tutti i diritti riservati",
        "foto:",
        "credito:",
        "vedi anche",
        "redazione",
    ],
}

PERIODO_BUSCA = "1d"
DOMINIOS_PREFERENCIAIS = []
MODELO_EMBEDDING_1024 = "BAAI/bge-m3"
SIMILARIDADE_REDUNDANCIA = 0.73
MAX_WORKERS_PARALELO = 8
TIMEOUT_REQUISICAO = 6
