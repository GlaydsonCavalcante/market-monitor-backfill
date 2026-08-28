"""Configuração para América Latina, Brasil, Portugal e Espanha."""

REGIAO_NOME = "LATAM_IBERIA"

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
    "Nubank": {
        "pt": [
            '("Nubank" OR "Nu Holdings" OR "Nu Pagamentos" OR "Nu Financeira" OR "Nubank N.A.") (lucro OR ROE OR eficiência OR ARPAC OR "receita por cliente ativo")',
            '("Nubank" OR "Nu Holdings") ("principalidade" OR engajamento OR "carteira de crédito" OR inadimplência)',
            '("Nubank" OR "Nu Holdings") ("modelos de crédito com IA" OR "revisão dinâmica de limites" OR "precificação de crédito" OR NuFormer OR "inteligência artificial")',
            '("Nubank" OR "Nu Holdings") (Croma OR Ultravioleta OR "alta renda" OR "mass affluent" OR "experiência hiperpersonalizada")',
            '("Nubank" OR "Nu Holdings") ("Nu Empresas" OR "pequenas empresas" OR NuCel OR "Nubank Shopping" OR marketplace OR investimentos OR seguros)',
            '("Nubank" OR "Nu Holdings") ("conta global" OR "parceria com Wise" OR "Open Finance" OR "licença bancária")',
            '("Nu México" OR "Nu Colombia" OR ("Nubank" AND (México OR Colômbia OR "Estados Unidos")))',
            '("Nubank" OR "Nu Holdings") (aquisições OR parcerias OR fraudes OR reclamações OR privacidade)',
        ],
        "es": [
            '("Nu México" OR "Nu Colombia" OR "Nubank" OR "Nu Holdings") (lucro OR ganancias OR ROE OR eficiencia OR ARPAC OR morosidad)',
            '("Nu México" OR "Nu Colombia" OR "Nubank") (principalidad OR "cartera de crédito" OR "modelos de crédito con IA" OR "límites dinámicos")',
            '("Nu México" OR "Nu Colombia" OR "Nubank") (NuFormer OR "inteligencia artificial" OR "experiencia hiperpersonalizada" OR Ultravioleta OR "alta renta")',
            '("Nu México" OR "Nu Colombia" OR "Nubank") ("Nu Empresas" OR marketplace OR inversiones OR seguros OR "cuenta global")',
            '("Nu México" OR "Nu Colombia" OR "Nubank") ("licencia bancaria" OR "Open Finance" OR expansión OR adquisiciones OR alianzas OR fraudes OR privacidad)',
        ],
    },
    "PicPay": {
        "pt": [
            '("PicPay" OR "PicPay Bank" OR "PicPay Card") (ChatGPT OR "integração PicPay" OR "IA como interface bancária" OR "finanças conversacionais")',
            '("PicPay" OR "PicPay Bank") ("Open Finance" OR "agregador financeiro" OR "saldo de outros bancos" OR "carteira digital")',
            '("PicPay" OR "PicPay Bank") (Pix OR "Pix parcelado" OR "crédito consignado privado" OR "Limite Garantido" OR Cofrinhos OR investimentos OR seguros)',
            '("PicPay Empresas" OR ("PicPay" AND (maquininha OR "PicPay Tap" OR "link de pagamento" OR adquirência OR "antecipação de recebíveis" OR "capital de giro")))',
            '("PicPay" OR "PicPay Bank") ("marketplace para empresas" OR IPO OR Nasdaq OR resultados OR lucro OR inadimplência)',
            '("PicPay" OR "PicPay Bank") ("expansão para viagens" OR alimentação OR fraude OR privacidade OR segurança)',
        ],
        "es": [
            '("PicPay" OR "PicPay Bank" OR "PicPay Card" OR "PicPay Empresas") (ChatGPT OR "IA conversacional" OR "interfaz bancaria" OR "Open Finance")',
            '("PicPay" OR "PicPay Bank") ("billetera digital" OR "agregador financiero" OR Pix OR créditos OR tarjetas OR inversiones OR seguros)',
            '("PicPay" OR "PicPay Bank") (adquirencia OR "PicPay Tap" OR "capital de trabajo" OR IPO OR Nasdaq OR resultados OR morosidad OR fraude OR seguridad)',
        ],
    },
    "Wise": {
        "pt": [
            '("Wise" OR "TransferWise" OR "Wise Platform" OR "Conta Wise" OR "Rende+") ("remessas internacionais" OR "pagamentos transfronteiriços" OR "cross-border payments")',
            '("Wise" OR "Wise Platform") ("Pix para estrangeiros" OR "chave Pix internacional" OR "infraestrutura global de pagamentos" OR "conexão direta" OR SPB OR SPI)',
            '("Wise" OR "Wise Platform") ("Banking as a Service" OR BaaS OR "parcerias com bancos" OR "conta multimoeda")',
            '("Wise" OR "TransferWise") ("câmbio comercial" OR "taxa comercial" OR "transparência de tarifas" OR "velocidade das transferências")',
            '("Wise Empresas" OR "Wise Business" OR ("Wise" AND ("pagamentos a fornecedores" OR freelancers OR "recebimentos internacionais PJ")))',
            '("Wise" OR "TransferWise") ("Rende+" OR licenças OR "expansão geográfica" OR fraudes OR compliance OR "prevenção à lavagem de dinheiro" OR PLD)',
        ],
        "es": [
            '("Wise" OR "TransferWise" OR "Wise Platform" OR "Cuenta Wise" OR "Wise Business") ("remesas internacionales" OR "pagos transfronterizos" OR "cross-border payments")',
            '("Wise" OR "Wise Platform") ("infraestructura global de pagos" OR "Banking as a Service" OR BaaS OR alianzas OR "cuenta multidivisa")',
            '("Wise" OR "TransferWise") ("tipo de cambio comercial" OR "transparencia de tarifas" OR "velocidad de transferencia" OR "pagos a proveedores" OR freelancers)',
            '("Wise" OR "TransferWise") (licencias OR "expansión geográfica" OR fraudes OR compliance OR "prevención de lavado de dinero" OR AML)',
        ],
    },
    "Nomad": {
        "pt": [
            '("Nomad Global" OR "Nomad Fintech" OR "Conta Nomad" OR "Nomad Wealth") ("conta internacional" OR "dólar e euro" OR câmbio OR conversão OR "cartão internacional")',
            '("Nomad Global" OR "Nomad Fintech") ("Nomad Explorer" OR "Visa Infinite" OR "Nomad Pass" OR "fidelidade e benefícios" OR "Nomad Lounge")',
            '("Nomad Global" OR "Nomad Fintech") ("Nomad Trips" OR "planejamento de viagens com IA" OR "reservas de hotéis e passagens" OR "Nomad Chip" OR eSIM OR "seguro viagem")',
            '("Nomad Global" OR "Nomad Fintech" OR "Nomad Wealth") ("cashback internacional" OR "dólar parcelado" OR "Investir para Viajar" OR "investimentos nos Estados Unidos")',
            '("Nomad Wealth" OR "Nomad Fintech") ("ações, ETFs e REITs" OR "experiência phygital em aeroportos" OR "parcerias de turismo" OR lifestyle OR licenças OR corretora)',
        ],
        "es": [
            '("Nomad Global" OR "Nomad Fintech" OR "Nomad Wealth" OR "Cuenta Nomad") ("cuenta internacional" OR "dólar y euro" OR cambio OR "tarjeta internacional")',
            '("Nomad Global" OR "Nomad Fintech") ("Nomad Explorer" OR "Nomad Pass" OR "Nomad Lounge" OR "Nomad Trips" OR "planificación de viajes con IA" OR eSIM OR "seguro de viaje")',
            '("Nomad Global" OR "Nomad Wealth") ("inversiones en Estados Unidos" OR "acciones, ETFs y REITs" OR licencias OR "alianzas de turismo" OR lifestyle)',
        ],
    },
    "Revolut": {
        "pt": [
            '("Revolut" OR "Revolut Bank" OR "Revolut Brasil" OR "Revolut Business" OR "Revolut Pay") ("expansão no Brasil" OR Pix OR "Open Finance" OR "conta remunerada em reais")',
            '("Revolut" OR "Revolut Ultra") ("cartões locais e globais" OR "crédito e empréstimos" OR "segmento premium" OR RevPoints OR "fidelidade e milhas")',
            '("Revolut" OR "Revolut Business") ("investimentos internacionais" OR "ações e ETFs" OR "criptomoedas e stablecoins" OR EURR OR "conta multimoeda" OR "Revolut Pay")',
            '("Revolut Research" OR ("Revolut" AND ("inteligência artificial" OR "modelos fundacionais financeiros" OR PRAGMA)))',
            '("Revolut" OR "Revolut Bank") ("licenças bancárias" OR "expansão na América Latina" OR México OR Colômbia OR Argentina OR Peru)',
            '("Revolut" OR "Revolut Bank") (compliance OR "restrições regulatórias" OR fraudes OR "prevenção a crimes financeiros" OR patrocínios)',
        ],
        "es": [
            '("Revolut" OR "Revolut Bank" OR "Revolut Ultra" OR "Revolut Business" OR "Revolut Pay") ("expansión en América Latina" OR México OR Colombia OR Argentina OR Perú OR "licencias bancarias")',
            '("Revolut" OR "Revolut Ultra") (RevPoints OR "tarjetas globales" OR créditos OR "cuenta remunerada" OR "segmento premium" OR "inversiones internacionales")',
            '("Revolut" OR "Revolut Business") ("acciones y ETFs" OR criptomonedas OR EURR OR "cuenta multidivisa" OR "Revolut Pay")',
            '("Revolut Research" OR ("Revolut" AND ("inteligencia artificial" OR "modelos fundacionales" OR PRAGMA)))',
            '("Revolut" OR "Revolut Bank") (compliance OR "restricciones regulatorias" OR fraudes OR "prevención de delitos financieros")',
        ],
    },
    "Caixa Economica Federal": {
        "pt": [
            '("Caixa Econômica Federal" OR "Caixa Economica" OR "CEF" OR "Caixa Habitação" OR "Caixa Seguridade") ("crédito imobiliário" OR SFH OR SBPE OR "Minha Casa Minha Vida" OR "funding imobiliário" OR LCI OR "securitização imobiliária" OR "teto de juros" OR "mercado imobiliário")',
            '("Caixa Econômica Federal" OR "Caixa Economica" OR "CEF" OR "Caixa Tem") ("programas sociais" OR "inclusão financeira" OR "benefícios sociais" OR "digitalização de benefícios" OR "governo digital")',
            '("Caixa Econômica Federal" OR "Caixa Economica" OR "CEF" OR "Caixa Tem") ("IA generativa" OR "atendimento digital" OR "jornada digital" OR automação OR personalização OR Pix OR "Pix Automático" OR "Pix Garantido" OR "carteira digital" OR "Open Finance")',
            '("Caixa Econômica Federal" OR "Caixa Economica" OR "CEF" OR "Caixa Empresas" OR "Caixa Asset") ("crédito rural" OR Pronaf OR "financiamento agro" OR "sustentabilidade no agro" OR eficiência OR produtividade OR rentabilidade OR "transformação operacional" OR "modernização tecnológica")',
        ],
        "es": [
            '("Caixa Econômica Federal" OR "Caixa Economica" OR "CEF" OR "Caixa Habitação" OR "Caixa Seguridade") ("crédito hipotecario" OR "crédito inmobiliario" OR "Minha Casa Minha Vida" OR SFH OR SBPE OR "financiación inmobiliaria" OR LCI OR "titulización inmobiliaria" OR "techo de tasas")',
            '("Caixa Econômica Federal" OR "Caixa Economica" OR "CEF" OR "Caixa Tem") ("programas sociales" OR "inclusión financiera" OR "beneficios sociales" OR "digitalización de beneficios" OR "gobierno digital")',
            '("Caixa Econômica Federal" OR "Caixa Economica" OR "CEF" OR "Caixa Tem") ("IA generativa" OR "atención digital" OR automatización OR personalización OR Pix OR "Pix Automático" OR "billetera digital" OR "Open Finance")',
            '("Caixa Econômica Federal" OR "Caixa Economica" OR "CEF" OR "Caixa Empresas" OR "Caixa Asset") ("crédito rural" OR Pronaf OR "financiamiento agro" OR eficiencia OR productividad OR rentabilidad OR "transformación operativa")',
        ],
    },
    "Itau": {
        "pt": [
            '("Itaú" OR "Itau" OR "Itaú Unibanco" OR "Itau Unibanco" OR "Itaú BBA" OR "iti") (IAI OR "IA generativa" OR "agentes de IA" OR "banco conversacional" OR "copilots financeiros" OR "personalização em escala" OR "IA para investimentos")',
            '("Itaú" OR "Itau" OR "Itaú Private" OR "Itaú Personnalité" OR "Itaú Asset") ("wealth management" OR advisory OR "investimentos internacionais" OR Vanguard OR "alocação global" OR "alta renda" OR "mass affluent")',
            '("Itaú" OR "Itau" OR "Itaú Unibanco" OR "Rede") ("embedded finance" OR "Banking as a Service" OR BaaS OR APIs OR "Open Finance" OR superapp OR "ecossistema financeiro")',
            '("Itaú" OR "Itau" OR "Itaú Unibanco" OR "Itaú BBA") ("crédito PJ" OR "pequenas empresas" OR "crédito agro" OR "crédito sustentável" OR "crédito baseado em dados" OR "finanças verdes" OR ESG OR "agricultura regenerativa" OR descarbonização OR "creator economy" OR atletas)',
        ],
        "es": [
            '("Itaú" OR "Itau" OR "Itaú Unibanco" OR "Itau Unibanco" OR "Itaú BBA" OR "iti") (IAI OR "IA generativa" OR "agentes de IA" OR "banca conversacional" OR "copilotos financieros" OR "personalización a escala" OR "IA para inversiones")',
            '("Itaú" OR "Itau" OR "Itaú Private" OR "Itaú Personnalité" OR "Itaú Asset") ("wealth management" OR asesoría OR "inversiones internacionales" OR Vanguard OR "asignación global" OR "alta renta" OR "mass affluent")',
            '("Itaú" OR "Itau" OR "Itaú Unibanco" OR "Rede") ("embedded finance" OR "Banking as a Service" OR BaaS OR APIs OR "Open Finance" OR superapp OR "ecosistema financiero")',
            '("Itaú" OR "Itau" OR "Itaú Unibanco" OR "Itaú BBA") ("crédito PJ" OR "pequeñas empresas" OR "crédito agro" OR "finanzas verdes" OR ESG OR "agricultura regenerativa" OR descarbonización OR "creator economy")',
        ],
    },
    "Bradesco": {
        "pt": [
            '("Bradesco" OR "Banco Bradesco" OR "Next" OR "Ágora") (BIA OR "BIA GenAI" OR "conversational banking" OR "assistente financeira" OR "IA transacional" OR "AI-first banking" OR "banco personalizado" OR "BIA Tech")',
            '("Bradesco" OR "Banco Bradesco") ("fechamento de agências" OR "redução de custos" OR produtividade OR "transformação operacional" OR digitalização OR "Meu Bradesco" OR "marketplace financeiro" OR "Open Finance" OR APIs)',
            '("Bradesco Seguros" OR ("Bradesco" AND ("seguro climático" OR "seguro paramétrico" OR "adaptação climática" OR "proteção integrada")))',
            '("Bradesco" OR "Bradesco Asset" OR "BBI" OR "Inovabra") ("ativos digitais" OR tokenização OR "custódia digital" OR criptomoedas OR "tokenized assets" OR "desenvolvedores" OR "IA para produtividade")',
        ],
        "es": [
            '("Bradesco" OR "Banco Bradesco" OR "Next" OR "Ágora") (BIA OR "BIA GenAI" OR "banca conversacional" OR "asistente financiero" OR "IA transaccional" OR "AI-first banking" OR "banco personalizado" OR "BIA Tech")',
            '("Bradesco" OR "Banco Bradesco") ("cierre de sucursales" OR "reducción de costes" OR productividad OR "transformación operativa" OR digitalización OR "Meu Bradesco" OR "marketplace financiero" OR "Open Finance")',
            '("Bradesco Seguros" OR ("Bradesco" AND ("seguro climático" OR "seguro paramétrico" OR "adaptación climática" OR "protección integrada")))',
            '("Bradesco" OR "Bradesco Asset" OR "BBI" OR "Inovabra") ("activos digitales" OR tokenización OR "custodia digital" OR criptomonedas OR "tokenized assets" OR "IA para productividad")',
        ],
    },
    "Bank of America": {
        "pt": [
            '("Bank of America" OR "BofA" OR "Merrill Lynch" OR "Merrill") ("digital banking" OR "agentic banking" OR "agentic AI" OR "agentes de IA" OR "autonomous finance" OR "copilots financeiros")',
            '("BofA Institute" OR "BofA Global Research" OR ("Bank of America" AND ("tendências de consumo" OR "Gen Z economy" OR "futuro dos bancos" OR "consumidor americano")))',
            '("Bank of America" OR "BofA" OR "BofA Securities") ("pagamentos em tempo real" OR RTP OR "pagamentos instantâneos" OR "cross-border payments" OR "embedded finance" OR "platform economy" OR "open banking")',
            '("Bank of America" OR "BofA" OR "Merrill") ("wealth management" OR "asset management" OR tokenização OR "tokenized assets" OR "crédito privado" OR "investimentos alternativos" OR "Jio Financial" OR "Jio Credit" OR "mercados emergentes")',
        ],
        "es": [
            '("Bank of America" OR "BofA" OR "Merrill Lynch" OR "Merrill") ("banca digital" OR "agentic banking" OR "agentic AI" OR "agentes de IA" OR "finanzas autónomas" OR "copilotos financieros")',
            '("BofA Institute" OR "BofA Global Research" OR ("Bank of America" AND ("tendencias de consumo" OR "economía Gen Z" OR "futuro de la banca" OR "consumidor estadounidense")))',
            '("Bank of America" OR "BofA" OR "BofA Securities") ("pagos en tiempo real" OR RTP OR "pagos instantáneos" OR "cross-border payments" OR "embedded finance" OR "economía de plataformas" OR "open banking")',
            '("Bank of America" OR "BofA" OR "Merrill") ("wealth management" OR "asset management" OR tokenización OR "activos tokenizados" OR "crédito privado" OR "inversiones alternativas" OR "Jio Financial" OR "mercados emergentes")',
        ],
    },
    "JPMorgan": {
        "pt": [
            '("JPMorgan" OR "JPMorgan Chase" OR "Chase" OR "Onyx" OR "Kinexys") (tokenização OR "depósitos tokenizados" OR "ativos digitais" OR "liquidação em blockchain" OR "blockchain institucional" OR "DeFi regulado" OR "smart contracts")',
            '("JPMorgan" OR "JPMorgan Chase" OR "JP Morgan Payments") ("infraestrutura financeira" OR "pagamentos corporativos" OR "wholesale payments" OR "pagamentos programáveis" OR "tesouraria em tempo real" OR "cross-border payments" OR "corporate payments")',
            '("JPMorgan" OR "JPMorgan Chase" OR "Chase") ("IA nos bancos" OR "IA generativa" OR "agentic AI" OR "IA em mercados" OR "IA para investimentos" OR "embedded finance" OR "API banking" OR BaaS)',
            '("JPMorgan Asset Management" OR ("JPMorgan" AND ("crédito privado" OR "mercados privados" OR "ativos alternativos" OR "investimento institucional" OR "digital cash")))',
        ],
        "es": [
            '("JPMorgan" OR "JPMorgan Chase" OR "Chase" OR "Onyx" OR "Kinexys") (tokenización OR "depósitos tokenizados" OR "activos digitales" OR "liquidación en blockchain" OR "blockchain institucional" OR "DeFi regulado" OR "smart contracts")',
            '("JPMorgan" OR "JPMorgan Chase" OR "JP Morgan Payments") ("infraestructura financiera" OR "pagos mayoristas" OR "pagos programables" OR "tesorería en tiempo real" OR "pagos transfronterizos" OR "servicios de tesorería")',
            '("JPMorgan" OR "JPMorgan Chase" OR "Chase") ("IA en banca" OR "IA generativa" OR "agentic AI" OR "IA en mercados" OR "embedded finance" OR "API banking" OR BaaS)',
            '("JPMorgan Asset Management" OR ("JPMorgan" AND ("crédito privado" OR "mercados privados" OR "activos alternativos" OR "inversión institucional" OR "digital cash")))',
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
        "promoção",
        "promocoes",
        "cupom",
        "cupons",
        "desconto",
        "sorteio",
        "como abrir conta",
        "passo a passo",
        "tutorial",
        "reclamação",
        "reclame aqui",
        "cotação diária",
        "fechamento do mercado",
        "melhores contas",
        "ranking",
        "horóscopo",
        "futebol",
        "esporte",
        "novela",
    ],
    "es": [
        "promoción",
        "promociones",
        "cupón",
        "cupones",
        "descuento",
        "sorteo",
        "cómo abrir cuenta",
        "paso a paso",
        "tutorial",
        "quejas",
        "reclamos",
        "cotización diaria",
        "cierre de mercado",
        "mejores cuentas",
        "ranking",
        "horóscopo",
        "fútbol",
        "deportes",
        "telenovela",
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
        "patrocinado",
        "como abrir sua conta",
        "abra sua conta em poucos passos",
        "reprodução:",
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
        "patrocinado",
        "cómo abrir tu cuenta",
        "siga leyendo",
    ],
}

PERIODO_BUSCA = "1d"
DOMINIOS_PREFERENCIAIS = []
MODELO_EMBEDDING_1024 = "BAAI/bge-m3"
SIMILARIDADE_REDUNDANCIA = 0.73
MAX_WORKERS_PARALELO = 8
TIMEOUT_REQUISICAO = 6
