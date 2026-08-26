"""Configuração para Japão e Coreia do Sul."""

REGIAO_NOME = "ASIA_JP_KR"

MONITORAMENTOS = {
    "Reinvencao do Consumo": {
        "ja": [
            '("消費の再発明" OR "消費者行動" OR "消費の未来") ("購買ジャーニー" OR "非線形ジャーニー" OR オムニチャネル)',
            '("エージェンティックコマース" OR "Agentic Commerce" OR "購買エージェント" OR "自律型コマース" OR "AIショッピング" OR "エージェント決済")',
            '("対話型AI" OR "カンバセーショナルコマース" OR "音声コマース" OR "予測型コマース" OR "ハイパーパーソナライゼーション")',
            '("ユニファイドコマース" OR "埋め込み型コマース" OR "フリクションレスコマース" OR "インビジブル決済" OR フィジカル)',
            '("ソーシャルコマース" OR "ライブコマース" OR "クリエイターコマース" OR "TikTok Shop" OR "WhatsAppコマース")',
            '("没入型体験" OR "小売AR" OR "バーチャル試着" OR "消費者の自律性")',
            '("プライバシー保護" OR "データ主権" OR "デジタルアイデンティティ" OR "デジタル疲労" OR "ダークパターン" OR "アルゴリズム操作")',
        ],
        "ko": [
            '("소비의 재발견" OR "소비자 행동" OR "소비의 미래") ("구매 여정" OR "비선형 여정" OR 옴니채널)',
            '("에이전틱 커머스" OR "Agentic Commerce" OR "쇼핑 에이전트" OR "자율 커머스" OR "AI 쇼핑" OR "에이전틱 결제")',
            '("대화형 AI" OR "대화형 커머스" OR "보이스 커머스" OR "예측 커머스" OR "초개인화")',
            '("통합 커머스" OR "임베디드 커머스" OR "무마찰 결제" OR "보이지 않는 결제" OR 피지컬)',
            '("소셜 커머스" OR "라이브 커머스" OR "크리에이터 커머스" OR "TikTok Shop" OR "WhatsApp 커머스")',
            '("몰입형 경험" OR "리테일 증강현실" OR "가상 피팅" OR "소비자 자율성")',
            '("소비자 프라이버시" OR "데이터 주권" OR "디지털 신원" OR "디지털 피로" OR "다크 패턴" OR "알고리즘 조작")',
        ],
    },
    "Nubank": {
        "ja": [
            '("Nubank" OR "Nu Holdings" OR "Nu México" OR "Nu Colombia" OR "Nubank N.A.") (利益 OR ROE OR 効率性 OR ARPAC OR 顧客あたり収益)',
            '("Nubank" OR "Nu Holdings") (メインバンク化 OR エンゲージメント OR 信用ポートフォリオ OR 延滞率 OR 不良債権)',
            '("Nubank" OR "Nu Holdings") ("AI与信モデル" OR "動的与信枠" OR NuFormer OR "人工知能" OR Ultravioleta OR 富裕層)',
            '("Nubank" OR "Nu Holdings") ("Nu Business" OR NuCel OR "Nubank Shopping" OR 投資 OR 保険 OR グローバル口座)',
            '("Nubank" OR "Nu Holdings") (銀行免許 OR "Wise提携" OR "Open Finance" OR メキシコ進出 OR コロンビア進出 OR 買収 OR 不正対策)',
        ],
        "ko": [
            '("Nubank" OR "Nu Holdings" OR "Nu México" OR "Nu Colombia" OR "Nubank N.A.") (수익 OR ROE OR 효율성 OR ARPAC OR 고객당매출)',
            '("Nubank" OR "Nu Holdings") (주거래화 OR 인게이지먼트 OR 대출포트폴리오 OR 연체율 OR 부실채권)',
            '("Nubank" OR "Nu Holdings") ("AI 신용평가모델" OR "동적 한도조정" OR NuFormer OR "인공지능" OR Ultravioleta OR 고액자산가)',
            '("Nubank" OR "Nu Holdings") ("Nu Business" OR NuCel OR "Nubank Shopping" OR 투자 OR 보험 OR 글로벌계좌)',
            '("Nubank" OR "Nu Holdings") (은행인가 OR "Wise 제휴" OR "오픈파이낸스" OR 멕시코진출 OR 콜롬비아진출 OR 인수합병 OR 부정결제)',
        ],
    },
    "PicPay": {
        "ja": [
            '("PicPay" OR "PicPay Bank" OR "PicPay Card" OR "PicPay Empresas") (ChatGPT OR "対話型バンキング" OR "Open Finance" OR デジタルウォレット OR Pix)',
            '("PicPay" OR "PicPay Bank") (給与担保ローン OR 保証枠 OR 投資 OR 保険 OR 決済端末 OR "PicPay Tap" OR アクワイアリング OR 運転資金)',
            '("PicPay" OR "PicPay Bank") (IPO OR ナスダック OR 業績 OR 利益 OR 延滞 OR 旅行サービス OR 不正対策 OR セキュリティ)',
        ],
        "ko": [
            '("PicPay" OR "PicPay Bank" OR "PicPay Card" OR "PicPay Empresas") (ChatGPT OR "대화형 뱅킹" OR "오픈파이낸스" OR 전자지갑 OR Pix)',
            '("PicPay" OR "PicPay Bank") (신용대출 OR 보증한도 OR 투자 OR 보험 OR 결제단말기 OR "PicPay Tap" OR 가맹점매입 OR 운전자금)',
            '("PicPay" OR "PicPay Bank") (IPO OR 나스닥 OR 실적 OR 순이익 OR 연체율 OR 여행서비스 OR 부정결제 OR 보안)',
        ],
    },
    "Wise": {
        "ja": [
            '("Wise" OR "TransferWise" OR "Wise Platform" OR "Wise口座" OR "Rende+") ("海外送金" OR "国境間決済" OR クロスボーダー決済)',
            '("Wise" OR "Wise Platform") ("グローバル決済インフラ" OR 直接接続 OR "Banking as a Service" OR BaaS OR 銀行提携)',
            '("Wise" OR "Wise Platform") ("マルチカレンシー口座" OR 仲値レート OR 手数料の透明性 OR 送金速度)',
            '("Wise Business" OR "Wise法人" OR ("Wise" AND (サプライヤー支払い OR フリーランス OR 法人送金)))',
            '("Wise" OR "TransferWise") (ライセンス OR 地理的拡大 OR 不正対策 OR コンプライアンス OR アンチマネーロンダリング OR AML)',
        ],
        "ko": [
            '("Wise" OR "TransferWise" OR "Wise Platform" OR "Wise 계좌" OR "Rende+") ("해외송금" OR "국경간 결제" OR 크로스보더 결제)',
            '("Wise" OR "Wise Platform") ("글로벌 결제 인프라" OR 직접연결 OR "Banking as a Service" OR BaaS OR 은행제휴)',
            '("Wise" OR "Wise Platform") ("다중통화 계좌" OR 기준환율 OR 수수료 투명성 OR 송금속도)',
            '("Wise Business" OR "Wise 기업" OR ("Wise" AND (공급망 결제 OR 프리랜서 OR 기업 해외수금)))',
            '("Wise" OR "TransferWise") (금융라이선스 OR 글로벌확장 OR 부정거래 OR 컴플라이언스 OR 자금세탁방지 OR AML)',
        ],
    },
    "Nomad": {
        "ja": [
            '("Nomad Global" OR "Nomad Fintech" OR "Nomad Wealth" OR "Nomad口座") ("国際口座" OR "ドル・ユーロ口座" OR 為替両替 OR 国際カード)',
            '("Nomad Global" OR "Nomad Fintech") ("Nomad Explorer" OR "Visa Infinite" OR "Nomad Pass" OR 特典 OR "Nomad Lounge" OR "Nomad Trips")',
            '("Nomad Global" OR "Nomad Fintech") ("AI旅行プランニング" OR ホテル・航空券予約 OR "Nomad Chip" OR eSIM OR 海外旅行保険 OR キャッシュバック)',
            '("Nomad Global" OR "Nomad Wealth") ("米国投資" OR "株式・ETF・REIT" OR 空港ラウンジ体験 OR 観光提携 OR 証券ライセンス)',
        ],
        "ko": [
            '("Nomad Global" OR "Nomad Fintech" OR "Nomad Wealth" OR "Nomad 계좌") ("해외계좌" OR "달러 및 유로" OR 환전 OR 해외체크카드)',
            '("Nomad Global" OR "Nomad Fintech") ("Nomad Explorer" OR "Visa Infinite" OR "Nomad Pass" OR 리워드 OR "Nomad Lounge" OR "Nomad Trips")',
            '("Nomad Global" OR "Nomad Fintech") ("AI 여행 플래닝" OR 호텔 및 항공권 예약 OR "Nomad Chip" OR eSIM OR 여행자보험 OR 해외 캐시백)',
            '("Nomad Global" OR "Nomad Wealth") ("미국 주식 투자" OR "주식, ETF 및 REITs" OR 공항 라운지 피지컬 경험 OR 관광 제휴 OR 증권 라이선스)',
        ],
    },
    "Revolut": {
        "ja": [
            '("Revolut" OR "Revolut Bank" OR "Revolut Ultra" OR "Revolut Business" OR "Revolut Pay") ("中南米進出" OR ブラジル OR メキシコ OR 銀行免許 OR 利息付き口座)',
            '("Revolut" OR "Revolut Ultra") (グローバルカード OR 融資 OR プレミアム層 OR RevPoints OR マイル特典 OR 国際投資)',
            '("Revolut" OR "Revolut Business") ("株式およびETF" OR 暗号資産 OR ステーブルコイン OR EURR OR マルチカレンシー口座 OR "Revolut Pay")',
            '("Revolut Research" OR ("Revolut" AND ("人工知能" OR "金融基盤モデル" OR PRAGMA)))',
            '("Revolut" OR "Revolut Bank") (コンプライアンス OR 規制制約 OR 不正対策 OR 金融犯罪防止 OR スポンサーシップ)',
        ],
        "ko": [
            '("Revolut" OR "Revolut Bank" OR "Revolut Ultra" OR "Revolut Business" OR "Revolut Pay") ("중남미 확장" OR 브라질 OR 멕시코 OR 은행인가 OR 파킹통장)',
            '("Revolut" OR "Revolut Ultra") (글로벌 카드 OR 대출 OR 프리미엄 세그먼트 OR RevPoints OR 마일리지 OR 해외투자)',
            '("Revolut" OR "Revolut Business") ("해외주식 및 ETF" OR 가상자산 OR 스테이블코인 OR EURR OR 다중통화 계좌 OR "Revolut Pay")',
            '("Revolut Research" OR ("Revolut" AND ("인공지능" OR "금융 파운데이션 모델" OR PRAGMA)))',
            '("Revolut" OR "Revolut Bank") (컴플라이언스 OR 규제제한 OR 부정결제방지 OR 금융범죄예방 OR 스폰서십)',
        ],
    },
}

