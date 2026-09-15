"""Configuração de monitoramento de Megatendências e Cenários de Futuro para América Latina e Península Ibérica."""

REGIAO_NOME = "LATAM_TENDENCIAS"

MONITORAMENTOS = {
    "Reinvencao do Consumo": {
        "pt": [
            '("reinvenção do consumo" OR "comportamento do consumidor" OR "futuro do consumo") ("jornada de compra" OR "jornada não linear" OR "jornada contínua")',
            '("comércio agêntico" OR "agentic commerce" OR "shopping agents" OR "agentes de compra" OR "autonomous commerce" OR "AI shopping" OR "pagamentos agênticos")',
            '("IA conversacional" OR "comércio conversacional" OR "voice commerce" OR "consumo antecipatório" OR "predictive commerce")',
            '("hiperpersonalização" OR "recomendação em tempo real" OR "context-aware commerce" OR "next best offer")',
            '("omnicanalidade" OR phygital OR "unified commerce" OR "embedded commerce" OR "frictionless commerce" OR "pagamentos invisíveis")',
            '("social commerce" OR "live commerce" OR "live shopping" OR "creator commerce" OR "shoppable content" OR "TikTok Shop" OR "WhatsApp commerce")',
            '("experiências imersivas" OR "realidade aumentada no varejo" OR "virtual try-on" OR "autonomia do consumidor")',
            '("privacidade do consumidor" OR "soberania dos dados" OR "identidade digital" OR "fadiga digital" OR "fadiga de personalização")',
            '("dark patterns" OR "manipulação algorítmica" OR "busca pelo analógico" OR "experiências autênticas" OR "humanização do atendimento")',
        ],
        "es": [
            '("reinvención del consumo" OR "comportamiento del consumidor" OR "futuro del consumo") ("viaje de compra" OR "jornada continua" OR "jornada no lineal")',
            '("comercio agéntico" OR "agentic commerce" OR "agentes de compra" OR "shopping agents" OR "comercio autónomo" OR "AI shopping" OR "pagos agénticos")',
            '("IA conversacional" OR "comercio conversacional" OR "voice commerce" OR "consumo anticipatorio" OR "comercio predictivo")',
            '("hiperpersonalización" OR "recomendación en tiempo real" OR "context-aware commerce" OR "next best offer")',
            '("omnicanalidad" OR phygital OR "comercio unificado" OR "embedded commerce" OR "comercio sin fricción" OR "pagos invisibles")',
            '("social commerce" OR "live commerce" OR "live shopping" OR "creator commerce" OR "shoppable content" OR "TikTok Shop" OR "WhatsApp commerce")',
            '("experiencias inmersivas" OR "realidad aumentada en retail" OR "probador virtual" OR "autonomía del consumidor")',
            '("privacidad del consumidor" OR "soberanía de datos" OR "identidad digital" OR "fatiga digital" OR "fatiga de personalización")',
            '("patrones oscuros" OR "manipulación algorítmica" OR "búsqueda de lo analógico" OR "experiencias auténticas" OR "humanización del servicio")',
        ],
    },
    "Reconfiguracao Demografica": {
        "pt": [
            '("reconfiguração demográfica" OR "transição demográfica" OR "mudança demográfica" OR "envelhecimento populacional" OR "envelhecimento da população" OR "sociedade envelhecida" OR "sociedade longeva" OR longevidade OR superenvelhecimento OR "declínio populacional" OR "inverno demográfico" OR "bônus demográfico" OR "razão de dependência" OR "estrutura etária" OR "pirâmide populacional" OR "dinâmica populacional")',
            '("queda da natalidade" OR "baixa natalidade" OR "taxa de fecundidade" OR "colapso da fecundidade" OR "crise demográfica" OR "menos filhos" OR "adiamento da maternidade" OR "adiamento da paternidade" OR "famílias menores" OR "não parentalidade" OR childfree OR infertilidade OR "reprodução assistida" OR "incentivos à natalidade")',
            '("economia da longevidade" OR "longevity economy" OR "envelhecimento ativo" OR "healthy aging" OR "silver economy" OR "silver market" OR "geração prata" OR "60+" OR "80+" OR centenários OR supercentenários OR "expectativa de vida" OR "extensão da vida" OR "life extension" OR "Aging tech" OR "AgeTech" OR "medicina da longevidade" OR "rejuvenescimento celular" OR gerociência)',
            '("escassez de mão de obra" OR "falta de trabalhadores" OR "envelhecimento da força de trabalho" OR "workforce aging" OR "requalificação profissional" OR reskilling OR "lifelong learning" OR "aprendizagem contínua" OR "carreiras não lineares" OR "segunda carreira" OR "trabalho após aposentadoria" OR "aposentadoria tardia" OR multigeracionalidade OR "convivência de gerações" OR "talento sênior" OR "economia dos cuidados")',
            '("reforma da previdência" OR "sustentabilidade previdenciária" OR "crise previdenciária" OR "sistemas de aposentadoria" OR "pacto intergeracional" OR "proteção social" OR "dependência econômica" OR "previdência complementar" OR "planejamento da aposentadoria" OR "renda na longevidade" OR "decumulação patrimonial")',
            '("cuidados de longa duração" OR "long-term care" OR "care economy" OR "economia do cuidado" OR cuidadores OR "cuidado domiciliar" OR "home care" OR "saúde digital" OR "digital health" OR "monitoramento remoto" OR telemedicina OR "medicina personalizada" OR "saúde preventiva" OR "envelhecimento saudável" OR "doenças crônicas" OR demência OR Alzheimer)',
            '("famílias unipessoais" OR "pessoas morando sozinhas" OR "novos arranjos familiares" OR "geração sanduíche" OR solidão OR "solitude e envelhecimento" OR "isolamento social" OR "casamentos tardios" OR "menos casamentos" OR "baixa formação de famílias" OR "transformação familiar")',
            '("migração internacional" OR "fluxos migratórios" OR "imigração qualificada" OR "refugiados climáticos" OR "mobilidade humana" OR "migração por trabalho" OR "êxodo rural" OR urbanização OR desurbanização OR interiorização OR "crescimento da África" OR "África Subsaariana" OR "dividendo demográfico africano")',
            '("cidades amigáveis ao idoso" OR "age-friendly cities" OR "moradia para idosos" OR "senior living" OR "comunidades intergeracionais" OR "habitação adaptada" OR "acessibilidade urbana" OR "mobilidade inclusiva" OR "envelhecimento urbano")',
            '("planejamento financeiro para longevidade" OR "wealth transfer" OR "sucessão patrimonial" OR herança OR "proteção de renda" OR "seguro de cuidados" OR "seguro de longevidade" OR "previdência privada" OR "investimentos para aposentadoria" OR "gestão patrimonial multigeracional" OR "mercado sênior")',
            '("quem financiará a longevidade" OR "crise dos sistemas previdenciários" OR "escassez global de trabalhadores" OR "colapso demográfico" OR "sociedade dos 100 anos" OR "trabalho até os 70 anos" OR "queda da população economicamente ativa" OR "guerra por talentos" OR "automação e escassez de mão de obra" OR "migração como solução demográfica" OR "sustentabilidade do pacto intergeracional")',
        ],
        "es": [
            '("reconfiguración demográfica" OR "transición demográfica" OR "cambio demográfico" OR "envejecimiento poblacional" OR "envejecimiento de la población" OR "sociedad envejecida" OR "sociedad longeva" OR longevidad OR superenvejecimiento OR "declive poblacional" OR "invierno demográfico" OR "bono demográfico" OR "tasa de dependencia" OR "pirámide poblacional")',
            '("caída de la natalidad" OR "baja natalidad" OR "tasa de fecundidad" OR "colapso de la fecundidad" OR "crisis demográfica" OR "menos hijos" OR "retraso de la maternidad" OR "familias más pequeñas" OR infertilidad OR "reproducción asistida" OR "incentivos a la natalidad")',
            '("economía de la longevidad" OR "longevity economy" OR "envejecimiento activo" OR "healthy aging" OR "silver economy" OR "economía plateada" OR "AgeTech" OR "medicina de la longevidad" OR "esperanza de vida" OR "extensión de la vida")',
            '("escasez de mano de obra" OR "falta de trabajadores" OR "envejecimiento de la fuerza laboral" OR "workforce aging" OR reskilling OR "aprendizaje continuo" OR "jubilación tardía" OR multigeneracionalidad OR "economía del cuidado")',
            '("reforma de pensiones" OR "sostenibilidad previsional" OR "crisis de pensiones" OR "sistemas de jubilación" OR "pacto intergeneracional" OR "protección social" OR "planes de pensiones" OR "decumulación patrimonial")',
            '("cuidados de larga duración" OR "long-term care" OR "care economy" OR "economía del cuidado" OR cuidadores OR "cuidado domiciliario" OR "salud digital" OR telemedicina OR "envejecimiento saludable" OR Alzheimer)',
            '("hogares unipersonales" OR "personas que viven solas" OR "generación sándwich" OR soledad OR "aislamiento social" OR "transformación familiar")',
            '("migración internacional" OR "flujos migratorios" OR "inmigración cualificada" OR "refugiados climáticos" OR "ciudades amigables con mayores" OR "senior living")',
            '("planificación financiera para longevidad" OR "wealth transfer" OR "sucesión patrimonial" OR herencia OR "seguro de longevidad" OR "pensiones privadas" OR "gestión patrimonial multigeneracional")',
            '("colapso demográfico" OR "sociedad de los 100 años" OR "trabajo hasta los 70 años" OR "caída de la población activa" OR "guerra por el talento" OR "sostenibilidad del pacto intergeneracional")',
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
MODELO_EMBEDDING_1024 = "BAAI/bge-m3"
SIMILARIDADE_REDUNDANCIA = 0.73
MAX_WORKERS_PARALELO = 8
TIMEOUT_REQUISICAO = 6