"""Configuração unificada de monitoramento para China e Singapura."""

REGIAO_NOME = "ASIA_CN_SG"

MONITORAMENTOS = {
    "Nubank": {
        "zh": [
            '("Nubank" OR "Nu Holdings" OR "Nu México" OR "Nu Colombia" OR "Nubank N.A.") (利润 OR ROE OR 效率 OR ARPAC OR 活跃用户收入)',
            '("Nubank" OR "Nu Holdings") (信贷组合 OR 不良贷款率 OR "AI信贷模型" OR "动态额度" OR NuFormer OR "人工智能")',
            '("Nubank" OR "Nu Holdings") (Ultravioleta OR 高净值客户 OR "Nu企业账户" OR NuCel OR "Nubank Shopping" OR 投资 OR 保险)',
            '("Nubank" OR "Nu Holdings") ("全球账户" OR "Wise合作" OR "开放银行" OR 银行牌照 OR 墨西哥扩张 OR 哥伦比亚扩张 OR 收购 OR 欺诈防范)',
        ],
        "en": [
            '("Nubank" OR "Nu Holdings" OR "Nu México" OR "Nu Colombia") (earnings OR profit OR ROE OR ARPAC OR "credit portfolio" OR NPL)',
            '("Nubank" OR "Nu Holdings") ("AI credit models" OR NuFormer OR "artificial intelligence" OR Ultravioleta OR "high income")',
            '("Nubank" OR "Nu Holdings") ("Nu Business" OR NuCel OR "global account" OR "Wise partnership" OR "banking license" OR expansion OR fraud)',
        ],
    },
    "PicPay": {
        "zh": [
            '("PicPay" OR "PicPay Bank" OR "PicPay Card" OR "PicPay Empresas") (ChatGPT OR "对话式银行" OR "开放金融" OR "数字钱包" OR Pix)',
            '("PicPay" OR "PicPay Bank") (信贷 OR "薪资贷款" OR 投资 OR 保险 OR POS机 OR "PicPay Tap" OR 收单业务 OR 营运资金)',
            '("PicPay" OR "PicPay Bank") (IPO OR 纳斯达克 OR 业绩 OR 利润 OR 不良贷款 OR 旅游服务 OR 欺诈安全)',
        ],
        "en": [
            '("PicPay" OR "PicPay Bank" OR "PicPay Empresas") (ChatGPT OR "conversational banking" OR "Open Finance" OR "digital wallet" OR Pix)',
            '("PicPay" OR "PicPay Bank") (loans OR POS OR "PicPay Tap" OR acquiring OR IPO OR Nasdaq OR earnings OR fraud)',
        ],
    },
    "Wise": {
        "zh": [
            '("Wise" OR "TransferWise" OR "Wise Platform" OR "Wise账户" OR "Rende+") ("跨境支付" OR "国际汇款" OR "全球支付基础设施" OR "直接直连")',
            '("Wise" OR "Wise Platform") ("BaaS金融即服务" OR 银行合作 OR "多币种账户" OR "商业汇率" OR "费率透明度" OR 转账速度)',
            '("Wise Business" OR "Wise企业版" OR ("Wise" AND (供应商付款 OR 自由职业者 OR B2B跨境收款)))',
            '("Wise" OR "TransferWise") (金融牌照 OR "全球扩张" OR 欺诈防范 OR 合规 OR 反洗钱 OR AML)',
        ],
        "en": [
            '("Wise" OR "TransferWise" OR "Wise Platform" OR "Wise Business") ("cross-border payments" OR "international remittances" OR Singapore OR "multi-currency account")',
            '("Wise" OR "Wise Platform") ("Banking as a Service" OR BaaS OR "bank partnerships" OR "mid-market rate" OR "transfer speed")',
            '("Wise Business" OR ("Wise" AND ("supplier payments" OR freelancers OR "enterprise cross-border")))',
            '("Wise" OR "TransferWise") (licensing OR "geographical expansion" OR fraud OR compliance OR AML OR "anti-money laundering")',
        ],
    },
    "Nomad": {
        "zh": [
            '("Nomad Global" OR "Nomad Fintech" OR "Nomad Wealth" OR "Nomad账户") ("国际账户" OR "美元与欧元" OR 外汇兑换 OR "国际卡")',
            '("Nomad Global" OR "Nomad Fintech") ("Nomad Explorer" OR "Visa Infinite" OR "Nomad Pass" OR 贵宾厅 OR "Nomad Lounge" OR "Nomad Trips")',
            '("Nomad Global" OR "Nomad Fintech") ("AI旅行规划" OR 酒店机票预订 OR "Nomad Chip" OR eSIM OR 旅行保险 OR 国际返现)',
            '("Nomad Global" OR "Nomad Wealth") ("美股投资" OR "股票、ETF与REITs" OR 机场物理体验 OR 旅游合作 OR 牌照 OR 券商)',
        ],
        "en": [
            '("Nomad Global" OR "Nomad Fintech" OR "Nomad Wealth") ("global account" OR FX OR "international card" OR "Nomad Explorer")',
            '("Nomad Global" OR "Nomad Fintech") ("Nomad Pass" OR "Nomad Lounge" OR "Nomad Trips" OR "AI travel planning" OR eSIM OR "travel insurance")',
            '("Nomad Global" OR "Nomad Wealth") ("US investments" OR "stocks, ETFs and REITs" OR lifestyle OR licensing OR brokerage)',
        ],
    },
    "Revolut": {
        "zh": [
            '("Revolut" OR "Revolut Bank" OR "Revolut Ultra" OR "Revolut Business" OR "Revolut Pay") ("拉美扩张" OR 巴西 OR 墨西哥 OR 银行牌照 OR 计息账户)',
            '("Revolut" OR "Revolut Ultra") (全球卡 OR 贷款 OR 高端客群 OR RevPoints OR 里程积分 OR "国际投资")',
            '("Revolut" OR "Revolut Business") ("股票与ETF" OR 加密货币 OR 稳定币 OR EURR OR "多币种账户" OR "Revolut Pay")',
            '("Revolut Research" OR ("Revolut" AND ("人工智能" OR "金融基础大模型" OR PRAGMA)))',
            '("Revolut" OR "Revolut Bank") (合规审查 OR 监管限制 OR 欺诈防范 OR "打击金融犯罪" OR 赞助合作)',
        ],
        "en": [
            '("Revolut" OR "Revolut Bank" OR "Revolut Ultra" OR "Revolut Business" OR "Revolut Pay") ("Latin America expansion" OR Singapore OR "banking license" OR RevPoints)',
            '("Revolut" OR "Revolut Business") ("international investments" OR crypto OR stablecoins OR EURR OR "multi-currency account")',
            '("Revolut Research" OR ("Revolut" AND ("artificial intelligence" OR "foundation models" OR PRAGMA)))',
            '("Revolut" OR "Revolut Bank") (compliance OR "regulatory restrictions" OR fraud OR "financial crime prevention")',
        ],
    },
    "Mercado Pago": {
        "zh": [
            '("Mercado Pago" OR "MercadoPago" OR "Mercado Pago Bank") (数字银行 OR 计息账户 OR 存款吸收 OR 工资账户 OR 主银行关系)',
            '("Mercado Pago" OR "MercadoPago") (Pix OR 数字支付 OR 二维码支付 OR Checkout OR "Tap to Pay" OR 收单业务 OR 支付网关 OR Point)',
            '("Mercado Pago" OR "MercadoPago") (中小企业财务管理 OR 企业ERP OR 中小企业数字化 OR 现金流管理)',
            '("Mercado Pago" OR "MercadoPago" OR "Mercado Creditos") (商户贷款 OR 营运资金贷款 OR 数据信贷 OR AI风控审批 OR 替代信贷评分)',
            '("Mercado Pago" OR "MercadoPago") (理财产品 OR 嵌入式金融 OR 金融超级应用 OR 动态定价 OR AI反欺诈)',
            '("Mercado Pago" OR "MercadoPago") (Nubank OR 传统银行 OR 竞争格局 OR 网络安全 OR 开放金融 OR 央行合规)',
        ],
        "en": [
            '("Mercado Pago" OR "MercadoPago" OR "Mercado Pago Bank") ("digital bank" OR deposits OR "merchant acquiring" OR "payment gateway")',
            '("Mercado Pago" OR "MercadoPago" OR "Mercado Creditos") ("SME lending" OR "working capital" OR "AI underwriting" OR "alternative score")',
            '("Mercado Pago" OR "MercadoPago") ("embedded finance" OR "financial super app" OR "AI fraud prevention" OR Nubank OR competition)',
        ],
    },
    "Mercado Livre": {
        "zh": [
            '("Mercado Libre" OR "MercadoLibre" OR "美客多" OR "MELI" OR "Mercado Envios" OR "Mercado Ads") (GMV OR "商品交易总额" OR 电商市场份额 OR 卖家 OR "第三方卖家" OR 零售媒体 OR 直播带货)',
            '("Mercado Libre" OR "MercadoLibre" OR "美客多" OR "Mercado Envios") (Fulfillment OR 履约仓 OR 物流配送中心 OR 最后一公里 OR 当日达 OR 自建物流网络)',
            '("Mercado Libre" OR "MercadoLibre" OR "美客多" OR "Mercado Creditos") (卖家信贷 OR 中小企业营运资金 OR 嵌入式信贷 OR "embedded lending")',
            '("Mercado Libre" OR "MercadoLibre" OR "Meli+") (会员体系 OR 客户忠诚度 OR 人工智能 OR AI购物代理 OR 物流自动化 OR 个性化推荐)',
            '("Mercado Libre" OR "MercadoLibre" OR "美客多") (电商监管 OR 亚马逊竞争 OR 跨境税收 OR 知识产权侵权 OR 假冒商品 OR 欺诈防范)',
        ],
        "en": [
            '("Mercado Libre" OR "MercadoLibre" OR "MELI") (GMV OR "e-commerce market share" OR sellers OR "retail media" OR fulfillment) Singapore',
            '("Mercado Libre" OR "MercadoLibre" OR "Mercado Envios") ("last mile delivery" OR "logistics network" OR "same-day delivery")',
            '("Mercado Libre" OR "MercadoLibre" OR "Mercado Creditos") ("merchant lending" OR "working capital" OR "embedded lending")',
            '("Mercado Libre" OR "MercadoLibre") ("artificial intelligence" OR "AI agents" OR "marketplace regulation" OR "Amazon competition")',
        ],
    },
    "Amazon": {
        "zh": [
            '("亚马逊" OR "Amazon" OR "Amazon Marketplace") (电商平台 OR 第三方卖家 OR FBA OR 亚马逊物流)',
            '("亚马逊" OR "Amazon") (运营中心 OR 物流机器人 OR 极速配送 OR 最后一公里 OR 无人机送货 OR 仓储自动化)',
            '("AWS" OR "亚马逊云科技" OR "Amazon Web Services") (云计算 OR 数字基础设施 OR 生成式AI OR 数据中心 OR 数据主权)',
            '("亚马逊" OR "AWS") ("Amazon Bedrock" OR AI智能体 OR 智能助手 OR "Alexa+" OR Alexa OR 大语言模型)',
            '("Amazon Ads" OR ("亚马逊" AND (零售媒体 OR 广告变现 OR "Amazon Prime" OR Prime会员)))',
            '("亚马逊" OR "Amazon") ("Amazon Pharmacy" OR 远程医疗 OR 数字医疗 OR 金融科技 OR 反垄断诉讼 OR 数据合规)',
        ],
        "en": [
            '("Amazon" OR "Amazon Marketplace") (marketplace OR "third-party sellers" OR FBA OR "fulfillment robotics")',
            '("AWS" OR "Amazon Web Services") ("cloud infrastructure" OR "Amazon Bedrock" OR "data sovereignty" OR "generative AI")',
            '("Amazon Ads" OR ("Amazon" AND ("retail media" OR "Amazon Prime" OR telehealth OR antitrust OR regulation)))',
        ],
    },
    "iFood": {
        "zh": [
            '("iFood") (外卖配送 OR 即时零售 OR "quick commerce" OR 极速达 OR 最后一公里 OR 城市即时物流)',
            '("iFood" OR "iFood Mercado") (前置仓 OR "dark stores" OR 线上生鲜配送 OR 商超即时达)',
            '("iFood Pago" OR "Conta Digital iFood" OR ("iFood" AND (餐饮商户贷款 OR 应收账款融资 OR 嵌入式金融)))',
            '("iFood") (餐厅数字化转型 OR 餐饮ERP管理 OR "iFood Ads" OR 零售媒体广告)',
            '("iFood Beneficios" OR ("iFood" AND (企业用餐福利 OR 员工弹性福利)))',
            '("iFood") (物流AI算法 OR 智能路径规划 OR 需求预测 OR 零工经济 OR 骑手权益保障 OR 平台用工监管)',
        ],
        "en": [
            '("iFood") (delivery OR "quick commerce" OR "instant delivery" OR "dark stores" OR "online grocery")',
            '("iFood Pago" OR ("iFood" AND ("restaurant financing" OR "embedded finance" OR "retail media" OR "flexible benefits")))',
            '("iFood") ("logistics AI" OR "smart routing" OR "gig economy" OR "delivery riders" OR "labor regulation")',
        ],
    },
    "Reinvencao do Consumo": {
        "zh": [
            '("消费重塑" OR "消费者行为" OR "未来消费") ("购物旅程" OR "全渠道" OR "即时零售" OR "非线性消费")',
            '("智能体电商" OR "Agentic Commerce" OR "购物智能体" OR "AI购物" OR "自主商业" OR "代理支付")',
            '("对话式AI" OR "对话式商务" OR "语音电商" OR "预测性消费" OR "超个性化")',
            '("统一商业" OR "嵌入式商业" OR "无感支付" OR "隐形支付" OR "实时推荐")',
            '("社交电商" OR "直播带货" OR "创作者电商" OR "TikTok Shop" OR "微信电商" OR "WhatsApp商务")',
            '("沉浸式体验" OR "零售增强现实" OR "虚拟试穿" OR "消费者自主权")',
            '("消费者隐私" OR "数据主权" OR "数字身份" OR "数字疲劳" OR "暗黑模式" OR "算法操纵" OR "人工客服温度")',
        ],
        "en": [
            '("future of consumption" OR "consumer behavior" OR "customer journey") ("agentic commerce" OR "shopping agents" OR "autonomous commerce") Singapore',
            '("conversational AI" OR "conversational commerce" OR "hyperpersonalization" OR "frictionless commerce" OR "invisible payments")',
            '("social commerce" OR "live shopping" OR "creator commerce" OR "TikTok Shop" OR "virtual try-on" OR "immersive experiences")',
            '("data sovereignty" OR "digital identity" OR "digital fatigue" OR "dark patterns" OR "humanized customer service")',
        ],
    },
    "Reconfiguracao Demografica": {
        "zh": [
            '("人口结构转型" OR "人口老龄化" OR "人口老龄化危机" OR "老龄化社会" OR "超老龄社会" OR 长寿时代 OR "人口悬崖" OR "人口负增长" OR "人口红利" OR "人口抚养比" OR "人口金字塔")',
            '("出生率下滑" OR "低生育率陷阱" OR "生育率崩塌" OR "少子化" OR "少子老龄化" OR "婚育推迟" OR "丁克家庭" OR 辅助生殖 OR "鼓励生育政策")',
            '("长寿经济" OR "银发经济" OR "健康老龄化" OR "老年产业" OR "AgeTech" OR "养老科技" OR "抗衰老医学" OR "细胞年轻化" OR 百岁老人)',
            '("劳动力短缺" OR "劳动人口老龄化" OR "技能重塑" OR "终身学习" OR "延迟退休" OR "退休后再就业" OR "多代同堂工作场所" OR "照护经济")',
            '("养老金制度改革" OR "养老金缺口" OR "养老金可持续性" OR "养老储备" OR "世代契约" OR "商业养老保险" OR "个人养老金制度" OR "退休资产去积累")',
            '("长期照护保险" OR "长期护理" OR "居家养老服务" OR "数字医疗" OR "远程健康监测" OR 智慧养老 OR 适老化改造 OR 慢性病管理 OR 阿尔茨海默病)',
            '("独居群体" OR "一人户家庭" OR "空巢老人" OR "三明治一代" OR "老年孤独感" OR "适老型城市" OR "养老社区")',
            '("长寿金融规划" OR "财富代际传承" OR "家族信托" OR "遗产规划" OR "长寿风险保险" OR "养老投资理财" OR "跨代财富管理" OR "银发金融市场")',
            '("谁来为长寿买单" OR "养老金体系崩溃" OR "全球劳动力枯竭" OR "百岁人生规划" OR "70岁退休" OR "劳动力萎缩与自动化" OR "移民与人口危机")',
        ],
        "en": [
            '("demographic transition" OR "population aging" OR "super-aged society" OR "demographic cliff" OR "dependency ratio") (China OR Singapore OR Asia)',
            '("falling fertility" OR "declining birth rate" OR "pro-natalist policies" OR "silver economy" OR "AgeTech" OR "longevity medicine")',
            '("labor shortage" OR "aging workforce" OR "delayed retirement" OR "pension reform" OR "pension sustainability" OR "long-term care")',
            '("wealth transfer" OR "longevity financial planning" OR "age-friendly cities" OR "senior living")',
        ],
    },
}

