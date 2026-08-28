"""Configuração para França, Alemanha, Itália e Suíça."""

REGIAO_NOME = "EUROPA_CONTINENTAL"

MONITORAMENTOS = {
    "Reinvencao do Consumo": {
        "fr": [
            '("réinvention de la consommation" OR "comportement du consommateur" OR "futur de la consommation") ("parcours d\'achat" OR "parcours non linéaire" OR omnicanal)',
            '("commerce agentique" OR "agentic commerce" OR "agents d\'achat" OR "commerce autonome" OR "AI shopping" OR "paiements agentiques")',
            '("IA conversationnelle" OR "commerce conversationnel" OR "commerce vocal" OR "consommation anticipative" OR "commerce prédictif")',
            '("hyperpersonnalisation" OR "recommandation en temps réel" OR "commerce contextuel" OR "next best offer")',
            '("commerce unifié" OR "commerce intégré" OR "commerce sans friction" OR "paiements invisibles" OR phygital)',
            '("social commerce" OR "live commerce" OR "live shopping" OR "creator commerce" OR "TikTok Shop" OR "WhatsApp commerce")',
            '("expériences immersives" OR "réalité augmentée retail" OR "essayage virtuel" OR "autonomie du consommateur")',
            '("confidentialité du consommateur" OR "souveraineté des données" OR "identité numérique" OR "fatigue numérique")',
            '("dark patterns" OR "manipulation algorithmique" OR "recherche d\'analogique" OR "expériences authentiques" OR "humanisation du service")',
        ],
        "de": [
            '("Neuerfindung des Konsums" OR "Konsumverhalten" OR "Zukunft des Konsums") ("Customer Journey" OR "nicht-lineare Customer Journey" OR Omnichannel)',
            '("Agentic Commerce" OR "Einkaufsagenten" OR "KI-Shopping" OR "autonomer Handel" OR "agentenbasierte Zahlungen")',
            '("konversationelle KI" OR "Conversational Commerce" OR "Voice Commerce" OR "antizipativer Konsum" OR "Predictive Commerce")',
            '("Hyperpersonalisierung" OR "Echtzeit-Empfehlungen" OR "kontextbezogener Handel" OR "Next Best Offer")',
            '("Unified Commerce" OR "Embedded Commerce" OR "reibungsloser Handel" OR "unsichtbare Zahlungen" OR Phygital)',
            '("Social Commerce" OR "Live-Shopping" OR "Creator Commerce" OR "Shoppable Content" OR "TikTok Shop" OR "WhatsApp Commerce")',
            '("immersive Erlebnisse" OR "Augmented Reality Handel" OR "virtuelle Anprobe" OR "Verbraucherautonomie")',
            '("Verbraucherdatenschutz" OR "Datensouveränität" OR "digitale Identität" OR "digitale Ermüdung")',
            '("Dark Patterns" OR "algorithmische Manipulation" OR "Streben nach Analogem" OR "authentische Erfahrungen" OR "Vermenschlichung des Kundenservice")',
        ],
        "it": [
            '("reinvenzione del consumo" OR "comportamento dei consumatori" OR "futuro del consumo") ("customer journey" OR "percorso non lineare" OR omnicanalità)',
            '("commercio agentico" OR "agentic commerce" OR "agenti di acquisto" OR "commercio autonomo" OR "AI shopping" OR "pagamenti agentici")',
            '("IA conversazionale" OR "commercio conversazionale" OR "voice commerce" OR "consumo anticipatorio" OR "commercio predittivo")',
            '("iperpersonalizzazione" OR "raccomandazioni in tempo reale" OR "context-aware commerce" OR "next best offer")',
            '("commercio unificato" OR "embedded commerce" OR "commercio senza attriti" OR "pagamenti invisibili" OR phygital)',
            '("social commerce" OR "live shopping" OR "creator commerce" OR "shoppable content" OR "TikTok Shop" OR "WhatsApp commerce")',
            '("esperienze immersive" OR "realtà aumentata retail" OR "camerino virtuale" OR "autonomia del consumatore")',
            '("privacy dei consumatori" OR "sovranità dei dati" OR "identità digitale" OR "affaticamento digitale")',
            '("dark pattern" OR "manipolazione algoritmica" OR "ricerca dell\'analogico" OR "esperienze autentiche" OR "umanizzazione del servizio")',
        ],
    },
    "Nubank": {
        "fr": [
            '("Nubank" OR "Nu Holdings" OR "Nu México" OR "Nu Colombia" OR "Nubank N.A.") (bénéfice OR ROE OR efficacité OR ARPAC OR "revenu par client actif")',
            '("Nubank" OR "Nu Holdings") (engagement OR "portefeuille de crédit" OR "taux de défaut" OR créances)',
            '("Nubank" OR "Nu Holdings") ("modèles de crédit IA" OR "limites dynamiques" OR NuFormer OR "intelligence artificielle" OR Ultravioleta)',
            '("Nubank" OR "Nu Holdings") ("Nu Entreprises" OR marketplace OR "Nubank Shopping" OR investissements OR assurances OR "compte global")',
            '("Nubank" OR "Nu Holdings") ("licence bancaire" OR "partenariat Wise" OR "Open Finance" OR expansion OR Mexique OR Colombie OR acquisitions OR sécurité)',
        ],
        "de": [
            '("Nubank" OR "Nu Holdings" OR "Nu México" OR "Nu Colombia" OR "Nubank N.A.") (Gewinn OR ROE OR Effizienz OR ARPAC OR Ertrag)',
            '("Nubank" OR "Nu Holdings") (Kundenbindung OR Kreditportfolio OR Kreditausfälle OR "KI-Kreditmodelle")',
            '("Nubank" OR "Nu Holdings") ("dynamische Limits" OR NuFormer OR "Künstliche Intelligenz" OR Ultravioleta OR "Mass Affluent")',
            '("Nubank" OR "Nu Holdings") ("Nu Business" OR NuCel OR "Nubank Shopping" OR Investitionen OR Versicherungen OR "globales Konto")',
            '("Nubank" OR "Nu Holdings") (Banklizenz OR "Wise Partnerschaft" OR "Open Finance" OR Expansion OR Mexiko OR Kolumbien OR Übernahmen OR Betrug)',
        ],
        "it": [
            '("Nubank" OR "Nu Holdings" OR "Nu México" OR "Nu Colombia" OR "Nubank N.A.") (utile OR ROE OR efficienza OR ARPAC OR ricavi)',
            '("Nubank" OR "Nu Holdings") (fidelizzazione OR "portafoglio crediti" OR insolvenze OR "modelli di credito IA")',
            '("Nubank" OR "Nu Holdings") (NuFormer OR "intelligenza artificiale" OR Ultravioleta OR "alta gamma" OR "Nu Business")',
            '("Nubank" OR "Nu Holdings") (marketplace OR investimenti OR assicurazioni OR "conto globale" OR "licenza bancaria")',
            '("Nubank" OR "Nu Holdings") ("Open Finance" OR "partnership Wise" OR espansione OR Messico OR Colombia OR acquisizioni OR frodi)',
        ],
    },
    "PicPay": {
        "fr": [
            '("PicPay" OR "PicPay Bank" OR "PicPay Card" OR "PicPay Empresas") (ChatGPT OR "IA conversationnelle" OR "interface bancaire" OR "Open Finance")',
            '("PicPay" OR "PicPay Bank") ("portefeuille numérique" OR agrégateur OR Pix OR crédits OR investissements OR assurances)',
            '("PicPay Empresas" OR ("PicPay" AND (TPE OR "PicPay Tap" OR acquisition OR "fonds de roulement" OR marketplace)))',
            '("PicPay" OR "PicPay Bank") (IPO OR Nasdaq OR résultats OR bénéfice OR insolvabilité OR expansion OR voyages OR fraude OR sécurité)',
        ],
        "de": [
            '("PicPay" OR "PicPay Bank" OR "PicPay Card" OR "PicPay Empresas") (ChatGPT OR "konversationelle KI" OR "Bank-Interface" OR "Open Finance")',
            '("PicPay" OR "PicPay Bank") ("digitale Geldbörse" OR Finanzaggregator OR Pix OR Kredite OR Investitionen OR Versicherungen)',
            '("PicPay Empresas" OR ("PicPay" AND (Kartenterminal OR "PicPay Tap" OR Händlerakquise OR Betriebskapital OR Marktplatz)))',
            '("PicPay" OR "PicPay Bank") (IPO OR Nasdaq OR Geschäftsergebnisse OR Gewinn OR Kreditausfälle OR Expansion OR Betrug OR Sicherheit)',
        ],
        "it": [
            '("PicPay" OR "PicPay Bank" OR "PicPay Card" OR "PicPay Empresas") (ChatGPT OR "IA conversazionale" OR "interfaccia bancaria" OR "Open Finance")',
            '("PicPay" OR "PicPay Bank") ("portafoglio digitale" OR aggregatore OR Pix OR prestiti OR investimenti OR assicurazioni)',
            '("PicPay Empresas" OR ("PicPay" AND (POS OR "PicPay Tap" OR acquiring OR "capitale circolante" OR marketplace)))',
            '("PicPay" OR "PicPay Bank") (IPO OR Nasdaq OR risultati OR utile OR insolvenze OR espansione OR viaggi OR frodi OR sicurezza)',
        ],
    },
    "Wise": {
        "fr": [
            '("Wise" OR "TransferWise" OR "Wise Platform" OR "Compte Wise" OR "Rende+") ("transferts internationaux" OR "paiements transfrontaliers" OR "cross-border")',
            '("Wise" OR "Wise Platform") ("Pix international" OR "infrastructure mondiale de paiement" OR "connexion directe" OR "Banking as a Service" OR BaaS)',
            '("Wise" OR "Wise Platform") ("partenariats bancaires" OR "compte multidevise" OR "taux de change réel" OR "transparence des frais")',
            '("Wise Business" OR "Wise Entreprises" OR ("Wise" AND ("paiements fournisseurs" OR freelances OR facturation)))',
            '("Wise" OR "TransferWise") (licences OR "expansion géographique" OR fraudes OR conformité OR "blanchiment d\'argent" OR LCB-FT)',
        ],
        "de": [
            '("Wise" OR "TransferWise" OR "Wise Platform" OR "Wise Konto" OR "Rende+") ("internationale Überweisungen" OR "grenzüberschreitende Zahlungen" OR Cross-Border)',
            '("Wise" OR "Wise Platform") ("globale Zahlungsinfrastruktur" OR Direktanbindung OR "Banking-as-a-Service" OR BaaS OR Bankpartnerschaften)',
            '("Wise" OR "Wise Platform") ("Multi-Währungs-Konto" OR Devisenmittelkurs OR Gebührentransparenz OR Überweisungsgeschwindigkeit)',
            '("Wise Business" OR "Wise Unternehmen" OR ("Wise" AND (Lieferantenzahlungen OR Freelancer OR B2B-Zahlungen)))',
            '("Wise" OR "TransferWise") (Banklizenzen OR "geografische Expansion" OR Betrugsprävention OR Compliance OR Geldwäschebekämpfung OR AML)',
        ],
        "it": [
            '("Wise" OR "TransferWise" OR "Wise Platform" OR "Conto Wise" OR "Rende+") ("trasferimenti internazionali" OR "pagamenti transfrontalieri" OR cross-border)',
            '("Wise" OR "Wise Platform") ("infrastruttura di pagamento globale" OR "connessione diretta" OR "Banking as a Service" OR BaaS OR partnership)',
            '("Wise" OR "Wise Platform") ("conto multivaluta" OR "tasso di cambio reale" OR "trasparenza delle commissioni" OR "velocità di trasferimento")',
            '("Wise Business" OR "Wise Aziende" OR ("Wise" AND ("pagamenti fornitori" OR freelancer OR pagamenti B2B)))',
            '("Wise" OR "TransferWise") (licenze OR "espansione geografica" OR frodi OR conformità OR antiriciclaggio OR AML)',
        ],
    },
    "Nomad": {
        "fr": [
            '("Nomad Global" OR "Nomad Fintech" OR "Nomad Wealth" OR "Compte Nomad") ("compte international" OR "devises dollar euro" OR change OR "carte internationale")',
            '("Nomad Global" OR "Nomad Fintech") ("Nomad Explorer" OR "Visa Infinite" OR "Nomad Pass" OR fidélité OR "Nomad Lounge" OR "Nomad Trips")',
            '("Nomad Global" OR "Nomad Fintech") ("planification voyages IA" OR réservations OR "Nomad Chip" OR eSIM OR "assurance voyage" OR cashback)',
            '("Nomad Global" OR "Nomad Wealth") ("investissements USA" OR "actions, ETF et REIT" OR "expérience aéroportuaire" OR partenariats OR licences OR courtage)',
        ],
        "de": [
            '("Nomad Global" OR "Nomad Fintech" OR "Nomad Wealth" OR "Nomad Konto") ("internationales Konto" OR "Dollar und Euro" OR Devisen OR "internationale Karte")',
            '("Nomad Global" OR "Nomad Fintech") ("Nomad Explorer" OR "Visa Infinite" OR "Nomad Pass" OR Treueprogramm OR "Nomad Lounge" OR "Nomad Trips")',
            '("Nomad Global" OR "Nomad Fintech") ("KI-Reiseplanung" OR Buchungen OR "Nomad Chip" OR eSIM OR Reiseversicherung OR Cashback)',
            '("Nomad Global" OR "Nomad Wealth") ("US-Investitionen" OR "Aktien, ETFs und REITs" OR Flughafen-Lounge OR Partnerschaften OR Broker-Lizenz)',
        ],
        "it": [
            '("Nomad Global" OR "Nomad Fintech" OR "Nomad Wealth" OR "Conto Nomad") ("conto internazionale" OR "dollari ed euro" OR cambio valuta OR "carta internazionale")',
            '("Nomad Global" OR "Nomad Fintech") ("Nomad Explorer" OR "Visa Infinite" OR "Nomad Pass" OR fedeltà OR "Nomad Lounge" OR "Nomad Trips")',
            '("Nomad Global" OR "Nomad Fintech") ("pianificazione viaggi IA" OR prenotazioni OR "Nomad Chip" OR eSIM OR "assicurazione viaggio" OR cashback)',
            '("Nomad Global" OR "Nomad Wealth") ("investimenti USA" OR "azioni, ETF e REIT" OR "esperienze in aeroporto" OR partnership OR licenze)',
        ],
    },
    "Revolut": {
        "fr": [
            '("Revolut" OR "Revolut Bank" OR "Revolut Ultra" OR "Revolut Business" OR "Revolut Pay") ("expansion Amérique Latine" OR Brésil OR "licence bancaire" OR "compte rémunéré")',
            '("Revolut" OR "Revolut Ultra") ("cartes globales" OR crédits OR "segment premium" OR RevPoints OR "programme de fidélité")',
            '("Revolut" OR "Revolut Business") ("investissements internationaux" OR "actions et ETF" OR cryptomonnaies OR EURR OR "compte multidevise" OR "Revolut Pay")',
            '("Revolut Research" OR ("Revolut" AND ("intelligence artificielle" OR "modèles de fondation financiers" OR PRAGMA)))',
            '("Revolut" OR "Revolut Bank") (conformité OR "restrictions réglementaires" OR fraudes OR "prévention criminalité financière" OR partenariats)',
        ],
        "de": [
            '("Revolut" OR "Revolut Bank" OR "Revolut Ultra" OR "Revolut Business" OR "Revolut Pay") ("Lateinamerika Expansion" OR Brasilien OR Banklizenz OR Tagesgeldkonto)',
            '("Revolut" OR "Revolut Ultra") (Globalkarten OR Kredite OR "Premium Segment" OR RevPoints OR Meilenprogramm)',
            '("Revolut" OR "Revolut Business") ("internationale Investitionen" OR "Aktien und ETFs" OR Krypto OR Stablecoins OR EURR OR "Multi-Währungs-Konto")',
            '("Revolut Research" OR ("Revolut" AND ("Künstliche Intelligenz" OR "Finanz-Basismodelle" OR PRAGMA)))',
            '("Revolut" OR "Revolut Bank") (Compliance OR "regulatorische Einschränkungen" OR Betrugsprävention OR Geldwäschebekämpfung)',
        ],
        "it": [
            '("Revolut" OR "Revolut Bank" OR "Revolut Ultra" OR "Revolut Business" OR "Revolut Pay") ("espansione America Latina" OR Brasile OR "licenza bancaria" OR "conto remunerato")',
            '("Revolut" OR "Revolut Ultra") ("carte globali" OR prestiti OR "segmento premium" OR RevPoints OR miglia)',
            '("Revolut" OR "Revolut Business") ("investimenti internazionali" OR "azioni ed ETF" OR criptovalute OR stablecoin OR EURR OR "conto multivaluta")',
            '("Revolut Research" OR ("Revolut" AND ("intelligenza artificiale" OR "modelli fondazionali" OR PRAGMA)))',
            '("Revolut" OR "Revolut Bank") (conformità OR "restrizioni normative" OR frodi OR "prevenzione reati finanziari")',
        ],
    },
    "Caixa Economica Federal": {
        "fr": [
            '("Caixa Econômica Federal" OR "Caixa Economica" OR "CEF" OR "Caixa Tem" OR "Caixa Habitação") ("crédit immobilier" OR "financement immobilier" OR "Minha Casa Minha Vida" OR SFH OR SBPE OR LCI OR titrisation)',
            '("Caixa Econômica Federal" OR "Caixa Economica" OR "CEF" OR "Caixa Tem") ("programmes sociaux" OR "inclusion financière" OR "gouvernement numérique" OR "IA générative" OR Pix OR "Open Finance")',
            '("Caixa Econômica Federal" OR "Caixa Economica" OR "CEF" OR "Caixa Empresas" OR "Caixa Asset") ("crédit rural" OR Pronaf OR agroalimentaire OR efficacité OR productivité OR "transformation opérationnelle")',
        ],
        "de": [
            '("Caixa Econômica Federal" OR "Caixa Economica" OR "CEF" OR "Caixa Tem" OR "Caixa Habitação") (Immobilienkredite OR Wohnungsbaufinanzierung OR "Minha Casa Minha Vida" OR SFH OR SBPE OR LCI OR Verbriefung)',
            '("Caixa Econômica Federal" OR "Caixa Economica" OR "CEF" OR "Caixa Tem") (Sozialprogramme OR "finanzielle Inklusion" OR "generative KI" OR Digitalisierung OR Pix OR "Open Finance")',
            '("Caixa Econômica Federal" OR "Caixa Economica" OR "CEF" OR "Caixa Empresas" OR "Caixa Asset") (Agrarkredite OR Pronaf OR Agrobusiness OR Effizienz OR "operative Transformation")',
        ],
        "it": [
            '("Caixa Econômica Federal" OR "Caixa Economica" OR "CEF" OR "Caixa Tem" OR "Caixa Habitação") ("mutui immobiliari" OR "credito immobiliare" OR "Minha Casa Minha Vida" OR SFH OR SBPE OR LCI OR cartolarizzazione)',
            '("Caixa Econômica Federal" OR "Caixa Economica" OR "CEF" OR "Caixa Tem") ("programmi sociali" OR "inclusione finanziaria" OR "governo digitale" OR "IA generativa" OR Pix OR "Open Finance")',
            '("Caixa Econômica Federal" OR "Caixa Economica" OR "CEF" OR "Caixa Empresas" OR "Caixa Asset") ("credito agrario" OR Pronaf OR efficienza OR produttività OR "trasformazione operativa")',
        ],
    },
    "Itau": {
        "fr": [
            '("Itaú" OR "Itau" OR "Itaú Unibanco" OR "Itau Unibanco" OR "Itaú BBA" OR "iti") ("IA générative" OR "agents IA" OR "banque conversationnelle" OR "copilotes financiers" OR "IA pour investissements" OR IAI)',
            '("Itaú" OR "Itau" OR "Itaú Private" OR "Itaú Asset" OR "Itaú Personnalité") ("gestion de patrimoine" OR "wealth management" OR advisory OR "investissements internationaux" OR Vanguard OR "allocation globale")',
            '("Itaú" OR "Itau" OR "Itaú Unibanco" OR "Rede") ("embedded finance" OR "Banking as a Service" OR BaaS OR APIs OR "Open Finance" OR "finance verte" OR ESG OR "crédit PME")',
        ],
        "de": [
            '("Itaú" OR "Itau" OR "Itaú Unibanco" OR "Itau Unibanco" OR "Itaú BBA" OR "iti") ("generative KI" OR "KI-Agenten" OR "Conversational Banking" OR "Finanz-Copilots" OR "KI-Investitionen" OR IAI)',
            '("Itaú" OR "Itau" OR "Itaú Private" OR "Itaú Asset" OR "Itaú Personnalité") ("Wealth Management" OR Vermögensverwaltung OR Vanguard OR "globale Allokation" OR "Mass Affluent")',
            '("Itaú" OR "Itau" OR "Itaú Unibanco" OR "Rede") ("Embedded Finance" OR "Banking as a Service" OR BaaS OR APIs OR "Open Finance" OR Superapp OR "Green Finance" OR ESG)',
        ],
        "it": [
            '("Itaú" OR "Itau" OR "Itaú Unibanco" OR "Itau Unibanco" OR "Itaú BBA" OR "iti") ("IA generativa" OR "agenti IA" OR "banca conversazionale" OR "copilot finanziari" OR "IA per investimenti" OR IAI)',
            '("Itaú" OR "Itau" OR "Itaú Private" OR "Itaú Asset" OR "Itaú Personnalité") ("wealth management" OR consulenza OR "investimenti internazionali" OR Vanguard OR "allocazione globale")',
            '("Itaú" OR "Itau" OR "Itaú Unibanco" OR "Rede") ("embedded finance" OR "Banking as a Service" OR BaaS OR APIs OR "Open Finance" OR superapp OR "finanza verde" OR ESG)',
        ],
    },
    "Bradesco": {
        "fr": [
            '("Bradesco" OR "Banco Bradesco" OR "Next" OR "Ágora") (BIA OR "BIA GenAI" OR "banque conversationnelle" OR "assistant financier" OR "AI-first banking" OR "BIA Tech")',
            '("Bradesco" OR "Banco Bradesco" OR "Bradesco Seguros") ("fermeture d\'agences" OR "réduction des coûts" OR "Meu Bradesco" OR "Open Finance" OR "assurance climatique" OR "assurance paramétrique")',
            '("Bradesco" OR "Bradesco Asset" OR "BBI" OR "Inovabra") ("actifs numériques" OR tokenisation OR "garde numérique" OR cryptomonnaies OR "tokenized assets")',
        ],
        "de": [
            '("Bradesco" OR "Banco Bradesco" OR "Next" OR "Ágora") (BIA OR "BIA GenAI" OR "Conversational Banking" OR "Finanzassistent" OR "AI-first Banking" OR "BIA Tech")',
            '("Bradesco" OR "Banco Bradesco" OR "Bradesco Seguros") (Filialschließungen OR Kostensenkung OR Digitalisierung OR "Meu Bradesco" OR "Open Finance" OR Klimaversicherung)',
            '("Bradesco" OR "Bradesco Asset" OR "BBI" OR "Inovabra") ("digitale Vermögenswerte" OR Tokenisierung OR "digitale Verwahrung" OR Krypto OR "Tokenized Assets")',
        ],
        "it": [
            '("Bradesco" OR "Banco Bradesco" OR "Next" OR "Ágora") (BIA OR "BIA GenAI" OR "banca conversazionale" OR "assistente finanziario" OR "AI-first banking" OR "BIA Tech")',
            '("Bradesco" OR "Banco Bradesco" OR "Bradesco Seguros") ("chiusura filiali" OR "riduzione costi" OR digitalizzazione OR "Meu Bradesco" OR "Open Finance" OR "assicurazione climatica")',
            '("Bradesco" OR "Bradesco Asset" OR "BBI" OR "Inovabra") ("asset digitali" OR tokenizzazione OR "custodia digitale" OR criptovalute OR "tokenized assets")',
        ],
    },
    "Bank of America": {
        "fr": [
            '("Bank of America" OR "BofA" OR "Merrill Lynch" OR "Merrill") ("banque numérique" OR "agentic banking" OR "agents IA" OR "finance autonome" OR "copilotes financiers")',
            '("BofA Institute" OR "BofA Global Research" OR ("Bank of America" AND ("tendances de consommation" OR "Gen Z economy" OR "futur de la banque")))',
            '("Bank of America" OR "BofA" OR "BofA Securities") ("paiements en temps réel" OR RTP OR "cross-border payments" OR "embedded finance" OR "wealth management" OR tokenisation OR "crédit privé" OR "Jio Financial")',
        ],
        "de": [
            '("Bank of America" OR "BofA" OR "Merrill Lynch" OR "Merrill") ("Digital Banking" OR "Agentic Banking" OR "KI-Agenten" OR "autonome Finanzsysteme" OR "Finanz-Copilots")',
            '("BofA Institute" OR "BofA Global Research" OR ("Bank of America" AND ("Konsumtrends" OR "Gen Z Wirtschaft" OR "Zukunft des Bankwesens")))',
            '("Bank of America" OR "BofA" OR "BofA Securities") ("Echtzeitzahlungen" OR RTP OR "grenzüberschreitende Zahlungen" OR "Embedded Finance" OR "Wealth Management" OR Tokenisierung OR "Private Credit" OR "Jio Financial")',
        ],
        "it": [
            '("Bank of America" OR "BofA" OR "Merrill Lynch" OR "Merrill") ("digital banking" OR "agentic banking" OR "agenti IA" OR "finanza autonoma" OR "copilot finanziari")',
            '("BofA Institute" OR "BofA Global Research" OR ("Bank of America" AND ("trend di consumo" OR "Gen Z economy" OR "futuro bancario")))',
            '("Bank of America" OR "BofA" OR "BofA Securities") ("pagamenti in tempo reale" OR RTP OR "pagamenti transfrontalieri" OR "embedded finance" OR "wealth management" OR tokenizzazione OR "credito privato" OR "Jio Financial")',
        ],
    },
    "JPMorgan": {
        "fr": [
            '("JPMorgan" OR "JPMorgan Chase" OR "Chase" OR "Onyx" OR "Kinexys") (tokenisation OR "dépôts tokenisés" OR "actifs numériques" OR "règlement blockchain" OR "blockchain institutionnelle" OR "DeFi régulée")',
            '("JPMorgan" OR "JPMorgan Chase" OR "JP Morgan Payments") ("infrastructure financière" OR "paiements de gros" OR "paiements programmables" OR "trésorerie en temps réel" OR "paiements transfrontaliers")',
            '("JPMorgan" OR "JPMorgan Chase" OR "Chase") ("IA bancaire" OR "IA générative" OR "agentic AI" OR "embedded finance" OR "API banking" OR BaaS OR "crédit privé" OR "investissements institutionnels")',
        ],
        "de": [
            '("JPMorgan" OR "JPMorgan Chase" OR "Chase" OR "Onyx" OR "Kinexys") (Tokenisierung OR "tokenisierte Einlagen" OR "digitale Vermögenswerte" OR Blockchain-Abwicklung OR "institutionelle Blockchain" OR "regulierte DeFi")',
            '("JPMorgan" OR "JPMorgan Chase" OR "JP Morgan Payments") (Finanzinfrastruktur OR "Wholesale Payments" OR "programmierbare Zahlungen" OR "Echtzeit-Treasury" OR "grenzüberschreitende Zahlungen")',
            '("JPMorgan" OR "JPMorgan Chase" OR "Chase") ("KI im Bankwesen" OR "generative KI" OR "Agentic AI" OR "Embedded Finance" OR "API Banking" OR BaaS OR "Private Credit" OR "institutionelle Anlagen")',
        ],
        "it": [
            '("JPMorgan" OR "JPMorgan Chase" OR "Chase" OR "Onyx" OR "Kinexys") (tokenizzazione OR "depositi tokenizzati" OR "asset digitali" OR "regolamento su blockchain" OR "blockchain istituzionale" OR "DeFi regolamentata")',
            '("JPMorgan" OR "JPMorgan Chase" OR "JP Morgan Payments") ("infrastruttura finanziaria" OR "pagamenti wholesale" OR "pagamenti programmabili" OR "tesoreria in tempo reale" OR "pagamenti transfrontalieri")',
            '("JPMorgan" OR "JPMorgan Chase" OR "Chase") ("IA bancaria" OR "IA generativa" OR "agentic AI" OR "embedded finance" OR "API banking" OR BaaS OR "credito privato" OR "investimenti istituzionali")',
        ],
    },
}

