"""Configuração unificada de monitoramento para Oriente Médio, África e Índia."""

REGIAO_NOME = "ORIENTE_MEDIO_AFRICA_INDIA"

MONITORAMENTOS = {
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
    "Mercado Pago": {
        "ar": [
            '("Mercado Pago" OR "MercadoPago" OR "Mercado Pago Bank") ("البنك الرقمي" OR "الحساب الرقمي" OR الودائع OR توطين الرواتب OR "العلاقة المصرفية الرئيسية")',
            '("Mercado Pago" OR "MercadoPago") (Pix OR "المدفوعات الرقمية" OR "رمز الاستجابة السريعة" OR Checkout OR "Tap to Pay" OR بوابات الدفع OR Point)',
            '("Mercado Pago" OR "MercadoPago") ("الإدارة المالية للشركات الصغيرة" OR "برامج تخطيط الموارد" OR التدفق النقدي)',
            '("Mercado Pago" OR "MercadoPago" OR "Mercado Creditos") ("قروض التجار" OR "رأس المال العامل" OR "تقييم الائتمان بالذكاء الاصطناعي" OR "التصنيف الائتماني البديل")',
            '("Mercado Pago" OR "MercadoPago") ("التمويل المدمج" OR "التطبيق المالي الفائق" OR "التسعير الديناميكي" OR مكافحة الاحتيال)',
            '("Mercado Pago" OR "MercadoPago") (Nubank OR المنافسة الفنتك OR الأمن السيبراني OR "الخدمات المصرفية المفتوحة")',
        ],
        "en": [
            '("Mercado Pago" OR "MercadoPago" OR "Mercado Pago Bank") ("digital banking" OR "interest-bearing accounts" OR deposits OR payroll)',
            '("Mercado Pago" OR "MercadoPago") (Pix OR "digital payments" OR "QR Code" OR Checkout OR "Tap to Pay" OR acquiring OR "payment gateway")',
            '("Mercado Pago" OR "MercadoPago" OR "Mercado Creditos") ("SME financial management" OR "merchant loans" OR "AI underwriting" OR "alternative credit score")',
            '("Mercado Pago" OR "MercadoPago") ("embedded finance" OR "financial super app" OR Nubank OR competition OR cybersecurity)',
        ],
        "hi": [
            '("Mercado Pago" OR "MercadoPago" OR "Mercado Pago Bank") ("डिजिटल बैंक" OR जमा OR वेतन खाता OR "डिजिटल भुगतान")',
            '("Mercado Pago" OR "MercadoPago") (Pix OR "क्यूआर कोड" OR चेकआउट OR "Tap to Pay" OR "पेमेंट गेटवे")',
            '("Mercado Pago" OR "MercadoPago" OR "Mercado Creditos") ("एसएमई ऋण" OR "कार्यशील पूंजी" OR "एआई अंडरराइटिंग")',
            '("Mercado Pago" OR "MercadoPago") ("एम्बेडेड फाइनेंस" OR "सुपर ऐप" OR साइबर सुरक्षा OR ओपन फाइनेंस)',
        ],
    },
    "Mercado Livre": {
        "ar": [
            '("Mercado Libre" OR "MercadoLibre" OR "MELI" OR "Mercado Envios" OR "Mercado Ads") (GMV OR "حصة التجارة الإلكترونية" OR البائعين OR "إعلانات التجزئة" OR "البث المباشر")',
            '("Mercado Libre" OR "MercadoLibre" OR "Mercado Envios") (مراكز التوزيع OR "التسليم في نفس اليوم" OR "الميل الأخير" OR "الخدمات اللوجستية")',
            '("Mercado Libre" OR "MercadoLibre" OR "Mercado Creditos") ("ائتمان البائعين" OR "رأس المال العامل للشركات الصغيرة" OR "التمويل المدمج")',
            '("Mercado Libre" OR "MercadoLibre" OR "Meli+") (برامج الولاء OR "الذكاء الاصطناعي" OR "وكلاء التسوق" OR "أتمتة اللوجستيات")',
            '("Mercado Libre" OR "MercadoLibre" OR "MELI") ("تنظيم المنصات" OR "المنافسة مع أمازون" OR الاحتيال OR البضائع المقلدة)',
        ],
        "en": [
            '("Mercado Libre" OR "MercadoLibre" OR "MELI") (GMV OR "e-commerce market share" OR sellers OR "retail media network" OR fulfillment)',
            '("Mercado Libre" OR "MercadoLibre" OR "Mercado Envios") ("distribution centers" OR "last mile" OR "same-day delivery")',
            '("Mercado Libre" OR "MercadoLibre" OR "Mercado Creditos") ("merchant credit" OR "working capital" OR "embedded lending")',
            '("Mercado Libre" OR "MercadoLibre") ("artificial intelligence" OR "AI agents" OR "Amazon competition" OR regulation)',
        ],
        "hi": [
            '("Mercado Libre" OR "MercadoLibre" OR "MELI") (GMV OR "ई-कॉमर्स मार्केट शेयर" OR विक्रेता OR "रिटेल मीडिया")',
            '("Mercado Libre" OR "MercadoLibre" OR "Mercado Envios") (फुलफिलमेंट OR "वितरण केंद्र" OR "लास्ट माइल" OR "लॉजिस्टिक्स नेटवर्क")',
            '("Mercado Libre" OR "MercadoLibre" OR "Mercado Creditos") ("मर्चेंट क्रेडिट" OR "कार्यशील पूंजी" OR "एम्बेडेड लेंडिंग")',
            '("Mercado Libre" OR "MercadoLibre") ("आर्टिफिशियल इंटेलिजेंस" OR "एआई एजेंट्स" OR अमेज़न OR विनियमन)',
        ],
    },
    "Amazon": {
        "ar": [
            '("أمازون" OR "Amazon" OR "Amazon Marketplace") (سوق إلكتروني OR بائعي الطرف الثالث OR FBA OR الشحن من قبل أمازون)',
            '("أمازون" OR "Amazon") (مراكز التنفيذ OR روبوتات اللوجستيات OR التوصيل فائق السرعة OR الميل الأخير OR طائرات الدرون)',
            '("AWS" OR "Amazon Web Services" OR ("أمازون" AND الحوسبة السحابية)) (البنية التحتية الرقمية OR الذكاء الاصطناعي التوليدي OR مراكز البيانات OR سيادة البيانات)',
            '("أمازون" OR "AWS") ("Amazon Bedrock" OR وكلاء الذكاء الاصطناعي OR "Alexa+" OR Alexa OR إعلانات التجزئة)',
            '("Amazon Prime" OR ("أمازون" AND ("Amazon Pharmacy" OR الرعاية الصحية الرقمية OR التكنولوجيا المالية OR مكافحة الاحتكار)))',
        ],
        "en": [
            '("Amazon" OR "Amazon Marketplace") (marketplace OR "third-party sellers" OR FBA OR "logistics robotics" OR "same-day delivery")',
            '("AWS" OR "Amazon Web Services" OR ("Amazon" AND cloud)) ("cloud computing" OR "data centers" OR "data sovereignty" OR "Amazon Bedrock")',
            '("Amazon Ads" OR ("Amazon" AND ("retail media" OR "Amazon Prime" OR "Amazon Pharmacy" OR telehealth OR antitrust OR regulation)))',
        ],
        "hi": [
            '("Amazon" OR "अमेज़न" OR "Amazon Marketplace") (मार्केटप्लेस OR तीसरे पक्ष के विक्रेता OR FBA OR "अमेज़न द्वारा पूर्ति")',
            '("Amazon" OR "अमेज़न") (लॉजिस्टिक्स रोबोटिक्स OR "उसी दिन डिलीवरी" OR लास्ट माइल OR ड्रोन डिलीवरी OR ऑटोमेशन)',
            '("AWS" OR "Amazon Web Services" OR ("अमेज़न" AND क्लाउड)) ("क्लाउड कंप्यूटिंग" OR "डेटा केंद्र" OR "डेटा संप्रभुता" OR "Amazon Bedrock")',
            '("Amazon Ads" OR ("अमेज़न" AND ("रिटेल मीडिया" OR "Amazon Prime" OR टेलीहेल्थ OR एकाधिकार विरोधी)))',
        ],
    },
    "iFood": {
        "ar": [
            '("iFood") (توصيل الطلبات OR التجارة السريعة OR التوصيل الفوري OR الميل الأخير OR اللوجستيات الحضرية)',
            '("iFood" OR "iFood Mercado") (المتاجر المظلمة OR توصيل البقالة عبر الإنترنت OR تمويل المطاعم OR التمويل المدمج)',
            '("iFood Ads" OR ("iFood" AND (إعلانات التجزئة OR قسائم الوجبات OR مزايا الموظفين المرنة)))',
            '("iFood") (ذكاء اصطناعي لوجستي OR التوجيه الذكي OR اقتصاد المنصات OR عمال التوصيل OR تنظيم العمل)',
        ],
        "en": [
            '("iFood") (delivery OR "quick commerce" OR "dark stores" OR "grocery delivery" OR "restaurant financing")',
            '("iFood Pago" OR ("iFood" AND ("embedded finance" OR "retail media" OR "flexible benefits" OR "meal vouchers")))',
            '("iFood") ("logistics AI" OR "smart routing" OR "gig economy" OR "delivery riders" OR "labor regulation")',
        ],
        "hi": [
            '("iFood") (डिलीवरी OR "क्विक कॉमर्स" OR "डार्क स्टोर्स" OR किराना डिलीवरी OR रेस्तरां वित्तपोषण)',
            '("iFood Pago" OR ("iFood" AND ("एम्बेडेड फाइनेंस" OR "रिटेल मीडिया" OR भोजन वाउचर)))',
            '("iFood") (लॉजिस्टिक्स एआई OR रूट ऑप्टिमाइज़ेशन OR "गिग इकॉनमी" OR डिलीवरी राइडर्स OR श्रम नियमन)',
        ],
    },
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
    "Reconfiguracao Demografica": {
        "ar": [
            '("التحول الديموغرافي" OR "التغير الديموغرافي" OR "شيخوخة السكان" OR "المجتمع المسن" OR "مجتمع المعمرين" OR طول العمر OR "الشتاء الديموغرافي" OR "انخفاض عدد السكان" OR "العائد الديموغرافي" OR "نسبة الإعالة" OR "الهرم السكاني")',
            '("انخفاض معدل المواليد" OR "تراجع الخصوبة" OR "انهيار الخصوبة" OR "الأزمة الديموغرافية" OR "تأخر سن الزواج" OR "العقم" OR "تقنيات الإنجاب المساعدة" OR "حوافز الإنجاب")',
            '("اقتصاد طول العمر" OR "اقتصاد الفئات الفضية" OR "الشيخوخة النشطة" OR "تكنولوجيا كبار السن" OR "AgeTech" OR "طب مكافحة الشيخوخة" OR متوسط العمر المتوقع)',
            '("نقص العمالة" OR "شيخوخة القوى العاملة" OR "إعادة صقل المهارات" OR "التعلم المستمر" OR "تأخير سن التقاعد" OR "بيئة عمل متعددة الأجيال" OR "اقتصاد الرعاية")',
            '("إصلاح أنظمة التقاعد" OR "استدامة المعاشات" OR "أزمة صناديق التقاعد" OR "العقد بين الأجيال" OR "الحماية الاجتماعية" OR "التأمين التقاعدي الخاص")',
            '("الرعاية طويلة الأمد" OR "اقتصاد الرعاية" OR "الرعاية المنزلية" OR "الصحة الرقمية" OR التطبيب عن بعد OR الأمراض المزمنة OR ألزهايمر)',
            '("الأسر المكونة من شخص واحد" OR "العيش المنفرد" OR "جيل الساندويتش" OR العزلة الاجتماعية OR "مدن صديقة للمسنين" OR "مجمعات كبار السن السكنية")',
            '("الهجرة الدولية" OR "هجرة الكفاءات" OR "لاجئو المناخ" OR "النمو السكاني في إفريقيا" OR "العائد الديموغرافي الإفريقي")',
            '("التخطيط المالي لمرحلة التقاعد" OR "انتقال الثروات" OR الميراث OR "تأمين رعاية المسنين" OR "صناديق التقاعد الخاصة" OR "إدارة الثروات العائلية")',
            '("من سيمول الشيخوخة" OR "انهيار أنظمة المعاشات" OR "نقص العمالة العالمي" OR "حياة المئة عام" OR "العمل حتى سن السبعين" OR "استدامة العقد بين الأجيال")',
        ],
        "en": [
            '("demographic transition" OR "population aging" OR "aging population" OR "super-aged society" OR "demographic dividend" OR "dependency ratio") (UAE OR "Saudi Arabia" OR Africa OR India)',
            '("declining birth rates" OR "falling fertility" OR "demographic crisis" OR "silver economy" OR "longevity economy" OR "AgeTech")',
            '("labor shortage" OR "workforce aging" OR "reskilling" OR "delayed retirement" OR "pension reform" OR "pension sustainability")',
            '("long-term care" OR "care economy" OR "digital health" OR "wealth transfer" OR "longevity financial planning" OR "Africa demographic boom")',
        ],
        "hi": [
            '("जनसांख्यिकीय संक्रमण" OR "जनसंख्या का वृद्ध होना" OR "बुजुर्ग समाज" OR "जनसांख्यिकीय लाभांश" OR "निर्भरता अनुपात" OR "जनसंख्या पिरामिड")',
            '("जन्म दर में कमी" OR "प्रजनन दर में गिरावट" OR "जनसांख्यिकीय संकट" OR "छोटा परिवार" OR "प्रजनन उपचार")',
            '("सिल्वर इकॉनमी" OR "दीर्घायु अर्थव्यवस्था" OR "सक्रिय बुढ़ापा" OR "एजटेक" OR "AgeTech" OR जीवन प्रत्याशा)',
            '("कार्यबल की कमी" OR "कर्मचारियों का वृद्ध होना" OR पुनर्कौशल OR "आजीवन सीखना" OR "देर से सेवानिवृत्ति" OR "केयर इकॉनमी")',
            '("पेंशन सुधार" OR "पेंशन स्थिरता" OR "पेंशन संकट" OR "अंतर-पीढ़ीगत सुरक्षा" OR "निजी पेंशन योजनाएं")',
            '("दीर्घकालिक देखभाल" OR "घरेलू स्वास्थ्य सेवा" OR "डिजिटल स्वास्थ्य" OR टेलीमेडिसिन OR डिमेंशिया OR अल्जाइमर)',
            '("एकल परिवार" OR "बुजुर्गों का अकेलापन" OR "वरिष्ठ नागरिकों के अनुकूल शहर" OR "सीनियर लिविंग सोसाइटी")',
            '("अंतर्राष्ट्रीय प्रवासन" OR "कुशल प्रवासन" OR "अफ्रीका की जनसांख्यिकी")',
            '("बुढ़ापे के लिए वित्तीय योजना" OR "धन हस्तांतरण" OR वसीयत OR "दीर्घायु बीमा" OR "वरिष्ठ वित्तीय उत्पाद")',
            '("दीर्घायु का वित्तपोषण कौन करेगा" OR "पेंशन प्रणाली संकट" OR "100 साल का जीवन" OR "70 साल तक काम" OR "श्रमिकों की कमी और स्वचालन")',
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
        "عروض ترويجية", "كوبون", "كوبونات", "خصم", "سحب جوائز", "كيفية فتح حساب",
        "خطوة بخطوة", "حركة الأسهم اليومية", "سعر الصرف اليومي", "شكاوى العملاء",
        "تصنيف أفضل الحسابات", "رياضة", "كرة القدم", "أبراج", "وصفات",
    ],
    "en": [
        "coupon", "coupons", "promo code", "discount", "giveaway", "how to open an account",
        "step by step tutorial", "daily stock movement", "daily exchange rate",
        "customer complaints", "best account ranking", "sports", "football", "cricket",
        "celebrity", "horoscope", "recipe",
    ],
    "hi": [
        "कूपन", "डिस्काउंट कोड", "खाता कैसे खोलें", "स्टेप बाय स्टेप", "दैनिक शेयर भाव",
        "दैनिक विनिमय दर", "ग्राहक शिकायतें", "सर्वश्रेष्ठ खाता रैंकिंग", "खेल",
        "क्रिकेट", "राशिफल", "व्यंजन विधि",
    ],
}

TERMOS_DESCARTE_TEXTO = {
    "ar": [
        "اقرأ المزيد", "اشترك", "مشاركة", "إعلان", "جميع الحقوق محفوظة", "مصدر الصورة:",
        "انقر هنا", "النشرة الإخبارية", "محتوى مدعوم", "طريقة فتح الحساب",
    ],
    "en": [
        "read more", "subscribe", "share", "advertisement", "all rights reserved",
        "photo:", "credit:", "see also", "click here", "newsletter", "sponsored",
    ],
    "hi": [
        "और पढ़ें", "सदस्यता लें", "शेयर करें", "विज्ञापन", "सर्वाधिकार सुरक्षित",
        "फोटो:", "यहां क्लिक करें", "न्यूज़लेटर", "प्रायोजित",
    ],
}

PERIODO_BUSCA = "1d"
DOMINIOS_PREFERENCIAIS = []
MODELO_EMBEDDING_1024 = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
SIMILARIDADE_REDUNDANCIA = 0.73
MAX_WORKERS_PARALELO = 8
TIMEOUT_REQUISICAO = 6
