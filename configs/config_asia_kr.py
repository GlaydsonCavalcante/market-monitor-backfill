"""Configuração de monitoramento de mercado para a Coreia do Sul."""

REGIAO_NOME = "ASIA_COREIA"

MONITORAMENTOS = {
    "Reinvencao do Consumo": {
        "ko": [
            '("소비의 재발견" OR "소비자 행동" OR "소비의 미래") ("구매 여정" OR "비선형 여정" OR 옴니채널)',
            '("에이전틱 커머스" OR "Agentic Commerce" OR "쇼핑 에이전트" OR "자율 커머스" OR "AI 쇼핑" OR "에이전틱 결제")',
            '("대화형 AI" OR "대화형 커머스" OR "보이스 커머스" OR "예측 커머스" OR "초개인화")',
            '("통합 커머스" OR "임베디드 커머스" OR "무마찰 결제" OR "보이지 않는 결제" OR 피지컬)',
            '("소셜 커머스" OR "라이브 커머스" OR "크리에이터 커머스" OR "TikTok Shop" OR "WhatsApp 커머스")',
            '("몰입형 경험" OR "리테일 증강현실" OR "가상 피팅" OR "소비자 자율성")',
            '("소비자 프라이버시" OR "데이터 주권" OR "디지털 신원" OR "디지털 피로" OR "다크 패턴" OR "알고리즘 조작")',
        ]
    },
    "Nubank": {
        "ko": [
            '("Nubank" OR "Nu Holdings" OR "Nu México" OR "Nu Colombia" OR "Nubank N.A.") (수익 OR ROE OR 효율성 OR ARPAC OR 고객당매출)',
            '("Nubank" OR "Nu Holdings") (주거래화 OR 인게이지먼트 OR 대출포트폴리오 OR 연체율 OR 부실채권)',
            '("Nubank" OR "Nu Holdings") ("AI 신용평가모델" OR "동적 한도조정" OR NuFormer OR "인공지능" OR Ultravioleta OR 고액자산가)',
            '("Nubank" OR "Nu Holdings") ("Nu Business" OR NuCel OR "Nubank Shopping" OR 투자 OR 보험 OR 글로벌계좌)',
            '("Nubank" OR "Nu Holdings") (은행인가 OR "Wise 제휴" OR "오픈파이낸스" OR 멕시코진출 OR 콜롬비아진출 OR 인수합병 OR 부정결제)',
        ]
    },
    "PicPay": {
        "ko": [
            '("PicPay" OR "PicPay Bank" OR "PicPay Card" OR "PicPay Empresas") (ChatGPT OR "대화형 뱅킹" OR "오픈파이낸스" OR 전자지갑 OR Pix)',
            '("PicPay" OR "PicPay Bank") (신용대출 OR 보증한도 OR 투자 OR 보험 OR 결제단말기 OR "PicPay Tap" OR 가맹점매입 OR 운전자금)',
            '("PicPay" OR "PicPay Bank") (IPO OR 나스닥 OR 실적 OR 순이익 OR 연체율 OR 여행서비스 OR 부정결제 OR 보안)',
        ]
    },
    "Wise": {
        "ko": [
            '("Wise" OR "TransferWise" OR "Wise Platform" OR "Wise 계좌" OR "Rende+") ("해외송금" OR "국경간 결제" OR 크로스보더 결제)',
            '("Wise" OR "Wise Platform") ("글로벌 결제 인프라" OR 직접연결 OR "Banking as a Service" OR BaaS OR 은행제휴)',
            '("Wise" OR "Wise Platform") ("다중통화 계좌" OR 기준환율 OR 수수료 투명성 OR 송금속도)',
            '("Wise Business" OR "Wise 기업" OR ("Wise" AND (공급망 결제 OR 프리랜서 OR 기업 해외수금)))',
            '("Wise" OR "TransferWise") (금융라이선스 OR 글로벌확장 OR 부정거래 OR 컴플라이언스 OR 자금세탁방지 OR AML)',
        ]
    },
    "Nomad": {
        "ko": [
            '("Nomad Global" OR "Nomad Fintech" OR "Nomad Wealth" OR "Nomad 계좌") ("해외계좌" OR "달러 및 유로" OR 환전 OR 해외체크카드)',
            '("Nomad Global" OR "Nomad Fintech") ("Nomad Explorer" OR "Visa Infinite" OR "Nomad Pass" OR 리워드 OR "Nomad Lounge" OR "Nomad Trips")',
            '("Nomad Global" OR "Nomad Fintech") ("AI 여행 플래닝" OR 호텔 및 항공권 예약 OR "Nomad Chip" OR eSIM OR 여행자보험 OR 해외 캐시백)',
            '("Nomad Global" OR "Nomad Wealth") ("미국 주식 투자" OR "주식, ETF 및 REITs" OR 공항 라운지 피지컬 경험 OR 관광 제휴 OR 증권 라이선스)',
        ]
    },
    "Revolut": {
        "ko": [
            '("Revolut" OR "Revolut Bank" OR "Revolut Ultra" OR "Revolut Business" OR "Revolut Pay") ("중남미 확장" OR 브라질 OR 멕시코 OR 은행인가 OR 파킹통장)',
            '("Revolut" OR "Revolut Ultra") (글로벌 카드 OR 대출 OR 프리미엄 세그먼트 OR RevPoints OR 마일리지 OR 해외투자)',
            '("Revolut" OR "Revolut Business") ("해외주식 및 ETF" OR 가상자산 OR 스테이블코인 OR EURR OR 다중통화 계좌 OR "Revolut Pay")',
            '("Revolut Research" OR ("Revolut" AND ("인공지능" OR "금융 파운데이션 모델" OR PRAGMA)))',
            '("Revolut" OR "Revolut Bank") (컴플라이언스 OR 규제제한 OR 부정결제방지 OR 금융범죄예방 OR 스폰서십)',
        ]
    },
    "Caixa Economica Federal": {
        "ko": [
            '("Caixa Econômica Federal" OR "Caixa Economica" OR "CEF" OR "Caixa Tem" OR "Caixa Habitação") ("주택담보대출" OR "부동산 대출" OR "Minha Casa Minha Vida" OR SFH OR SBPE OR 주택금융 OR LCI OR 유동화)',
            '("Caixa Econômica Federal" OR "Caixa Economica" OR "CEF" OR "Caixa Tem") ("사회 복지" OR "포용적 금융" OR "디지털 정부" OR "생성형 AI" OR "디지털 상담" OR 자동화 OR Pix OR "오픈 파이낸스")',
            '("Caixa Econômica Federal" OR "Caixa Economica" OR "CEF" OR "Caixa Empresas" OR "Caixa Asset") ("농업 금융" OR Pronaf OR 경영효율화 OR 수익성 OR "운영 혁신" OR 기술현대화)',
        ]
    },
    "Itau": {
        "ko": [
            '("Itaú" OR "Itau" OR "Itaú Unibanco" OR "Itau Unibanco" OR "Itaú BBA" OR "iti") ("생성형 AI" OR "AI 에이전트" OR "대화형 뱅킹" OR "금융 코파일럿" OR "AI 투자" OR "초개인화" OR IAI)',
            '("Itaú" OR "Itau" OR "Itaú Private" OR "Itaú Asset" OR "Itaú Personnalité") ("자산관리" OR Wealth Management OR 자문 OR "글로벌 자산배분" OR Vanguard OR 뱅가드 OR 고액자산가)',
            '("Itaú" OR "Itau" OR "Itaú Unibanco" OR "Rede") ("임베디드 금융" OR "Banking as a Service" OR BaaS OR APIs OR "오픈 파이낸스" OR 슈퍼앱 OR 중소기업 대출 OR ESG)',
        ]
    },
    "Bradesco": {
        "ko": [
            '("Bradesco" OR "Banco Bradesco" OR "Next" OR "Ágora") (BIA OR "BIA GenAI" OR "대화형 뱅킹" OR "금융 AI 어시스턴트" OR "AI-first 뱅킹" OR "BIA Tech")',
            '("Bradesco" OR "Banco Bradesco") (지점폐쇄 OR 비용절감 OR 생산성 OR 운영혁신 OR 디지털전환 OR "Meu Bradesco" OR "오픈 파이낸스")',
            '("Bradesco Seguros" OR ("Bradesco" AND ("기후 보험" OR 파라메트릭 보험 OR 디지털 자산 OR 토큰화 OR 디지털 커스터디 OR 암호화폐)))',
        ]
    },
    "Bank of America": {
        "ko": [
            '("Bank of America" OR "BofA" OR "뱅크오브아메리카" OR "Merrill Lynch") ("디지털 뱅킹" OR "에이전틱 뱅킹" OR "Agentic AI" OR "AI 에이전트" OR "자율 금융" OR "금융 코파일럿")',
            '("BofA Institute" OR "BofA Global Research" OR ("Bank of America" AND ("소비 트렌드" OR "Z세대 경제" OR "은행의 미래" OR "미국 소비자")))',
            '("Bank of America" OR "BofA" OR "BofA Securities") ("실시간 결제" OR RTP OR 즉시결제 OR 국경간 결제 OR 임베디드 금융 OR 플랫폼 경제 OR 자산 토큰화 OR 사모대출 OR "Jio Financial")',
        ]
    },
    "JPMorgan": {
        "ko": [
            '("JPMorgan" OR "JPMorgan Chase" OR "JP모건" OR "Onyx" OR "Kinexys") (토큰화 OR 토큰화 예금 OR 디지털 자산 OR 블록체인 결제 OR 기관용 블록체인 OR 규제 준수 DeFi OR 스마트 계약)',
            '("JPMorgan" OR "JPMorgan Chase" OR "JP Morgan Payments") ("금융 인프라" OR 도매 결제 OR 프로그래머블 결제 OR 실시간 재무 OR 국경간 결제 OR 기업 결제)',
            '("JPMorgan" OR "JPMorgan Chase" OR "Chase") ("AI 뱅킹" OR 생성형 AI OR "Agentic AI" OR 임베디드 금융 OR API 뱅킹 OR BaaS OR 사모대출 OR 기관투자)',
        ]
    },
}

MERCADOS_ALVO = [
    {"gl": "KR", "hl": "ko-KR", "lang": "ko"}
]

TERMOS_EXCLUIDOS = {
    "ko": [
        "쿠폰", "할인코드", "이벤트추첨", "계좌개설방법", "단계별안내",
        "오늘의주가", "오늘의환율", "고객불만", "추천계좌순위", "스포츠",
        "축구", "연예", "운세", "요리레시피",
    ]
}

TERMOS_DESCARTE_TEXTO = {
    "ko": [
        "더 보기", "구독", "공유", "광고", "무단 전재 및 재배포 금지", "사진:", "출처:",
        "관련 기사", "편집국", "여기를 클릭", "뉴스레터", "스폰서 콘텐츠", "계좌 개설 방법",
    ]
}

PERIODO_BUSCA = "1d"
DOMINIOS_PREFERENCIAIS = []
MODELO_EMBEDDING_1024 = "BAAI/bge-m3"
SIMILARIDADE_REDUNDANCIA = 0.73
MAX_WORKERS_PARALELO = 8
TIMEOUT_REQUISICAO = 5
