"""Configuração de monitoramento de Grandes Plataformas e Ecossistemas para América Latina e Península Ibérica."""

REGIAO_NOME = "LATAM_PLATAFORMAS"

MONITORAMENTOS = {
    "Mercado Livre": {
        "pt": [
            '("Mercado Livre" OR "MercadoLibre" OR "MELI" OR "Meli" OR "Mercado Livre Brasil" OR "Marketplace Mercado Livre" OR "Mercado Shops" OR "Mercado Play") (GMV OR "volume bruto de mercadorias" OR "market share" OR sellers OR "vendedores profissionais" OR "social commerce" OR "live commerce")',
            '("Mercado Livre" OR "MercadoLibre" OR "MELI" OR "Mercado Envios") (fulfillment OR "centros de distribuição" OR "last mile" OR "entrega no mesmo dia" OR "entrega em 24 horas" OR "logística própria" OR "rede logística")',
            '("Mercado Livre" OR "MercadoLibre" OR "Mercado Ads") ("retail media" OR "mídia de varejo" OR "monetização de tráfego" OR publicidade)',
            '("Mercado Livre" OR "MercadoLibre" OR "Mercado Créditos") ("crédito para vendedores" OR "capital de giro para PMEs" OR "crédito embarcado" OR "embedded lending" OR inadimplência)',
            '("Mercado Livre" OR "MercadoLibre" OR "Meli+") (fidelização OR "programa de benefícios" OR membership OR assinatura)',
            '("Mercado Livre" OR "MercadoLibre" OR "MELI") ("inteligência artificial" OR "recomendação de produtos" OR "busca conversacional" OR "agentes de IA" OR "automação logística" OR personalização)',
            '("Mercado Livre" OR "MercadoLibre" OR "MELI") ("novas verticais" OR aquisições OR fusões OR "parcerias estratégicas" OR "expansão regional")',
            '("Mercado Livre" OR "MercadoLibre" OR "MELI") ("regulação de marketplaces" OR "concorrência com Amazon" OR "tributação internacional" OR fraudes OR "produtos falsificados")',
        ],
        "es": [
            '("Mercado Libre" OR "MercadoLibre" OR "MELI" OR "Meli" OR "Marketplace Mercado Libre" OR "Mercado Shops" OR "Mercado Play") (GMV OR "volumen bruto de mercancías" OR "cuota de mercado" OR sellers OR vendedores OR "social commerce" OR "live commerce")',
            '("Mercado Libre" OR "MercadoLibre" OR "MELI" OR "Mercado Envíos") (fulfillment OR "centros de distribución" OR "última milla" OR "entrega el mismo día" OR "entrega en 24 horas" OR "logística propia")',
            '("Mercado Libre" OR "MercadoLibre" OR "Mercado Ads") ("retail media" OR "publicidad digital" OR "monetización de tráfico")',
            '("Mercado Libre" OR "MercadoLibre" OR "Mercado Créditos") ("crédito para vendedores" OR "capital de trabajo para pymes" OR "crédito embebido" OR "embedded lending")',
            '("Mercado Libre" OR "MercadoLibre" OR "Meli+") (fidelización OR "programa de beneficios" OR membresía OR suscripción)',
            '("Mercado Libre" OR "MercadoLibre" OR "MELI") ("inteligencia artificial" OR "recomendación de productos" OR "búsqueda conversacional" OR "agentes de IA" OR "automatización logística" OR personalización)',
            '("Mercado Libre" OR "MercadoLibre" OR "MELI") ("nuevas verticales" OR adquisiciones OR fusiones OR "alianzas estratégicas" OR "expansión regional")',
            '("Mercado Libre" OR "MercadoLibre" OR "MELI") ("regulación de marketplaces" OR "competencia con Amazon" OR "tributación internacional" OR fraudes OR "productos falsificados")',
        ],
    },
    "Amazon": {
        "pt": [
            '("Amazon" OR "Amazon Brasil" OR "Amazon.com" OR "Amazon Marketplace") (marketplace OR "third-party sellers" OR "vendedores parceiros" OR FBA OR "Fulfillment by Amazon")',
            '("Amazon" OR "Amazon Brasil") ("centros de distribuição" OR "robótica logística" OR "entrega ultrarrápida" OR "last mile" OR drones OR automação)',
            '("AWS" OR "Amazon Web Services" OR ("Amazon" AND ("computação em nuvem" OR "cloud computing"))) ("infraestrutura digital" OR "data centers" OR "soberania de dados")',
            '("Amazon" OR "AWS") ("Amazon Bedrock" OR "agentes de IA" OR "assistentes inteligentes" OR "Alexa+" OR Alexa OR "IA generativa")',
            '("Amazon Ads" OR ("Amazon" AND ("retail media" OR "mídia de varejo")))',
            '("Amazon Prime" OR ("Amazon" AND (fidelização OR streaming OR "ecossistema Prime" OR Prime)))',
            '("Amazon Pharmacy" OR ("Amazon" AND (telemedicina OR "saúde digital")))',
            '("Amazon" OR "AWS") ("novas verticais" OR fintech OR "embedded finance" OR aquisições)',
            '("Amazon" OR "AWS") (antitruste OR "regulação digital" OR LGPD OR "uso de dados" OR tributação)',
        ],
        "es": [
            '("Amazon" OR "Amazon Marketplace") (marketplace OR "third-party sellers" OR "vendedores externos" OR FBA OR "Fulfillment by Amazon")',
            '("Amazon") ("centros de distribución" OR "robótica logística" OR "entrega ultrarrápida" OR "última milla" OR drones OR automatización)',
            '("AWS" OR "Amazon Web Services" OR ("Amazon" AND ("computación en la nube" OR "cloud computing"))) ("infraestructura digital" OR "centros de datos" OR "soberanía de datos")',
            '("Amazon" OR "AWS") ("Amazon Bedrock" OR "agentes de IA" OR "asistentes inteligentes" OR "Alexa+" OR Alexa OR "IA generativa")',
            '("Amazon Ads" OR ("Amazon" AND ("retail media" OR "publicidad digital")))',
            '("Amazon Prime" OR ("Amazon" AND (fidelización OR streaming OR "ecosistema Prime")))',
            '("Amazon Pharmacy" OR ("Amazon" AND (telemedicina OR "salud digital")))',
            '("Amazon" OR "AWS") ("nuevas verticales" OR fintech OR "embedded finance" OR adquisiciones)',
            '("Amazon" OR "AWS") (antimonopolio OR "regulación digital" OR "privacidad de datos" OR tributación)',
        ],
    },
    "iFood": {
        "pt": [
            '("iFood" OR "Clube iFood" OR "iFood Card") (delivery OR "quick commerce" OR "entrega rápida" OR "última milha" OR "logística urbana")',
            '("iFood" OR "iFood Mercado") ("dark stores" OR "conveniência digital" OR "delivery de supermercado")',
            '("iFood Pago" OR "Conta Digital iFood" OR ("iFood" AND ("crédito para restaurantes" OR "antecipação de recebíveis" OR "embedded finance" OR "banking para restaurantes")))',
            '("iFood") ("digitalização de restaurantes" OR "gestão de restaurantes" OR "ERP para restaurantes" OR "ecossistema do parceiro")',
            '("iFood Ads") ("retail media" OR "monetização da audiência" OR publicidade)',
            '("iFood Benefícios") ("vale refeição" OR "vale alimentação" OR "benefícios flexíveis" OR PAT)',
            '("iFood") ("IA para logística" OR "planejamento de demanda" OR "roteirização inteligente" OR "IA conversacional")',
            '("iFood") ("gig economy" OR "economia de plataforma" OR entregadores OR "relações trabalhistas")',
            '("iFood") ("novas categorias" OR finanças OR saúde OR "super app")',
            '("iFood") ("regulação do trabalho de plataforma" OR "concorrência com Rappi" OR "concorrência com 99Food" OR "segurança alimentar")',
        ],
        "es": [
            '("iFood" OR "Clube iFood" OR "iFood Card") (delivery OR "quick commerce" OR "entrega rápida" OR "última milla" OR "logística urbana")',
            '("iFood" OR "iFood Mercado") ("dark stores" OR "conveniencia digital" OR "delivery de supermercado")',
            '("iFood Pago" OR "Cuenta Digital iFood" OR ("iFood" AND ("crédito para restaurantes" OR "anticipo de facturas" OR "embedded finance")))',
            '("iFood") ("digitalización de restaurantes" OR "gestión de restaurantes" OR "ERP para restaurantes")',
            '("iFood Ads" OR ("iFood" AND ("retail media" OR "monetización de audiencia")))',
            '("iFood Beneficios" OR ("iFood" AND ("vales de comida" OR "beneficios flexibles")))',
            '("iFood") ("IA para logística" OR "enrutamiento inteligente" OR "planificación de demanda")',
            '("iFood") ("gig economy" OR "economía de plataforma" OR repartidores OR "relaciones laborales")',
            '("iFood") ("nuevas categorías" OR finanzas OR salud OR "super app" OR regulación OR Rappi)',
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
        "promoção", "promocoes", "cupom", "cupons", "desconto", "sorteio",
        "como abrir conta", "passo a passo", "tutorial", "reclamação",
        "reclame aqui", "cotação diária", "fechamento do mercado",
        "melhores contas", "ranking", "horóscopo", "futebol", "esporte", "novela",
    ],
    "es": [
        "promoción", "promociones", "cupón", "cupones", "descuento", "sorteo",
        "cómo abrir cuenta", "paso a paso", "tutorial", "quejas", "reclamos",
        "cotización diaria", "cierre de mercado", "mejores cuentas",
        "ranking", "horóscopo", "fútbol", "deportes", "telenovela",
    ],
}

TERMOS_DESCARTE_TEXTO = {
    "pt": [
        "leia mais", "inscreva-se", "compartilhe", "publicidade",
        "todos os direitos reservados", "foto:", "crédito:", "veja também",
        "redação", "clique aqui", "newsletter", "patrocinado",
        "como abrir sua conta", "abra sua conta em poucos passos", "reprodução:",
    ],
    "es": [
        "leer más", "suscríbete", "suscribirse", "compartir", "publicidad",
        "todos los derechos reservados", "foto:", "crédito:", "ver también",
        "redacción", "haz clic aquí", "patrocinado", "cómo abrir tu cuenta", "siga leyendo",
    ],
}

PERIODO_BUSCA = "1d"
DOMINIOS_PREFERENCIAIS = []
MODELO_EMBEDDING_1024 = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
SIMILARIDADE_REDUNDANCIA = 0.73
MAX_WORKERS_PARALELO = 8
TIMEOUT_REQUISICAO = 6
