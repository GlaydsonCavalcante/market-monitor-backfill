"""Configuração unificada de monitoramento para França, Alemanha, Itália e Suíça."""

REGIAO_NOME = "EUROPA_CONTINENTAL"

MONITORAMENTOS = {
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
    "Mercado Pago": {
        "fr": [
            '("Mercado Pago" OR "MercadoPago" OR "Mercado Pago Bank") ("banque numérique" OR "compte rémunéré" OR dépôts OR paie OR "relation bancaire principale")',
            '("Mercado Pago" OR "MercadoPago") (Pix OR "paiements numériques" OR "QR Code" OR Checkout OR "Tap to Pay" OR acquisition OR "passerelle de paiement")',
            '("Mercado Pago" OR "MercadoPago" OR "Mercado Creditos") ("gestion financière PME" OR "prêts aux marchands" OR "fonds de roulement" OR underwriting OR "score alternatif")',
            '("Mercado Pago" OR "MercadoPago") (investissements OR "embedded finance" OR "super app financière" OR "tarification dynamique" OR "fraude IA")',
            '("Mercado Pago" OR "MercadoPago") (concurrence OR Nubank OR cybersécurité OR "Open Finance" OR réglementation)',
        ],
        "de": [
            '("Mercado Pago" OR "MercadoPago" OR "Mercado Pago Bank") (Digitalbank OR Tagesgeldkonto OR Einlagen OR Gehaltskonto OR Hauptbankverbindung)',
            '("Mercado Pago" OR "MercadoPago") (Pix OR "digitale Zahlungen" OR "QR-Code" OR Checkout OR "Tap to Pay" OR Acquiring OR Payment-Gateway)',
            '("Mercado Pago" OR "MercadoPago" OR "Mercado Creditos") (KMU-Finanzmanagement OR Händlerkredite OR Betriebskapital OR "KI-Underwriting" OR Scoring)',
            '("Mercado Pago" OR "MercadoPago") (Geldanlage OR "Embedded Finance" OR "Finanz-Super-App" OR dynamische Preisgestaltung OR "KI-Betrugserkennung")',
            '("Mercado Pago" OR "MercadoPago") (Wettbewerb OR Nubank OR Cybersicherheit OR "Open Finance" OR Bankenregulierung)',
        ],
        "it": [
            '("Mercado Pago" OR "MercadoPago" OR "Mercado Pago Bank") ("banca digitale" OR "conto remunerato" OR depositi OR stipendi OR "banca principale")',
            '("Mercado Pago" OR "MercadoPago") (Pix OR "pagamenti digitali" OR "QR Code" OR Checkout OR "Tap to Pay" OR acquiring OR "gateway di pagamento")',
            '("Mercado Pago" OR "MercadoPago" OR "Mercado Creditos") ("gestione finanziaria PMI" OR "prestiti ai commercianti" OR "capitale circolante" OR "underwriting con IA")',
            '("Mercado Pago" OR "MercadoPago") (investimenti OR "embedded finance" OR "super app finanziaria" OR "rilevamento frodi IA")',
            '("Mercado Pago" OR "MercadoPago") (concorrenza OR Nubank OR sicurezza informatica OR "Open Finance" OR regolamentazione)',
        ],
    },
    "Mercado Livre": {
        "fr": [
            '("Mercado Libre" OR "MercadoLibre" OR "MELI" OR "Mercado Envios" OR "Mercado Ads") (GMV OR "part de marché e-commerce" OR vendeurs OR "retail media" OR "live commerce")',
            '("Mercado Libre" OR "MercadoLibre" OR "Mercado Envios") (fulfillment OR "centres de distribution" OR "dernier kilomètre" OR "livraison le jour même" OR "réseau logistique")',
            '("Mercado Libre" OR "MercadoLibre" OR "Mercado Creditos") ("crédit aux vendeurs" OR "fonds de roulement PME" OR "crédit intégré" OR "embedded lending")',
            '("Mercado Libre" OR "MercadoLibre" OR "Meli+") (fidélisation OR adhésion OR "intelligence artificielle" OR "recherche conversationnelle" OR "agents IA" OR "automatisation logistique")',
            '("Mercado Libre" OR "MercadoLibre" OR "MELI") ("nouvelles verticales" OR acquisitions OR "concurrence Amazon" OR régulation OR contrefaçon OR fraudes)',
        ],
        "de": [
            '("Mercado Libre" OR "MercadoLibre" OR "MELI" OR "Mercado Envios" OR "Mercado Ads") (GMV OR "E-Commerce-Marktanteil" OR Verkäufer OR "Retail Media" OR "Live Shopping")',
            '("Mercado Libre" OR "MercadoLibre" OR "Mercado Envios") (Fulfillment OR Distributionszentren OR "Letzte Meile" OR "Lieferung am selben Tag" OR Logistiknetzwerk)',
            '("Mercado Libre" OR "MercadoLibre" OR "Mercado Creditos") (Händlerkredite OR Betriebskapital OR "Embedded Lending" OR KMU)',
            '("Mercado Libre" OR "MercadoLibre" OR "Meli+") (Kundenbindung OR Mitgliedschaft OR "Künstliche Intelligenz" OR "KI-Agenten" OR Logistikautomatisierung)',
            '("Mercado Libre" OR "MercadoLibre" OR "MELI") (Marktplatzregulierung OR "Amazon-Wettbewerb" OR Übernahmen OR Betrug OR Produktfälschung)',
        ],
        "it": [
            '("Mercado Libre" OR "MercadoLibre" OR "MELI" OR "Mercado Envios" OR "Mercado Ads") (GMV OR "quota di mercato e-commerce" OR venditori OR "retail media" OR "live commerce")',
            '("Mercado Libre" OR "MercadoLibre" OR "Mercado Envios") (fulfillment OR "centri di distribuzione" OR "ultimo miglio" OR "consegna in giornata" OR logistica)',
            '("Mercado Libre" OR "MercadoLibre" OR "Mercado Creditos") ("credito ai venditori" OR "capitale circolante PMI" OR "embedded lending")',
            '("Mercado Libre" OR "MercadoLibre" OR "Meli+") (fidelizzazione OR abbonamento OR "intelligenza artificiale" OR "agenti IA" OR automazione)',
            '("Mercado Libre" OR "MercadoLibre" OR "MELI") ("regolamentazione marketplace" OR "concorrenza con Amazon" OR acquisizioni OR frodi OR contraffazione)',
        ],
    },
    "Amazon": {
        "fr": [
            '("Amazon" OR "Amazon Marketplace") (marketplace OR "vendeurs tiers" OR FBA OR "Fulfillment by Amazon")',
            '("Amazon") ("centres de distribution" OR "robotique logistique" OR "livraison ultra-rapide" OR "dernier kilomètre" OR drones OR automatisation)',
            '("AWS" OR "Amazon Web Services" OR ("Amazon" AND cloud)) ("cloud computing" OR "infrastructure numérique" OR "IA générative" OR "centres de données" OR "souveraineté des données")',
            '("Amazon" OR "AWS") ("Amazon Bedrock" OR "agents IA" OR "assistants intelligents" OR "Alexa+" OR Alexa OR "Amazon Ads" OR "retail media")',
            '("Amazon Prime" OR ("Amazon" AND ("Amazon Pharmacy" OR télémédecine OR fintech OR "embedded finance" OR antitrust OR régulation)))',
        ],
        "de": [
            '("Amazon" OR "Amazon Marketplace") (Marktplatz OR Drittanbieter OR FBA OR "Fulfillment by Amazon")',
            '("Amazon") (Logistikzentren OR Logistikrobotik OR "Lieferung am selben Tag" OR "Letzte Meile" OR Drohnen OR Automatisierung)',
            '("AWS" OR "Amazon Web Services" OR ("Amazon" AND Cloud)) ("Cloud Computing" OR digitale Infrastruktur OR "generative KI" OR Rechenzentren OR Datensouveränität)',
            '("Amazon" OR "AWS") ("Amazon Bedrock" OR "KI-Agenten" OR intelligente Assistenten OR "Alexa+" OR Alexa OR "Amazon Ads" OR "Retail Media")',
            '("Amazon Prime" OR ("Amazon" AND ("Amazon Pharmacy" OR Telemedizin OR Fintech OR "Embedded Finance" OR Kartellrecht OR Regulierung)))',
        ],
        "it": [
            '("Amazon" OR "Amazon Marketplace") (marketplace OR "venditori terzi" OR FBA OR "Fulfillment by Amazon")',
            '("Amazon") ("centri logistici" OR "robotica logistica" OR "consegna ultraveloce" OR "ultimo miglio" OR droni OR automazione)',
            '("AWS" OR "Amazon Web Services" OR ("Amazon" AND cloud)) ("cloud computing" OR "infrastruttura digitale" OR "IA generativa" OR "data center" OR "sovranità dei dati")',
            '("Amazon" OR "AWS") ("Amazon Bedrock" OR "agenti IA" OR "assistenti intelligenti" OR "Alexa+" OR Alexa OR "Amazon Ads" OR "retail media")',
            '("Amazon Prime" OR ("Amazon" AND ("Amazon Pharmacy" OR telemedicina OR fintech OR "embedded finance" OR antitrust OR regolamentazione)))',
        ],
    },
    "iFood": {
        "fr": [
            '("iFood" OR "iFood Card") (livraison OR "quick commerce" OR "livraison rapide" OR "dernier kilomètre" OR "logistique urbaine")',
            '("iFood" OR "iFood Mercado") ("dark stores" OR "commerce de proximité digital" OR "livraison d\'épicerie")',
            '("iFood Pago" OR "Conta Digital iFood" OR ("iFood" AND ("crédit aux restaurants" OR affacturage OR "embedded finance")))',
            '("iFood Ads" OR ("iFood" AND ("retail media" OR "titres-restaurant" OR "avantages sociaux flexibles")))',
            '("iFood") ("IA logistique" OR "optimisation des tournées" OR "gig economy" OR livreurs OR "régulation du travail de plateforme")',
        ],
        "de": [
            '("iFood" OR "iFood Card") (Lieferdienst OR "Quick Commerce" OR Expresslieferung OR "Letzte Meile" OR "urbane Logistik")',
            '("iFood" OR "iFood Mercado") ("Dark Stores" OR "Online-Lebensmittel" OR "Kredite für Restaurants" OR "Embedded Finance")',
            '("iFood Ads" OR ("iFood" AND ("Retail Media" OR Essensgutscheine OR "Mitarbeiter-Benefits")))',
            '("iFood") ("KI-Logistik" OR Tourenplanung OR "Gig Economy" OR Plattformarbeit OR Lieferkuriere OR Arbeitsregulierung)',
        ],
        "it": [
            '("iFood" OR "iFood Card") (delivery OR "quick commerce" OR "consegna rapida" OR "ultimo miglio" OR "logistica urbana")',
            '("iFood" OR "iFood Mercado") ("dark store" OR "spesa online" OR "credito per ristoranti" OR "embedded finance")',
            '("iFood Ads" OR ("iFood" AND ("retail media" OR "buoni pasto" OR "flexible benefit")))',
            '("iFood") ("IA per la logistica" OR "pianificazione percorsi" OR "gig economy" OR fattorini OR "regolamentazione del lavoro su piattaforma")',
        ],
    },
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
    "Reconfiguracao Demografica": {
        "fr": [
            '("transition démographique" OR "changement démographique" OR "vieillissement de la population" OR "société vieillissante" OR "société de longévité" OR "hiver démographique" OR "déclin démographique" OR "taux de dépendance" OR "pyramide des âges")',
            '("chute de la natalité" OR "baisse de la fécondité" OR "crise démographique" OR "familles plus petites" OR infertilité OR "procréation médicalement assistée" OR "politiques natalistes")',
            '("économie de la longévité" OR "silver économie" OR "vieillissement actif" OR "AgeTech" OR "médecine de la longévité" OR "espérance de vie" OR centenaires)',
            '("pénurie de main-d\'œuvre" OR "vieillissement de la main-d\'œuvre" OR reskilling OR "formation continue" OR "retraite tardive" OR multigénérationnel OR "économie du soin")',
            '("réforme des retraites" OR "durabilité des retraites" OR "crise des retraites" OR "pacte intergénérationnel" OR "protection sociale" OR "retraite complémentaire" OR "décumulation")',
            '("soins de longue durée" OR "long-term care" OR "maintien à domicile" OR "santé numérique" OR télémédecine OR "vieillissement en bonne santé" OR démence OR Alzheimer)',
            '("ménages d\'une personne" OR "personnes seules" OR "génération sandwich" OR solitude OR "isolement social" OR "villes amies des aînés" OR "résidences seniors")',
            '("planification financière de la longévité" OR "transmission de patrimoine" OR succession OR "assurance dépendance" OR "assurance longévité" OR "épargne retraite" OR "gestion de patrimoine intergénérationnelle")',
            '("effondrement démographique" OR "société des 100 ans" OR "travailler jusqu\'à 70 ans" OR "baisse de la population active" OR "guerre des talents" OR "pénurie de main-d\'œuvre et automatisation")',
        ],
        "de": [
            '("demografischer Wandel" OR "demografischer Übergang" OR "Überalterung der Gesellschaft" OR "alternde Gesellschaft" OR Langlebigkeit OR "demografischer Winter" OR "Bevölkerungsrückgang" OR "Altenquotient" OR "Alterspyramide")',
            '("Geburtenrückgang" OR "sinkende Geburtenrate" OR "Geburtenkrise" OR "demografische Krise" OR "kinderlose Familien" OR "künstliche Befruchtung" OR "Geburtenförderung")',
            '("Silver Economy" OR "Langlebigkeitsökonomie" OR "aktives Altern" OR "AgeTech" OR "Altersmedizin" OR Lebenserwartung OR Hundertjährige)',
            '("Fachkräftemangel" OR "Arbeitskräftemangel" OR "alternde Belegschaft" OR Weiterbildung OR "lebenslanges Lernen" OR "späterer Renteneintritt" OR "Care-Ökonomie")',
            '("Rentenreform" OR "Rentennachhaltigkeit" OR "Rentenkrise" OR "Generationenvertrag" OR "betriebliche Altersvorsorge" OR "private Altersvorsorge" OR Vermögensverzehr)',
            '("Langzeitpflege" OR "Pflegeökonomie" OR "häusliche Pflege" OR "digitale Gesundheit" OR Telemedizin OR "gesundes Altern" OR Demenz OR Alzheimer)',
            '("Einpersonenhaushalte" OR Alleinstehende OR "Sandwich-Generation" OR Einsamkeit OR "soziale Isolation" OR "altersgerechtes Wohnen" OR Seniorenresidenzen)',
            '("Altersfinanzplanung" OR "Vermögensübertragung" OR Erbschaft OR "Pflegerentenversicherung" OR "Langlebigkeitsversicherung" OR "Generationen-Vermögensverwaltung")',
            '("demografischer Kollaps" OR "100-Jährige-Gesellschaft" OR "Arbeiten bis 70" OR "Rückgang der Erwerbsbevölkerung" OR "Nachhaltigkeit des Generationenvertrags")',
        ],
        "it": [
            '("transizione demografica" OR "invecchiamento della popolazione" OR "società che invecchia" OR "società longeva" OR longevità OR "inverno demografico" OR "declino demografico" OR "indice di dipendenza" OR "piramide delle età")',
            '("calo delle nascite" OR "bassa fecondità" OR "crisi demografica" OR "denatalità" OR "procreazione medicalmente assistita" OR "incentivi alla natalità")',
            '("silver economy" OR "economia della longevità" OR "invecchiamento attivo" OR "AgeTech" OR "medicina della longevità" OR "aspettativa di vita" OR centenari)',
            '("carenza di manodopera" OR "invecchiamento della forza lavoro" OR reskilling OR "apprendimento continuo" OR "pensionamento tardivo" OR multigenerazionale OR "economia della cura")',
            '("riforma delle pensioni" OR "sostenibilità previdenziale" OR "crisi pensionistica" OR "patto intergenerazionale" OR "previdenza complementare" OR "decumulo patrimoniale")',
            '("cure a lungo termine" OR "assistenza domiciliare" OR "sanità digitale" OR telemedicina OR "invecchiamento sano" OR demenza OR Alzheimer)',
            '("famiglie unipersonali" OR "persone che vivono sole" OR "generazione sandwich" OR solitudine OR "isolamento sociale" OR "senior living")',
            '("pianificazione finanziaria per la longevità" OR "passaggio generazionale" OR successione OR "assicurazione longevità" OR "fondi pensione privati")',
            '("collasso demografico" OR "società dei 100 anni" OR "lavorare fino a 70 anni" OR "calo della popolazione attiva" OR "sostenibilità del patto intergenerazionale")',
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
        "promotion", "promotions", "code promo", "coupon", "tirage au sort",
        "jeu concours", "comment ouvrir un compte", "tutoriel étape par étape",
        "cours de l'action du jour", "taux de change quotidien", "réclamations clients",
        "comparatif des meilleures banques", "sport", "football", "horoscope", "recette",
    ],
    "de": [
        "Gutschein", "Rabattcode", "Aktion", "Gewinnspiel", "Konto eröffnen Anleitung",
        "Schritt für Schritt", "Aktienkurs heute", "Tageskurs", "Kundenbeschwerden",
        "die besten Konten Vergleich", "Sport", "Fußball", "Promi", "Horoskop", "Rezept",
    ],
    "it": [
        "promozione", "promozioni", "codice sconto", "coupon", "lotteria",
        "come aprire un conto", "guida passo passo", "andamento azioni oggi",
        "tasso di cambio oggi", "reclami clienti", "classifica migliori conti",
        "sport", "calcio", "celebrità", "oroscopo", "ricetta",
    ],
}

TERMOS_DESCARTE_TEXTO = {
    "fr": [
        "lire la suite", "s'abonner", "partager", "publicité", "tous droits réservés",
        "photo :", "crédit :", "voir aussi", "rédaction", "cliquez ici", "newsletter",
        "sponsorisé", "comment ouvrir un compte",
    ],
    "de": [
        "weiterlesen", "abonnieren", "teilen", "werbung", "alle rechte vorbehalten",
        "foto:", "bild:", "siehe auch", "redaktion", "hier klicken", "gesponsert", "konto eröffnen",
    ],
    "it": [
        "leggi di più", "iscriviti", "condividi", "pubblicità", "tutti i diritti riservati",
        "foto:", "credito:", "vedi anche", "redazione", "clicca qui", "sponsorizzato",
    ],
}

PERIODO_BUSCA = "1d"
DOMINIOS_PREFERENCIAIS = []
MODELO_EMBEDDING_1024 = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
SIMILARIDADE_REDUNDANCIA = 0.73
MAX_WORKERS_PARALELO = 8
TIMEOUT_REQUISICAO = 6
