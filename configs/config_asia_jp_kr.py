"""Configuração consolidada de monitoramento para Japão e Coreia do Sul."""

REGIAO_NOME = "ASIA_JP_KR"

MONITORAMENTOS = {
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
    "Mercado Pago": {
        "ja": [
            '("Mercado Pago" OR "MercadoPago" OR "Mercado Pago Bank") (デジタルバンク OR 利息付き口座 OR 預金獲得 OR 給与口座 OR メインバンク化)',
            '("Mercado Pago" OR "MercadoPago") (Pix OR デジタル決済 OR QRコード決済 OR チェックアウト OR "Tap to Pay" OR 加盟店開拓 OR 決済ゲートウェイ OR Point)',
            '("Mercado Pago" OR "MercadoPago") (中小企業財務管理 OR 中小企業向けERP OR 資金繰り管理 OR キャッシュフロー)',
            '("Mercado Pago" OR "MercadoPago" OR "Mercado Creditos") (事業者ローン OR 運転資金融資 OR データ審査 OR AI与信モデル OR オルタナティブスコア)',
            '("Mercado Pago" OR "MercadoPago") (資産運用 OR 組み込み型金融 OR 金融スーパーアプリ OR ダイナミックプライシング OR AI不正検知)',
            '("Mercado Pago" OR "MercadoPago") (Nubank OR 競合フィンテック OR 伝統的銀行 OR サイバーセキュリティ OR オープンファイナンス OR 規制対応)',
        ],
        "ko": [
            '("Mercado Pago" OR "MercadoPago" OR "Mercado Pago Bank") (인터넷전문은행 OR 디지털뱅킹 OR 고금리파킹통장 OR 예금유치 OR 급여계좌 OR 주거래은행화)',
            '("Mercado Pago" OR "MercadoPago") (Pix OR 간편결제 OR QR결제 OR 체크아웃 OR "Tap to Pay" OR 가맹점인수 OR 결제게이트웨이 OR Point)',
            '("Mercado Pago" OR "MercadoPago") (중소기업재무관리 OR 소상공인ERP OR 자금관리 OR 캐시플로우)',
            '("Mercado Pago" OR "MercadoPago" OR "Mercado Creditos") (사업자대출 OR 운전자금대출 OR 데이터기반대출 OR AI신용평가 OR 대안신용평가)',
            '("Mercado Pago" OR "MercadoPago") (투자상품 OR 임베디드파이낸스 OR 금융슈퍼앱 OR 동적가격책정 OR AI이상거래탐지)',
            '("Mercado Pago" OR "MercadoPago") (Nubank OR 핀테크경쟁 OR 시중은행 OR 금융보안 OR 오픈파이낸스 OR 금융규제)',
        ],
    },
    "Mercado Livre": {
        "ja": [
            '("Mercado Libre" OR "MercadoLibre" OR "メルカドリブレ" OR "MELI" OR "Mercado Envios" OR "Mercado Ads") (GMV OR 流通取引総額 OR "EC市場シェア" OR 出品者 OR セラー OR リテールメディア OR ライブコマース)',
            '("Mercado Libre" OR "MercadoLibre" OR "メルカドリブレ" OR "Mercado Envios") (フルフィルメント OR 配送センター OR ラストワンマイル OR 即日配送 OR 自社物流ネットワーク)',
            '("Mercado Libre" OR "MercadoLibre" OR "Mercado Creditos") (出品者ローン OR 中小企業向け運転資金 OR 組み込み型金融 OR "embedded lending")',
            '("Mercado Libre" OR "MercadoLibre" OR "Meli+") (会員プログラム OR 人工知能 OR AIショッピングエージェント OR 物流自動化 OR パーソナライゼーション)',
            '("Mercado Libre" OR "MercadoLibre" OR "メルカドリブレ") (ECプラットフォーム規制 OR アマゾン競争 OR 模倣品対策 OR 不正対策 OR 企業買収)',
        ],
        "ko": [
            '("Mercado Libre" OR "MercadoLibre" OR "메르카도리브레" OR "MELI" OR "Mercado Envios" OR "Mercado Ads") (GMV OR 총거래액 OR "이커머스 점유율" OR 셀러 OR "입점 판매자" OR 리테일미디어 OR 라이브커머스)',
            '("Mercado Libre" OR "MercadoLibre" OR "Mercado Envios") (풀필먼트 OR 물류센터 OR 라스트마일 OR 당일배송 OR 익일배송 OR 자체물류망)',
            '("Mercado Libre" OR "MercadoLibre" OR "Mercado Creditos") (판매자대출 OR "중소기업 운전자금" OR 임베디드렌딩 OR "embedded lending")',
            '("Mercado Libre" OR "MercadoLibre" OR "Meli+") (멤버십 OR 고객충성도 OR 인공지능 OR AI쇼핑에이전트 OR 물류자동화 OR 개인화추천)',
            '("Mercado Libre" OR "MercadoLibre" OR "메르카도리브레") (플랫폼규제 OR 아마존경쟁 OR 위조품차단 OR 부정거래 OR M&A)',
        ],
    },
    "Amazon": {
        "ja": [
            '("Amazon" OR "アマゾン" OR "Amazonマーケットプレイス") (マーケットプレイス OR 出品者 OR サードパーティセラー OR FBA OR フルフィルメントby Amazon)',
            '("Amazon" OR "アマゾン") (物流拠点 OR 物流ロボティクス OR 即日配送 OR ラストワンマイル OR ドローン配達 OR 倉庫自動化)',
            '("AWS" OR "アマゾンウェブサービス" OR ("Amazon" AND クラウド)) (クラウドコンピューティング OR デジタルインフラ OR 生成AI OR データセンター OR データ主権)',
            '("Amazon" OR "AWS") ("Amazon Bedrock" OR AIエージェント OR 音声アシスタント OR "Alexa+" OR Alexa OR 大規模言語モデル)',
            '("Amazon Ads" OR ("Amazon" AND (リテールメディア OR 広告収益 OR "Amazonプライム" OR Primeビデオ)))',
            '("Amazon Pharmacy" OR ("Amazon" AND (オンライン診療 OR デジタルヘルス OR フィンテック OR 組み込み金融 OR 独占禁止法 OR データ規制)))',
        ],
        "ko": [
            '("Amazon" OR "아마존" OR "Amazon Marketplace") (오픈마켓 OR 제3자판매자 OR FBA OR "풀필먼트 바이 아마존")',
            '("Amazon" OR "아마존") (물류센터 OR 물류로봇 OR 초고속배송 OR 라스트마일 OR 드론배송 OR 물류자동화)',
            '("AWS" OR "아마존웹서비스" OR ("Amazon" AND 클라우드)) (클라우드컴퓨팅 OR 디지털인프라 OR 생성형AI OR 데이터센터 OR 데이터주권)',
            '("Amazon" OR "AWS") ("Amazon Bedrock" OR AI에이전트 OR 지능형비서 OR "Alexa+" OR Alexa OR 파운데이션모델)',
            '("Amazon Ads" OR ("Amazon" AND (리테일미디어 OR 광고수익 OR "Amazon Prime" OR 아마존프라임)))',
            '("Amazon Pharmacy" OR ("Amazon" AND (원격의료 OR 디지털헬스케어 OR 핀테크 OR 반독점규제 OR 데이터프라이버시)))',
        ],
    },
    "iFood": {
        "ja": [
            '("iFood") (フードデリバリー OR クイックコマース OR 即時配達 OR ラストワンマイル OR 都市物流)',
            '("iFood" OR "iFood Mercado") (ダークストア OR デジタルコンビニ OR 食料品デリバリー)',
            '("iFood Pago" OR ("iFood" AND (レストラン向け融資 OR 売掛金早期資金化 OR エンベデッドファイナンス)))',
            '("iFood") (飲食店DX OR レストラン向けERP OR "iFood Ads" OR リテールメディア)',
            '("iFood Beneficios" OR ("iFood" AND (食事券 OR 食事手当 OR 福利厚生プラットフォーム)))',
            '("iFood") (物流AI OR 配送ルート最適化 OR 需要予測 OR ギグワーカー OR 配達員 OR プラットフォーム労働規制)',
        ],
        "ko": [
            '("iFood") (음식배달 OR 퀵커머스 OR 즉시배달 OR 라스트마일 OR 도심물류)',
            '("iFood" OR "iFood Mercado") (다크스토어 OR 디지털편의점 OR 온라인마트배달)',
            '("iFood Pago" OR ("iFood" AND (외식업자대출 OR 매출채권유동화 OR 임베디드파이낸스)))',
            '("iFood") (외식업소DX OR 식당관리ERP OR "iFood Ads" OR 리테일미디어광고)',
            '("iFood Beneficios" OR ("iFood" AND (식권서비스 OR 모바일식권 OR 임직원복지)))',
            '("iFood") (물류AI OR 스마트배차 OR 배달경로최적화 OR 긱이코노미 OR 배달라이더 OR 플랫폼노동규제)',
        ],
    },
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
    "Reconfiguracao Demografica": {
        "ja": [
            '("人口動態の変化" OR "人口減少社会" OR "少子高齢化" OR "超高齢社会" OR 長寿社会 OR "人口オーナス" OR "人口危機" OR "生産年齢人口の減少" OR "従属人口比率" OR "人口ピラミッド")',
            '("少子化" OR "出生率低下" OR "合計特殊出生率の低下" OR "異次元の少子化" OR "晩婚化" OR "未婚化" OR "不妊治療" OR "少子化対策" OR "子どもを持たない選択")',
            '("長寿経済" OR "シルバーエコノミー" OR "アクティブシニア" OR "エイジテック" OR "AgeTech" OR "抗老化医学" OR "健康寿命" OR "百寿者" OR "センテナリアン")',
            '("人手不足" OR "労働力不足" OR "労働力の高齢化" OR "リスキリング" OR "リカレント教育" OR "生涯学習" OR "定年延長" OR "高齢者雇用" OR "ケアエコノミー")',
            '("年金改革" OR "公的年金財政" OR "年金持続可能性" OR "世代間格差" OR "私的年金" OR "企業年金" OR "退職後資産取り崩し" OR "リタイアメントプランニング")',
            '("長期療養" OR "介護保険" OR "訪問介護" OR "在宅医療" OR "デジタルヘルス" OR "遠隔医療" OR "健康加齢" OR 認知症 OR アルツハイマー病)',
            '("単身世帯" OR "高齢者の一人暮らし" OR "8050問題" OR "ヤングケアラー" OR "孤独・孤立対策" OR "社会的孤立" OR "シニア向け住宅" OR "高齢者配慮型都市")',
            '("外国人労働者受け入れ" OR "高度外国人材" OR "労働移民" OR "都市集中" OR "地方過疎化")',
            '("長寿時代の資産形成" OR "資産承継" OR "事業承継" OR "生前贈与" OR "認知症と資産凍結" OR "介護保険商品" OR "トンチン年金" OR "シニア向け金融商品")',
            '("長寿の費用は誰が払うのか" OR "年金崩壊" OR "世界的な人手不足" OR "人生100年時代" OR "70歳現役社会" OR "労働力不足と自動化" OR "世代間契約の持続可能性")',
        ],
        "ko": [
            '("인구구조 변화" OR "인구학적 전환" OR "인구변화" OR "인구고령화" OR "고령사회" OR "초고령사회" OR 장수사회 OR "인구소멸" OR "인구감소" OR "인구절벽" OR "부양비" OR "인구피라미드")',
            '("저출산" OR "초저출생" OR "합계출산율 급락" OR "출산율 쇼크" OR "인구위기" OR "출산기피" OR "만혼" OR "비혼" OR 딩크족 OR 난임 OR "보조생식술" OR "출산장려정책")',
            '("장수경제" OR "실버경제" OR "실버산업" OR "액티브 시니어" OR "에이지테크" OR "AgeTech" OR "항노화치료" OR "기대수명" OR "수명연장" OR "100세시대")',
            '("인력부족" OR "노동력부족" OR "생산인구 감소" OR "고령인력" OR "재교육" OR "리스키링" OR "평생교육" OR "정년연장" OR "퇴직후재취업" OR "돌봄경제")',
            '("국민연금 개혁" OR "연금재정 건전성" OR "연금고갈" OR "세대간 연대" OR "사회안전망" OR "퇴직연금" OR "개인연금" OR "노후소득보장" OR "자산탈축적")',
            '("장기요양보험" OR "돌봄경제" OR "재가요양" OR "간병인" OR "디지털헬스케어" OR 원격의료 OR "예방의학" OR 치매 OR 알츠하이머)',
            '("1인가구 증가" OR "독거노인" OR "샌드위치세대" OR "노인고독사" OR "사회적고립" OR "시니어타운" OR "고령친화도시")',
            '("이민정책" OR "외국인근로자 유치" OR "우수인재 이민" OR "지방소멸" OR "도시집중")',
            '("노후자산관리" OR "세대간 자산이전" OR "상속 증여" OR "장수보험" OR "간병보험" OR "시니어특화금융")',
            '("장수비용은 누가 부담하나" OR "연금제도 붕괴" OR "글로벌 노동력 절벽" OR "100세 시대의 위기" OR "70세 정년" OR "생산가능인구 급감" OR "인력난과 자동화")',
        ],
    },
}

