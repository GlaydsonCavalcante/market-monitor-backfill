"""Configuração para China e Singapura."""

REGIAO_NOME = "ASIA_CN_SG"

MONITORAMENTOS = {
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
}

MERCADOS_ALVO = [
    {"gl": "CN", "hl": "zh-CN", "lang": "zh"},
    {"gl": "SG", "hl": "en-SG", "lang": "en"},
]

TERMOS_EXCLUIDOS = {
    "zh": [
        "优惠券",
        "折扣码",
        "抽奖",
        "开户教程",
        "手把手教学",
        "每日股价波动",
        "每日汇率收盘",
        "客户投诉",
        "最佳账户评测",
        "体育",
        "足球",
        "八卦",
        "星座",
        "菜谱",
    ],
    "en": [
        "coupon",
        "coupons",
        "promo code",
        "giveaway",
        "how to open an account",
        "daily stock movement",
        "daily exchange rate",
        "customer complaints",
        "best account ranking",
        "sports",
        "football",
        "celebrity",
        "horoscope",
    ],
}

TERMOS_DESCARTE_TEXTO = {
    "zh": [
        "阅读更多",
        "订阅",
        "分享",
        "广告",
        "版权所有",
        "图片来源：",
        "相关阅读",
        "编辑：",
        "点击这里",
        "新闻早报",
        "赞助内容",
        "如何开通账户",
    ],
    "en": [
        "read more",
        "subscribe",
        "share",
        "advertisement",
        "all rights reserved",
        "photo:",
        "credit:",
        "see also",
        "click here",
        "newsletter",
        "sponsored",
    ],
}

PERIODO_BUSCA = "1d"
DOMINIOS_PREFERENCIAIS = []
MODELO_EMBEDDING_1024 = "BAAI/bge-m3"
SIMILARIDADE_REDUNDANCIA = 0.73
MAX_WORKERS_PARALELO = 8
TIMEOUT_REQUISICAO = 5
