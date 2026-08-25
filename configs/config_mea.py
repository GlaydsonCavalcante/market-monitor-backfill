"""Configuração para Emirados Árabes, Arábia Saudita, África do Sul, Nigéria, Quênia, Egito e Índia."""

REGIAO_NOME = "ORIENTE_MEDIO_AFRICA_INDIA"

MONITORAMENTOS = {
    "Comércio Agentico": {
        "ar": [
            '"الذكاء الاصطناعي" بنوك',
            '"التجارة الوكيلة"',
            '"الذكاء الاصطناعي الذاتي" تمويل',
            '"وكلاء الذكاء الاصطناعي" بنوك',
            '"المدفوعات الذاتية"',
        ],
        "en": [
            '"agentic commerce" UAE OR "Saudi Arabia"',
            '"autonomous AI" banking Africa',
            '"agentic AI" finance India',
            '"fintech innovation" "digital payments" Africa',
            '"AI agents" banking Middle East',
        ],
        "hi": [
            '"आर्टिफिशियल इंटेलिजेंस" बैंक',
            '"एजेंटिक कॉमर्स"',
            '"स्वायत्त एआई" वित्त',
            '"एआई एजेंट" बैंक',
        ],
    },
    "Longevidade": {
        "ar": [
            '"الاقتصاد الفضي" بنوك',
            '"الشيخوخة السكانية" اقتصاد',
            '"التحول الديموغرافي"',
            '"الصحة الرقمية"',
            '"طول العمر النشط"',
        ],
        "en": [
            '"silver economy" Middle East',
            '"demographic transition" Africa finance',
            '"digital health" "personalized medicine" India',
            '"longevity economy" UAE OR "Saudi Arabia"',
            '"healthcare financing" Africa',
        ],
        "hi": [
            '"सिल्वर इकोनॉमी" बैंक',
            '"जनसंख्या का वृद्ध होना"',
            '"डिजिटल स्वास्थ्य"',
        ],
    },
}

MERCADOS_ALVO = [
    # Oriente Médio
    {"gl": "AE", "hl": "ar", "lang": "ar"},
    {"gl": "AE", "hl": "en-AE", "lang": "en"},
    {"gl": "SA", "hl": "ar", "lang": "ar"},
    {"gl": "EG", "hl": "ar", "lang": "ar"},
    # África Subsaariana
    {"gl": "ZA", "hl": "en-ZA", "lang": "en"},
    {"gl": "NG", "hl": "en-NG", "lang": "en"},
    {"gl": "KE", "hl": "en-KE", "lang": "en"},
    # Sul da Ásia
    {"gl": "IN", "hl": "en-IN", "lang": "en"},
    {"gl": "IN", "hl": "hi", "lang": "hi"},
]

TERMOS_EXCLUIDOS = {
    "ar": [
        "رياضة",
        "كرة القدم",
        "مشاهير",
        "أبراج",
        "وصفة",
        "يانصيب",
    ],
    "en": [
        "sports",
        "football",
        "cricket",
        "celebrity",
        "horoscope",
        "recipe",
        "lottery",
    ],
    "hi": [
        "खेल",
        "फुटबॉल",
        "क्रिकेट",
        "सेलिब्रिटी",
        "राशिफल",
        "नुस्खा",
        "लॉटरी",
    ],
}

TERMOS_DESCARTE_TEXTO = {
    "ar": [
        "اقرأ المزيد",
        "اشترك",
        "مشاركة",
        "إعلان",
        "جميع الحقوق محفوظة",
        "صورة:",
        "المصدر:",
        "انقر هنا",
    ],
    "en": [
        "read more",
        "subscribe",
        "share",
        "advertisement",
        "all rights reserved",
        "photo:",
        "credit:",
        "click here",
    ],
    "hi": [
        "और पढ़ें",
        "सदस्यता लें",
        "शेयर करें",
        "विज्ञापन",
        "सर्वाधिकार सुरक्षित",
        "फोटो:",
        "स्रोत:",
    ],
}

PERIODO_BUSCA = "1d"
DOMINIOS_PREFERENCIAIS = []
MODELO_EMBEDDING_1024 = "BAAI/bge-m3"
SIMILARIDADE_REDUNDANCIA = 0.73
MAX_WORKERS_PARALELO = 8
TIMEOUT_REQUISICAO = 6