MERCADOS_ALVO = [
    {"gl": "CN", "hl": "zh-CN", "lang": "zh"},
    {"gl": "SG", "hl": "en-SG", "lang": "en"},
]

TERMOS_EXCLUIDOS = {
    "zh": [
        "优惠券", "折扣码", "抽奖", "开户教程", "手把手教学", "每日股价波动",
        "每日汇率收盘", "客户投诉", "最佳账户评测", "体育", "足球", "八卦", "星座", "菜谱",
    ],
    "en": [
        "coupon", "coupons", "promo code", "giveaway", "how to open an account",
        "daily stock movement", "daily exchange rate", "customer complaints",
        "best account ranking", "sports", "football", "celebrity", "horoscope",
    ],
}

TERMOS_DESCARTE_TEXTO = {
    "zh": [
        "阅读更多", "订阅", "分享", "广告", "版权所有", "图片来源：",
        "相关阅读", "编辑：", "点击这里", "新闻早报", "赞助内容", "如何开通账户",
    ],
    "en": [
        "read more", "subscribe", "share", "advertisement", "all rights reserved",
        "photo:", "credit:", "see also", "click here", "newsletter", "sponsored",
    ],
}

PERIODO_BUSCA = "1d"
DOMINIOS_PREFERENCIAIS = []
MODELO_EMBEDDING_1024 = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
SIMILARIDADE_REDUNDANCIA = 0.73
MAX_WORKERS_PARALELO = 8
TIMEOUT_REQUISICAO = 5
