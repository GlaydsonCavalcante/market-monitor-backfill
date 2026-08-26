"""Configuração para Oriente Médio, África e Índia."""

REGIAO_NOME = "ORIENTE_MEDIO_AFRICA_INDIA"

MONITORAMENTOS = {
    "Reinvencao do Consumo": {
        "ar": [
            '("إعادة ابتكار الاستهلاك" OR "سلوك المستهلك" OR "مستقبل الاستهلاك") ("رحلة الشراء" OR "الرحلة غير الخطية" OR "التجارة متعددة القنوات")',
            '("التجارة الوكيلة" OR "Agentic Commerce" OR "وكلاء التسوق" OR "التجارة المستقلة" OR "AI shopping" OR "المدفوعات الوكيلة")',
            '("الذكاء الاصطناعي التحادثي" OR "التجارة التحادثية" OR "التجارة الصوتية" OR "الاستهلاك الاستباقي" OR "التجارة التنبؤية")',
            '("التخصيص الفائق" OR "التوصية في الوقت الفعلي" OR "التجارة الواعية بالسياق" OR "العرض الأفضل التالي")',
            '("التجارة الموحدة" OR "التجارة المضمنة" OR "التجارة السلسة" OR "المدفوعات غير المرئية" OR الفيجيتال)',
            '("التجارة الاجتماعية" OR "البث المباشر للتسوق" OR "تجارة منشئي المحتوى" OR "TikTok Shop" OR "تجارة واتساب")',
            '("تجارب غامرة" OR "الواقع المعزز في التجزئة" OR "القياس الافتراضي" OR "استقلالية المستهلك")',
            '("خصوصية المستهلك" OR "سيادة البيانات" OR "الهوية الرقمية" OR "الإرهاق الرقمي" OR "أنماط مظلمة" OR "التلاعب الخوارزمي" OR "إضفاء الطابع الإنساني على الخدمة")',
        ],
        "en": [
            '("future of consumption" OR "consumer behavior" OR "customer journey") ("agentic commerce" OR "shopping agents" OR "autonomous commerce") (UAE OR "Saudi Arabia" OR Africa OR India)',
            '("conversational AI" OR "conversational commerce" OR "voice commerce" OR "anticipatory consumption" OR "predictive commerce")',
            '("hyperpersonalization" OR "context-aware commerce" OR "unified commerce" OR "frictionless commerce" OR "invisible payments")',
            '("social commerce" OR "live shopping" OR "creator commerce" OR "TikTok Shop" OR "WhatsApp commerce")',
            '("immersive experiences" OR "retail AR" OR "virtual try-on" OR "data sovereignty" OR "digital identity" OR "dark patterns" OR "humanized service")',
        ],
        "hi": [
            '("उपभोक्ता व्यवहार" OR "उपभोग का भविष्य" OR "ग्राहक यात्रा") ("एजेंटिक कॉमर्स" OR "Agentic Commerce" OR "शॉपिंग एजेंट्स" OR "AI शॉपिंग")',
            '("संवादात्मक AI" OR "कन्वर्सेशनल कॉमर्स" OR "हाइपर-पर्सनलाइजेशन" OR "फ्रिक्शनलेस कॉमर्स" OR "अदृश्य भुगतान")',
            '("सोशल कॉमर्स" OR "लाइव शॉपिंग" OR "TikTok Shop" OR "WhatsApp कॉमर्स" OR "वर्चुअल ट्राई-ऑन" OR "डेटा संप्रभुता" OR "डिजिटल पहचान" OR "डार्क पैटर्न्स")',
        ],
    },
    "Nubank": {
        "ar": [
            '("Nubank" OR "Nu Holdings" OR "Nu México" OR "Nu Colombia" OR "Nubank N.A.") (أرباح OR عائد حقوق الملكية OR كفاءة OR ARPAC OR الإيرادات لكل عميل)',
            '("Nubank" OR "Nu Holdings") (المحفظة الائتمانية OR القروض المتعثرة OR "نماذج الائتمان بالذكاء الاصطناعي" OR NuFormer OR "الذكاء الاصطناعي")',
            '("Nubank" OR "Nu Holdings") (Ultravioleta OR أصحاب الثروات OR "Nu للشركات" OR NuCel OR سوق نوبانك OR استثمارات OR تأمين)',
            '("Nubank" OR "Nu Holdings") ("الحساب العالمي" OR "شراكة Wise" OR "الخدمات المصرفية المفتوحة" OR رخصة مصرفية OR التوسع في المكسيك OR استحواذ OR احتيال)',
        ],
        "en": [
            '("Nubank" OR "Nu Holdings" OR "Nu México" OR "Nu Colombia") (earnings OR profit OR ROE OR ARPAC OR "credit portfolio" OR NPL)',
            '("Nubank" OR "Nu Holdings") ("AI credit models" OR NuFormer OR "artificial intelligence" OR Ultravioleta OR "mass affluent")',
            '("Nubank" OR "Nu Holdings") ("Nu Business" OR "global account" OR "Wise partnership" OR "banking license" OR expansion OR acquisitions OR fraud)',
        ],
        "hi": [
            '("Nubank" OR "Nu Holdings") (कमाई OR लाभ OR ROE OR ARPAC OR "क्रेडिट पोर्टफोलियो" OR "AI क्रेडिट मॉडल" OR NuFormer OR "आर्टिफिशियल इंटेलिजेंस")',
            '("Nubank" OR "Nu Holdings") (Ultravioleta OR "Nu Business" OR "ग्लोबल अकाउंट" OR "बैंकिंग लाइसेंस" OR विस्तार OR धोखाधड़ी)',
        ],
    },
    "PicPay": {
        "ar": [
            '("PicPay" OR "PicPay Bank" OR "PicPay Card" OR "PicPay Empresas") (ChatGPT OR "المصرفية التحادثية" OR "التمويل المفتوح" OR المحفظة الرقمية OR Pix)',
            '("PicPay" OR "PicPay Bank") (قروض بضمان الراتب OR استثمارات OR تأمين OR نقاط البيع OR "PicPay Tap" OR الاستحواذ على التجار OR رأس المال العامل)',
            '("PicPay" OR "PicPay Bank") (IPO OR ناسداك OR نتائج مالية OR تعثر الائتمان OR التوسع في السفر OR أمن واحتيال)',
        ],
        "en": [
            '("PicPay" OR "PicPay Bank" OR "PicPay Empresas") (ChatGPT OR "conversational banking" OR "Open Finance" OR "digital wallet" OR Pix)',
            '("PicPay" OR "PicPay Bank") (payroll loans OR investments OR acquiring OR "PicPay Tap" OR "working capital" OR IPO OR Nasdaq OR earnings OR fraud)',
        ],
        "hi": [
            '("PicPay" OR "PicPay Bank") (ChatGPT OR "कन्वर्सेशनल बैंकिंग" OR "ओपन फाइनेंस" OR डिजिटल वॉलेट OR Pix OR आईपीओ OR नैस्डैक OR परिणाम)',
        ],
    },
    "Wise": {
        "ar": [
            '("Wise" OR "TransferWise" OR "Wise Platform" OR "حساب Wise" OR "Rende+") ("التحويلات الدولية" OR "المدفوعات عبر الحدود" OR البنية التحتية العالمية للمدفوعات)',
            '("Wise" OR "Wise Platform") ("الخدمات المصرفية كخدمة" OR BaaS OR الشراكات المصرفية OR "حساب متعدد العملات" OR سعر الصرف التجاري OR شفافية الرسوم)',
            '("Wise Business" OR "Wise للشركات" OR ("Wise" AND (مدفوعات الموردين OR المستقلين OR المدفوعات الدولية للشركات)))',
            '("Wise" OR "TransferWise") (تراخيص OR التوسع الجغرافي OR الاحتيال OR الامتثال OR مكافحة غسل الأموال OR AML)',
        ],
        "en": [
            '("Wise" OR "TransferWise" OR "Wise Platform" OR "Wise Business") ("international remittances" OR "cross-border payments" OR "global payment infrastructure")',
            '("Wise" OR "Wise Platform") ("Banking as a Service" OR BaaS OR "bank partnerships" OR "multi-currency account" OR "fee transparency" OR "transfer speed")',
            '("Wise Business" OR ("Wise" AND ("supplier payments" OR freelancers OR "enterprise cross-border")))',
            '("Wise" OR "TransferWise") (licenses OR "geographical expansion" OR fraud OR compliance OR "anti-money laundering" OR AML)',
        ],
        "hi": [
            '("Wise" OR "TransferWise" OR "Wise Platform") ("अंतरराष्ट्रीय प्रेषण" OR "सीमा पार भुगतान" OR "बहु-मुद्रा खाता" OR BaaS OR बैंक साझेदारी)',
            '("Wise Business" OR ("Wise" AND (लाइसेंस OR भौगोलिक विस्तार OR धोखाधड़ी OR अनुपालन OR मनी लॉन्ड्रिंग रोधी)))',
        ],
    },
    "Nomad": {
        "ar": [
            '("Nomad Global" OR "Nomad Fintech" OR "Nomad Wealth" OR "حساب Nomad") ("حساب دولي" OR "الدولار واليورو" OR تحويل العملات OR بطاقة دولية)',
            '("Nomad Global" OR "Nomad Fintech") ("Nomad Explorer" OR "Visa Infinite" OR "Nomad Pass" OR "Nomad Lounge" OR "Nomad Trips" OR "تخطيط السفر بالذكاء الاصطناعي")',
            '("Nomad Global" OR "Nomad Fintech") ("Nomad Chip" OR eSIM OR تأمين السفر OR الاسترداد النقدي الدولي OR "الاستثمار في أمريكا" OR "الأسهم وصناديق الاستثمار")',
            '("Nomad Wealth" OR "Nomad Fintech") (صالات المطارات OR شراكات السياحة OR التراخيص OR الوساطة المالية)',
        ],
        "en": [
            '("Nomad Global" OR "Nomad Fintech" OR "Nomad Wealth") ("global account" OR FX OR "international card" OR "Nomad Explorer" OR "Visa Infinite")',
            '("Nomad Global" OR "Nomad Fintech") ("Nomad Pass" OR "Nomad Lounge" OR "Nomad Trips" OR "AI travel planning" OR "Nomad Chip" OR eSIM OR "travel insurance")',
            '("Nomad Global" OR "Nomad Wealth") ("US investments" OR "stocks, ETFs and REITs" OR "airport lounge experience" OR lifestyle OR licensing OR brokerage)',
        ],
        "hi": [
            '("Nomad Global" OR "Nomad Fintech" OR "Nomad Wealth") ("ग्लोबल अकाउंट" OR "अंतरराष्ट्रीय कार्ड" OR "Nomad Explorer" OR "AI यात्रा योजना" OR eSIM)',
            '("Nomad Global" OR "Nomad Wealth") ("अमेरिकी निवेश" OR "स्टॉक्स, ईटीएफ और आरईआईटी" OR लाइसेंस OR ब्रोकरेज)',
        ],
    },
    "Revolut": {
        "ar": [
            '("Revolut" OR "Revolut Bank" OR "Revolut Ultra" OR "Revolut Business" OR "Revolut Pay") ("التوسع في أمريكا اللاتينية" OR الإمارات OR الهند OR رخصة مصرفية OR حساب بعائد)',
            '("Revolut" OR "Revolut Ultra") (بطاقات عالمية OR قروض OR الفئة المميزة OR RevPoints OR أميال المكافآت OR استثمارات دولية)',
            '("Revolut" OR "Revolut Business") ("الأسهم وصناديق الاستثمار" OR العملات المشفرة OR العملات المستقرة OR EURR OR حساب متعدد العملات OR "Revolut Pay")',
            '("Revolut Research" OR ("Revolut" AND ("الذكاء الاصطناعي" OR "النماذج التأسيسية المالية" OR PRAGMA)))',
            '("Revolut" OR "Revolut Bank") (الامتثال OR القيود التنظيمية OR مكافحة الاحتيال OR "منع الجرائم المالية")',
        ],
        "en": [
            '("Revolut" OR "Revolut Bank" OR "Revolut Ultra" OR "Revolut Business" OR "Revolut Pay") ("Latin America expansion" OR UAE OR India OR "banking license" OR "high yield account")',
            '("Revolut" OR "Revolut Ultra") ("global cards" OR RevPoints OR "loyalty miles" OR "international investments" OR "stocks and ETFs")',
            '("Revolut" OR "Revolut Business") ("crypto and stablecoins" OR EURR OR "multi-currency account" OR "Revolut Pay")',
            '("Revolut Research" OR ("Revolut" AND ("artificial intelligence" OR "financial foundation models" OR PRAGMA)))',
            '("Revolut" OR "Revolut Bank") (compliance OR "regulatory restrictions" OR fraud OR "financial crime prevention")',
        ],
        "hi": [
            '("Revolut" OR "Revolut Bank" OR "Revolut Ultra" OR "Revolut Business") (विस्तार OR भारत OR यूएई OR "बैंकिंग लाइसेंस" OR RevPoints OR अंतरराष्ट्रीय निवेश)',
            '("Revolut Research" OR ("Revolut" AND ("आर्टिफिशियल इंटेलिजेंस" OR PRAGMA OR क्रिप्टो OR EURR OR अनुपालन OR धोखाधड़ी)))',
        ],
    },
}

