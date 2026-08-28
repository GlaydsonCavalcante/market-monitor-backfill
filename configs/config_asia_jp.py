"""Configuração de monitoramento de mercado para o Japão."""

REGIAO_NOME = "ASIA_JAPAO"

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
        ]
    },
    "Nubank": {
        "ja": [
            '("Nubank" OR "Nu Holdings" OR "Nu México" OR "Nu Colombia" OR "Nubank N.A.") (利益 OR ROE OR 効率性 OR ARPAC OR 顧客あたり収益)',
            '("Nubank" OR "Nu Holdings") (メインバンク化 OR エンゲージメント OR 信用ポートフォリオ OR 延滞率 OR 不良債権)',
            '("Nubank" OR "Nu Holdings") ("AI与信モデル" OR "動的与信枠" OR NuFormer OR "人工知能" OR Ultravioleta OR 富裕層)',
            '("Nubank" OR "Nu Holdings") ("Nu Business" OR NuCel OR "Nubank Shopping" OR 投資 OR 保険 OR グローバル口座)',
            '("Nubank" OR "Nu Holdings") (銀行免許 OR "Wise提携" OR "Open Finance" OR メキシコ進出 OR コロンビア進出 OR 買収 OR 不正対策)',
        ]
    },
    "PicPay": {
        "ja": [
            '("PicPay" OR "PicPay Bank" OR "PicPay Card" OR "PicPay Empresas") (ChatGPT OR "対話型バンキング" OR "Open Finance" OR デジタルウォレット OR Pix)',
            '("PicPay" OR "PicPay Bank") (給与担保ローン OR 保証枠 OR 投資 OR 保険 OR 決済端末 OR "PicPay Tap" OR アクワイアリング OR 運転資金)',
            '("PicPay" OR "PicPay Bank") (IPO OR ナスダック OR 業績 OR 利益 OR 延滞 OR 旅行サービス OR 不正対策 OR セキュリティ)',
        ]
    },
    "Wise": {
        "ja": [
            '("Wise" OR "TransferWise" OR "Wise Platform" OR "Wise口座" OR "Rende+") ("海外送金" OR "国境間決済" OR クロスボーダー決済)',
            '("Wise" OR "Wise Platform") ("グローバル決済インフラ" OR 直接接続 OR "Banking as a Service" OR BaaS OR 銀行提携)',
            '("Wise" OR "Wise Platform") ("マルチカレンシー口座" OR 仲値レート OR 手数料の透明性 OR 送金速度)',
            '("Wise Business" OR "Wise法人" OR ("Wise" AND (サプライヤー支払い OR フリーランス OR 法人送金)))',
            '("Wise" OR "TransferWise") (ライセンス OR 地理的拡大 OR 不正対策 OR コンプライアンス OR アンチマネーロンダリング OR AML)',
        ]
    },
    "Nomad": {
        "ja": [
            '("Nomad Global" OR "Nomad Fintech" OR "Nomad Wealth" OR "Nomad口座") ("国際口座" OR "ドル・ユーロ口座" OR 為替両替 OR 国際カード)',
            '("Nomad Global" OR "Nomad Fintech") ("Nomad Explorer" OR "Visa Infinite" OR "Nomad Pass" OR 特典 OR "Nomad Lounge" OR "Nomad Trips")',
            '("Nomad Global" OR "Nomad Fintech") ("AI旅行プランニング" OR ホテル・航空券予約 OR "Nomad Chip" OR eSIM OR 海外旅行保険 OR キャッシュバック)',
            '("Nomad Global" OR "Nomad Wealth") ("米国投資" OR "株式・ETF・REIT" OR 空港ラウンジ体験 OR 観光提携 OR 証券ライセンス)',
        ]
    },
    "Revolut": {
        "ja": [
            '("Revolut" OR "Revolut Bank" OR "Revolut Ultra" OR "Revolut Business" OR "Revolut Pay") ("中南米進出" OR ブラジル OR メキシコ OR 銀行免許 OR 利息付き口座)',
            '("Revolut" OR "Revolut Ultra") (グローバルカード OR 融資 OR プレミアム層 OR RevPoints OR マイル特典 OR 国際投資)',
            '("Revolut" OR "Revolut Business") ("株式およびETF" OR 暗号資産 OR ステーブルコイン OR EURR OR マルチカレンシー口座 OR "Revolut Pay")',
            '("Revolut Research" OR ("Revolut" AND ("人工知能" OR "金融基盤モデル" OR PRAGMA)))',
            '("Revolut" OR "Revolut Bank") (コンプライアンス OR 規制制約 OR 不正対策 OR 金融犯罪防止 OR スポンサーシップ)',
        ]
    },
    "Caixa Economica Federal": {
        "ja": [
            '("Caixa Econômica Federal" OR "Caixa Economica" OR "CEF" OR "Caixa Tem" OR "Caixa Habitação") ("住宅ローン" OR "不動産融資" OR "Minha Casa Minha Vida" OR SFH OR SBPE OR 住宅資金 OR LCI OR 証券化)',
            '("Caixa Econômica Federal" OR "Caixa Economica" OR "CEF" OR "Caixa Tem") ("社会保障" OR "金融包摂" OR "デジタル行政" OR "生成AI" OR "デジタル接客" OR 自動化 OR Pix OR "オープンファイナンス")',
            '("Caixa Econômica Federal" OR "Caixa Economica" OR "CEF" OR "Caixa Empresas" OR "Caixa Asset") ("農業融資" OR Pronaf OR 業務効率化 OR 収益性 OR "業務変革" OR 技術近代化)',
        ]
    },
    "Itau": {
        "ja": [
            '("Itaú" OR "Itau" OR "Itaú Unibanco" OR "Itau Unibanco" OR "Itaú BBA" OR "iti") ("生成AI" OR "AIエージェント" OR "対話型バンキング" OR "金融コパイロット" OR "AI投資" OR "パーソナライゼーション" OR IAI)',
            '("Itaú" OR "Itau" OR "Itaú Private" OR "Itaú Asset" OR "Itaú Personnalité") ("ウェルスマネジメント" OR 資産運用助言 OR "海外投資" OR Vanguard OR バンガード OR グローバル分散投資 OR 富裕層)',
            '("Itaú" OR "Itau" OR "Itaú Unibanco" OR "Rede") ("埋め込み型金融" OR "Embedded Finance" OR "Banking as a Service" OR BaaS OR APIs OR "オープンファイナンス" OR スーパーアプリ OR 中小企業融資 OR ESG)',
        ]
    },
    "Bradesco": {
        "ja": [
            '("Bradesco" OR "Banco Bradesco" OR "Next" OR "Ágora") (BIA OR "BIA GenAI" OR "対話型バンキング" OR "金融アシスタント" OR "AIファーストバンキング" OR "BIA Tech")',
            '("Bradesco" OR "Banco Bradesco") (店舗閉鎖 OR コスト削減 OR 生産性 OR 業務変革 OR デジタル化 OR "Meu Bradesco" OR "金融マーケットプレイス" OR "オープンファイナンス")',
            '("Bradesco Seguros" OR ("Bradesco" AND ("気候保険" OR パラメトリック保険 OR デジタル資産 OR トークン化 OR デジタルカストディ OR 暗号資産)))',
        ]
    },
    "Bank of America": {
        "ja": [
            '("Bank of America" OR "BofA" OR "バンク・オブ・アメリカ" OR "Merrill Lynch") ("デジタルバンキング" OR "エージェンティックバンキング" OR "Agentic AI" OR "自律型金融" OR "金融コパイロット")',
            '("BofA Institute" OR "BofA Global Research" OR ("Bank of America" AND ("消費トレンド" OR "Z世代経済" OR "銀行の未来" OR "米国消費者")))',
            '("Bank of America" OR "BofA" OR "BofA Securities") ("リアルタイム決済" OR RTP OR 即時決済 OR 国境間送金 OR 組込型金融 OR プラットフォーム経済 OR 資産トークン化 OR プライベートクレジット OR "Jio Financial")',
        ]
    },
    "JPMorgan": {
        "ja": [
            '("JPMorgan" OR "JPMorgan Chase" OR "JPモルガン" OR "Onyx" OR "Kinexys") (トークン化 OR トークン化預金 OR デジタル資産 OR ブロックチェーン決済 OR 機関向けブロックチェーン OR 規制準拠DeFi OR スマートコントラクト)',
            '("JPMorgan" OR "JPMorgan Chase" OR "JP Morgan Payments") ("金融インフラ" OR ホールセール決済 OR プログラマブル決済 OR リアルタイムトレジャリー OR 国境間送金 OR 企業間決済)',
            '("JPMorgan" OR "JPMorgan Chase" OR "Chase") ("AIバンキング" OR 生成AI OR "Agentic AI" OR 組込型金融 OR APIバンキング OR BaaS OR プライベートクレジット OR 機関投資家)',
        ]
    },
}

MERCADOS_ALVO = [
    {"gl": "JP", "hl": "ja-JP", "lang": "ja"}
]

TERMOS_EXCLUIDOS = {
    "ja": [
        "クーポン", "割引コード", "プレゼントキャンペーン", "口座開設手順", "ステップバイステップ",
        "本日の株価推移", "本日の為替レート", "顧客の苦情", "おすすめ口座ランキング", "スポーツ",
        "サッカー", "芸能", "占い", "レシピ",
    ]
}

TERMOS_DESCARTE_TEXTO = {
    "ja": [
        "続きを読む", "登録", "共有", "広告", "無断転載を禁じます", "写真：", "クレジット：",
        "関連記事", "編集部", "ここをクリック", "メルマガ登録", "スポンサー記事", "口座開設方法",
    ]
}

PERIODO_BUSCA = "1d"
DOMINIOS_PREFERENCIAIS = []
MODELO_EMBEDDING_1024 = "BAAI/bge-m3"
SIMILARIDADE_REDUNDANCIA = 0.73
MAX_WORKERS_PARALELO = 8
TIMEOUT_REQUISICAO = 5