MERCADOS_ALVO = [
    {"gl": "FR", "hl": "fr-FR", "lang": "fr"},
    {"gl": "DE", "hl": "de-DE", "lang": "de"},
    {"gl": "IT", "hl": "it-IT", "lang": "it"},
    {"gl": "CH", "hl": "de-CH", "lang": "de"},
    {"gl": "CH", "hl": "fr-CH", "lang": "fr"},
]

TERMOS_EXCLUIDOS = {
    "fr": [
        "promotion",
        "promotions",
        "code promo",
        "coupon",
        "tirage au sort",
        "jeu concours",
        "comment ouvrir un compte",
        "tutoriel étape par étape",
        "cours de l'action du jour",
        "taux de change quotidien",
        "réclamations clients",
        "comparatif des meilleures banques",
        "sport",
        "football",
        "horoscope",
        "recette",
    ],
    "de": [
        "Gutschein",
        "Rabattcode",
        "Aktion",
        "Gewinnspiel",
        "Konto eröffnen Anleitung",
        "Schritt für Schritt",
        "Aktienkurs heute",
        "Tageskurs",
        "Kundenbeschwerden",
        "die besten Konten Vergleich",
        "Sport",
        "Fußball",
        "Promi",
        "Horoskop",
        "Rezept",
    ],
    "it": [
        "promozione",
        "promozioni",
        "codice sconto",
        "coupon",
        "lotteria",
        "come aprire un conto",
        "guida passo passo",
        "andamento azioni oggi",
        "tasso di cambio oggi",
        "reclami clienti",
        "classifica migliori conti",
        "sport",
        "calcio",
        "celebrità",
        "oroscopo",
        "ricetta",
    ],
}

TERMOS_DESCARTE_TEXTO = {
    "fr": [
        "lire la suite",
        "s'abonner",
        "partager",
        "publicité",
        "tous droits réservés",
        "photo :",
        "crédit :",
        "voir aussi",
        "rédaction",
        "cliquez ici",
        "newsletter",
        "sponsorisé",
        "comment ouvrir un compte",
    ],
    "de": [
        "weiterlesen",
        "abonnieren",
        "teilen",
        "werbung",
        "alle rechte vorbehalten",
        "foto:",
        "bild:",
        "siehe auch",
        "redaktion",
        "hier klicken",
        "gesponsert",
        "konto eröffnen",
    ],
    "it": [
        "leggi di più",
        "iscriviti",
        "condividi",
        "pubblicità",
        "tutti i diritti riservati",
        "foto:",
        "credito:",
        "vedi anche",
        "redazione",
        "clicca qui",
        "sponsorizzato",
    ],
}

PERIODO_BUSCA = "1d"
DOMINIOS_PREFERENCIAIS = []
MODELO_EMBEDDING_1024 = "BAAI/bge-m3"
SIMILARIDADE_REDUNDANCIA = 0.73
MAX_WORKERS_PARALELO = 8
TIMEOUT_REQUISICAO = 6