MERCADOS_ALVO = [
    {"gl": "JP", "hl": "ja-JP", "lang": "ja"},
    {"gl": "KR", "hl": "ko-KR", "lang": "ko"},
]

TERMOS_EXCLUIDOS = {
    "ja": [
        "クーポン", "割引コード", "プレゼントキャンペーン", "口座開設手順", "ステップバイステップ",
        "本日の株価推移", "本日の為替レート", "顧客の苦情", "おすすめ口座ランキング", "スポーツ",
        "サッカー", "芸能", "占い", "レシピ",
    ],
    "ko": [
        "쿠폰", "할인코드", "이벤트추첨", "계좌개설방법", "단계별안내",
        "오늘의주가", "오늘의환율", "고객불만", "추천계좌순위", "스포츠",
        "축구", "연예", "운세", "요리레시피",
    ],
}

TERMOS_DESCARTE_TEXTO = {
    "ja": [
        "続きを読む", "登録", "共有", "広告", "無断転載を禁じます", "写真：", "クレジット：",
        "関連記事", "編集部", "ここをクリック", "メルマガ登録", "スポンサー記事", "口座開設方法",
    ],
    "ko": [
        "더 보기", "구독", "공유", "광고", "무단 전재 및 재배포 금지", "사진:", "출처:",
        "관련 기사", "편집국", "여기를 클릭", "뉴스레터", "스폰서 콘텐츠", "계좌 개설 방법",
    ],
}

PERIODO_BUSCA = "1d"
DOMINIOS_PREFERENCIAIS = []
MODELO_EMBEDDING_1024 = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
SIMILARIDADE_REDUNDANCIA = 0.73
MAX_WORKERS_PARALELO = 8
TIMEOUT_REQUISICAO = 5