MERCADOS_ALVO = [
    {"gl": "JP", "hl": "ja-JP", "lang": "ja"},
    {"gl": "KR", "hl": "ko-KR", "lang": "ko"},
]

TERMOS_EXCLUIDOS = {
    "ja": [
        "クーポン",
        "割引コード",
        "プレゼントキャンペーン",
        "口座開設手順",
        "ステップバイステップ",
        "本日の株価推移",
        "本日の為替レート",
        "顧客の苦情",
        "おすすめ口座ランキング",
        "スポーツ",
        "サッカー",
        "芸能",
        "占い",
        "レシピ",
    ],
    "ko": [
        "쿠폰",
        "할인코드",
        "이벤트추첨",
        "계좌개설방법",
        "단계별안내",
        "오늘의주가",
        "오늘의환율",
        "고객불만",
        "추천계좌순위",
        "스포츠",
        "축구",
        "연예",
        "운세",
        "요리레시피",
    ],
}

TERMOS_DESCARTE_TEXTO = {
    "ja": [
        "続きを読む",
        "登録",
        "共有",
        "広告",
        "無断転載を禁じます",
        "写真：",
        "クレジット：",
        "関連記事",
        "編集部",
        "ここをクリック",
        "メルマガ登録",
        "スポンサー記事",
        "口座開設方法",
    ],
    "ko": [
        "더 보기",
        "구독",
        "공유",
        "광고",
        "무단 전재 및 재배포 금지",
        "사진:",
        "출처:",
        "관련 기사",
        "편집국",
        "여기를 클릭",
        "뉴스레터",
        "스폰서 콘텐츠",
        "계좌 개설 방법",
    ],
}

PERIODO_BUSCA = "1d"
DOMINIOS_PREFERENCIAIS = []
MODELO_EMBEDDING_1024 = "BAAI/bge-m3"
SIMILARIDADE_REDUNDANCIA = 0.73
MAX_WORKERS_PARALELO = 8
TIMEOUT_REQUISICAO = 5