MERCADOS_ALVO = [
    {"gl": "AE", "hl": "ar", "lang": "ar"},
    {"gl": "AE", "hl": "en-AE", "lang": "en"},
    {"gl": "SA", "hl": "ar", "lang": "ar"},
    {"gl": "EG", "hl": "ar", "lang": "ar"},
    {"gl": "ZA", "hl": "en-ZA", "lang": "en"},
    {"gl": "NG", "hl": "en-NG", "lang": "en"},
    {"gl": "KE", "hl": "en-KE", "lang": "en"},
    {"gl": "IN", "hl": "en-IN", "lang": "en"},
    {"gl": "IN", "hl": "hi", "lang": "hi"},
]

TERMOS_EXCLUIDOS = {
    "ar": [
        "عروض ترويجية",
        "كوبون",
        "كوبونات",
        "خصم",
        "سحب جوائز",
        "كيفية فتح حساب",
        "خطوة بخطوة",
        "حركة الأسهم اليومية",
        "سعر الصرف اليومي",
        "شكاوى العملاء",
        "تصنيف أفضل الحسابات",
        "رياضة",
        "كرة القدم",
        "أبراج",
        "وصفات",
    ],
    "en": [
        "coupon",
        "coupons",
        "promo code",
        "discount",
        "giveaway",
        "how to open an account",
        "step by step tutorial",
        "daily stock movement",
        "daily exchange rate",
        "customer complaints",
        "best account ranking",
        "sports",
        "football",
        "cricket",
        "celebrity",
        "horoscope",
        "recipe",
    ],
    "hi": [
        "कूपन",
        "डिस्काउंट कोड",
        "खाता कैसे खोलें",
        "स्टेप बाय स्टेप",
        "दैनिक शेयर भाव",
        "दैनिक विनिमय दर",
        "ग्राहक शिकायतें",
        "सर्वश्रेष्ठ खाता रैंकिंग",
        "खेल",
        "क्रिकेट",
        "राशिफल",
        "व्यंजन विधि",
    ],
}

TERMOS_DESCARTE_TEXTO = {
    "ar": [
        "اقرأ المزيد",
        "اشترك",
        "مشاركة",
        "إعلان",
        "جميع الحقوق محفوظة",
        "مصدر الصورة:",
        "انقر هنا",
        "النشرة الإخبارية",
        "محتوى مدعوم",
        "طريقة فتح الحساب",
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
    "hi": [
        "और पढ़ें",
        "सदस्यता लें",
        "शेयर करें",
        "विज्ञापन",
        "सर्वाधिकार सुरक्षित",
        "फोटो:",
        "यहां क्लिक करें",
        "न्यूज़लेटर",
        "प्रायोजित",
    ],
}

PERIODO_BUSCA = "1d"
DOMINIOS_PREFERENCIAIS = []
MODELO_EMBEDDING_1024 = "BAAI/bge-m3"
SIMILARIDADE_REDUNDANCIA = 0.73
MAX_WORKERS_PARALELO = 8
TIMEOUT_REQUISICAO = 6
