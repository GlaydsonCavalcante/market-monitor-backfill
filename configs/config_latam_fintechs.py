"""Configuração de monitoramento de Fintechs e Neobanks para América Latina e Península Ibérica."""

REGIAO_NOME = "LATAM_FINTECHS"

MONITORAMENTOS = {
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
    "Mercado Pago": {
        "pt": [
            '("Mercado Pago" OR "MercadoPago" OR "Mercado Pago Brasil" OR "Mercado Pago Bank" OR "Conta Mercado Pago") ("banco digital" OR "conta digital" OR "conta remunerada" OR CDI OR "captura de depósitos" OR salário OR "principalidade financeira")',
            '("Mercado Pago" OR "MercadoPago") (Pix OR "Pix Automático" OR "QR Code" OR Checkout OR "Tap to Pay" OR adquirência OR "gateway de pagamento" OR Point)',
            '("Mercado Pago" OR "MercadoPago" OR "Conta Negócio Mercado Pago") ("gestão financeira de PMEs" OR "ERP financeiro" OR "digitalização de PMEs" OR "fluxo de caixa")',
            '("Mercado Pago" OR "MercadoPago" OR "Mercado Créditos") (empréstimos OR "capital de giro" OR "crédito para vendedores" OR "crédito baseado em dados" OR "underwriting com IA" OR "score alternativo")',
            '("Mercado Pago" OR "MercadoPago") (cofrinhos OR "produtos de investimento" OR "tesouraria digital" OR CDI OR CDB OR "embedded finance" OR "super app financeiro")',
            '("Mercado Pago" OR "MercadoPago") ("precificação dinâmica" OR "modelos de risco" OR "fraude com IA" OR "personalização financeira")',
            '("Mercado Pago" OR "MercadoPago") (Nubank OR PagBank OR Inter OR PicPay OR "bancos tradicionais" OR concorrência)',
            '("Mercado Pago" OR "MercadoPago") ("fraudes Pix" OR "golpes digitais" OR "segurança cibernética" OR "Open Finance" OR regulação)',
        ],
        "es": [
            '("Mercado Pago" OR "MercadoPago" OR "Mercado Pago Bank" OR "Cuenta Mercado Pago") ("banco digital" OR "cuenta digital" OR "cuenta remunerada" OR depósitos OR salarios OR "principalidad financiera")',
            '("Mercado Pago" OR "MercadoPago") ("pagos digitales" OR "código QR" OR Checkout OR "Tap to Pay" OR adquirencia OR "pasarela de pagos" OR Point)',
            '("Mercado Pago" OR "MercadoPago" OR "Cuenta Negocio") ("gestión financiera pymes" OR "ERP financiero" OR "digitalización de pymes" OR "flujo de caja")',
            '("Mercado Pago" OR "MercadoPago" OR "Mercado Créditos") (préstamos OR "capital de trabajo" OR "crédito para vendedores" OR "crédito basado en datos" OR "underwriting con IA" OR "score alternativo")',
            '("Mercado Pago" OR "MercadoPago") (inversiones OR "fondos comunes" OR "embedded finance" OR "servicios financieros embebidos" OR "super app financiero")',
            '("Mercado Pago" OR "MercadoPago") ("precios dinámicos" OR "modelos de riesgo" OR "fraude con IA" OR "personalización financiera")',
            '("Mercado Pago" OR "MercadoPago") (competencia OR fintech OR "bancos tradicionales" OR Nubank OR Ualá)',
            '("Mercado Pago" OR "MercadoPago") (fraudes OR estafas OR ciberseguridad OR "Open Finance" OR regulación)',
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
