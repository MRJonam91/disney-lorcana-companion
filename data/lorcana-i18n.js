/* ==========================================================================
   DISNEY LORCANA · 5-LANGUAGE I18N ENGINE & 3D HOLOGRAPHIC FOIL CONTROLLER
   Supported Languages: IT (Italiano), EN (English), FR (Français), DE (Deutsch), ES (Español)
   ========================================================================== */

(function () {
  const I18N = {
    it: {
      nav_hub: "🌐 Hub",
      nav_decklab: "🃏 Deck Lab",
      nav_vault: "💎 Collezionismo & Pulls",
      nav_guide: "📖 Guida",
      nav_guide_href: "guide/guida-lorcana-it.html",
      nav_app: "📱 App Ufficiale",
      nav_forum: "💬 Discussions",

      // Index Page
      idx_badge: "✦ Il Portale Definitivo per gli Illumineer ✦",
      idx_subtitle: "Repository completo della community, guide strategiche interattive in 5 lingue, storico dei 14 Set, rarità e collezionismo, simulatore spacchettamento foil e laboratorio mazzi da torneo.",
      idx_cta_deck: "🃏 Apri Deck Lab & Playtester",
      idx_cta_vault: "💎 Apri Collector's Vault & Pulls",
      idx_cta_guide: "📖 Leggi Guida Interattiva",
      idx_cta_app: "📱 App Ufficiale Ravensburger",
      idx_lang_title: "Scegli la Tua Lingua · 5 Edizioni Ufficiali",
      idx_lang_desc: "Guide interattive standalone, regole complete, segnapunti Lore e simulatore matematico del mulligan.",
      idx_apps_title: "✨ Web App Interattive & Simulatori da Tavolo",
      idx_apps_desc: "Strumenti avanzati con effetti Foil olografici CSS per creazione mazzi, goldfish playtesting e calcolo pull rate.",
      idx_deck_title: "Deck Lab & Playtester",
      idx_deck_desc: "Costruisci il tuo mazzo da 60 carte pescando dal database portatile dei 14 Set, analizza la curva d'inchiostro, simula la mano iniziale con mulligan e testa i turni in modalità Goldfish. Esporta con 1 click per duels.ink, inktable e dreamborn.",
      idx_deck_btn: "Lancia Deck Lab & Playtester ➔",
      idx_vault_title: "Collector's Vault & Pulls",
      idx_vault_desc: "Simula l'apertura di qualsiasi numero di bustine (1, 8, 10, Box da 24, Case da 96 o quantità libera) con effetti Foil CSS, rarità Epiche e Iconiche, guida alle 3 Ere, simboli ufficiali e calcolatore binomiale.",
      idx_vault_btn: "Apri Collector's Vault ➔",
      idx_kb_title: "Knowledge Base & Documentazione",
      idx_kb_desc: "Guide markdown complete e database consultabili in tutte le 5 lingue nella cartella docs/.",
      idx_app_badge: "App Ufficiale Ravensburger per il Collezionismo",
      idx_app_title: "Disney Lorcana TCG Companion App",
      idx_app_desc: "L'applicazione ufficiale gratuita per iOS e Android sviluppata da Ravensburger: catalogo completo di tutte le carte con effetto foil 3D reattivo al movimento, gestione collezione e wishlist, contatore Lore e aggiornamenti ufficiali.",

      // Collector Vault Page
      vault_badge: "Simulatore Collezionismo, Effetti Foil & Pull Rate",
      vault_title: "Disney Lorcana · Collector's Vault",
      vault_desc: "Simula l'apertura di bustine, Trove, Booster Box e Case con effetti Foil olografici. Calcola le probabilità matematiche per tutti i 14 Set (incluse Epiche e Iconiche) ed esplora il catalogo prodotti.",
      disclaimer_html: "<strong>NOTA INFORMATIVA & STATISTICHE SPERIMENTALI:</strong> Disney Lorcana™ è un marchio registrato di Disney e Ravensburger. <strong>Ravensburger non pubblica percentuali ufficiali di estrazione.</strong> Tutti i tassi e i simulatori qui presenti sono stime sperimentali della community internazionale (casi studio su 44+ box di <em>The Gamers Lodge</em> e <em>Reddit r/Lorcana</em>) e modelli di distribuzione binomiale.",
      tab_sim: "🎴 Simulatore Pull",
      tab_prob: "📊 Calcolatore Probabilità",
      tab_guide: "📖 Ere, Simboli & God Packs",
      tab_prod: "📦 Catalogo Prodotti",
      tab_chal: "🏆 Sfide & Moneta 3D",
      sim_panel_title: "🎴 Simulatore Spacchettamento Olografico",
      btn_reset_col: "🔄 Azzera Collezione",
      lbl_set_select: "Set Espansione:",
      lbl_custom_packs: "🔢 Quantità libera:",
      btn_open_custom: "🚀 Apri Bustine",
      act_1_title: "1 Booster Pack",
      act_1_sub: "1 Bustina · 12 Carte (o Starter)",
      act_4_title: "Gift Set",
      act_4_sub: "4 Bustine · 48 Carte",
      act_8_title: "Illumineer's Trove",
      act_8_sub: "8 Bustine · 96 Carte",
      act_24_title: "1 Booster Box",
      act_24_sub: "24 Bustine · 288 Carte",
      act_96_title: "1 Master Case",
      act_96_sub: "96 Bustine · 4 Box Sigillati",
      stat_packs: "Bustine",
      stat_common: "Comuni ⚪",
      stat_uncommon: "Non Comuni 📖",
      stat_rare: "Rare 🔺",
      stat_super: "Super Rare 🔷",
      stat_legendary: "Leggendarie 🟡",
      stat_epic: "Epiche 🟣",
      stat_enchanted: "Incantate ✨",
      stat_iconic: "Iconiche 👑",
      stat_foils: "Foil Totali 🌟",
      lbl_last_pulled: "✨ Ultime Carte Sbustate (Passa il mouse per l'effetto Foil 3D):",
      empty_pull_msg: "Seleziona un prodotto qui sopra o inserisci un numero di bustine per iniziare lo spacchettamento con effetti Foil!",
      prob_title: "📊 Calcolatore Probabilità Matematiche & Pull Rate",
      prob_desc: "Muovi lo slider per calcolare cosa aspettarti in base al numero di bustine aperte secondo il modello binomiale della community.",
      guide_title: "📖 Guida ai Simboli, Evoluzione delle 3 Ere & God Packs",
      prod_title: "📦 Catalogo Completo dei Prodotti Ufficiali",
      chal_quest_title: "🎲 Sfida della Serata (Community Quest Generator)",
      chal_quest_btn: "✨ Genera Nuova Sfida per la Partita",
      chal_coin_title: "🪙 Chi Inizia il Turno 1? (Illumineer Coin Flip)",
      chal_ach_title: "🏅 Traguardi del Collezionista & Giocatore",

      // Deck Lab Page
      dl_badge: "Tournament Deck Builder & Goldfish Playtester",
      dl_title: "Disney Lorcana · Deck Lab",
      dl_desc: "Costruisci il tuo mazzo da 60 carte con il database completo dei 14 Set, analizza la curva d'inchiostro, testa la mano iniziale con mulligan e simula i turni. Esporta per duels.ink, inktable o dreamborn.",
      dl_tab_builder: "🛠️ Deck Builder & Curva",
      dl_tab_goldfish: "🎲 Simulatore Mano & Goldfish",
      dl_tab_online: "⚡ Gioca Online (Duels.ink & Inktable)",
      dl_cat_title: "📚 Catalogo Carte (Set 1 – 14)",
      dl_preset_lbl: "Carica Deck Meta Competitivo:",
      dl_search_ph: "🔍 Cerca per nome, rarità o abilità (es. Mickey, Epic, Shift, Ward)...",
      dl_deck_title: "🃏 Mazzo Attivo",
      dl_btn_clear: "🗑️ Svuota",
      dl_stat_total: "Carte Totali",
      dl_stat_ink: "Inchiostrabili",
      dl_stat_noink: "Non-Inkable",
      dl_stat_avg: "Costo Medio",
      dl_curve_lbl: "Distribuzione Curva d'Inchiostro:",
      dl_gf_title: "🎲 Tavolo di Test Goldfish (Mano Iniziale, Mulligan & Primi Turni)",
      dl_btn_newhand: "🔄 Nuova Mano (7 Carte)",
      dl_btn_mulligan: "✨ Esegui Mulligan Selezionate",
      dl_btn_nextturn: "⏭️ Passa al Turno Successivo (+1 Pesca)"
    },

    en: {
      nav_hub: "🌐 Hub",
      nav_decklab: "🃏 Deck Lab",
      nav_vault: "💎 Collector Vault",
      nav_guide: "📖 Guide",
      nav_guide_href: "guide/lorcana-guide-en.html",
      nav_app: "📱 Official App",
      nav_forum: "💬 Discussions",

      idx_badge: "✦ The Ultimate Illumineer Portal ✦",
      idx_subtitle: "Complete community repository, interactive strategy guides in 5 languages, full 14-Set history, card rarities & collecting, holographic pack simulator, and tournament deck builder.",
      idx_cta_deck: "🃏 Launch Deck Lab & Playtester",
      idx_cta_vault: "💎 Open Collector's Vault & Pulls",
      idx_cta_guide: "📖 Read Interactive Guide",
      idx_cta_app: "📱 Official Ravensburger App",
      idx_lang_title: "Select Your Language · 5 Official Editions",
      idx_lang_desc: "Standalone interactive web guides with lore tracker, card anatomy, and mathematical mulligan simulator.",
      idx_apps_title: "✨ Interactive Web Apps & Tabletop Simulators",
      idx_apps_desc: "Next-gen tools with CSS Holographic Foil effects for deck building, goldfish playtesting, and pull rate analysis.",
      idx_deck_title: "Deck Lab & Playtester",
      idx_deck_desc: "Build and refine your 60-card deck using the portable 14-Set database, live ink curve visualizer, realistic opening hand mulligan tester, and turn-by-turn goldfish simulator. 1-click export for duels.ink, inktable, and dreamborn.",
      idx_deck_btn: "Launch Deck Lab & Playtester ➔",
      idx_vault_title: "Collector's Vault & Pulls",
      idx_vault_desc: "Simulate opening any number of packs (1, 8, 10, 24-Pack Box, 96-Pack Case, or custom amount) with 3D CSS Foil shaders, Epic & Iconic rarities, 3-Eras comparison, official symbols, and binomial odds calculator.",
      idx_vault_btn: "Open Collector's Vault ➔",
      idx_kb_title: "Repository Knowledge Base",
      idx_kb_desc: "Comprehensive markdown documentation and portable data files available in all 5 languages inside docs/.",
      idx_app_badge: "Official Ravensburger Collecting App",
      idx_app_title: "Disney Lorcana TCG Companion App",
      idx_app_desc: "The official free iOS and Android app by Ravensburger: browse the complete card catalog with gyroscope 3D foil effects, track your personal collection and wishlist, use the built-in Lore counter, and get expansion news.",

      vault_badge: "Collecting Simulator, Holographic Foil FX & Pull Rates",
      vault_title: "Disney Lorcana · Collector's Vault",
      vault_desc: "Simulate opening booster packs, Troves, Booster Boxes, and Sealed Cases with CSS Holographic Foil effects. Calculate binomial probabilities across all 14 Sets (including Epic & Iconic) and explore sealed products.",
      disclaimer_html: "<strong>STATISTICAL NOTICE & EXPERIMENTAL PULL RATES:</strong> Disney Lorcana™ is a registered trademark of Disney and Ravensburger. <strong>Ravensburger does not publish official pull rates.</strong> All odds and simulations on this platform are experimental community estimates (44+ box case studies by <em>The Gamers Lodge</em> and <em>Reddit r/Lorcana</em>) combined with binomial distribution models.",
      tab_sim: "🎴 Pack Simulator",
      tab_prob: "📊 Probability Calculator",
      tab_guide: "📖 Eras, Symbols & God Packs",
      tab_prod: "📦 Product Catalog",
      tab_chal: "🏆 Quests & 3D Coin",
      sim_panel_title: "🎴 Realistic Holographic Pack Simulator",
      btn_reset_col: "🔄 Reset Collection",
      lbl_set_select: "Expansion Set:",
      lbl_custom_packs: "🔢 Custom packs:",
      btn_open_custom: "🚀 Open Packs",
      act_1_title: "1 Booster Pack",
      act_1_sub: "1 Pack · 12 Cards (or Starter)",
      act_4_title: "Gift Set",
      act_4_sub: "4 Packs · 48 Cards",
      act_8_title: "Illumineer's Trove",
      act_8_sub: "8 Packs · 96 Cards",
      act_24_title: "1 Booster Box",
      act_24_sub: "24 Packs · 288 Cards",
      act_96_title: "1 Master Case",
      act_96_sub: "96 Packs · 4 Sealed Boxes",
      stat_packs: "Packs",
      stat_common: "Common ⚪",
      stat_uncommon: "Uncommon 📖",
      stat_rare: "Rare 🔺",
      stat_super: "Super Rare 🔷",
      stat_legendary: "Legendary 🟡",
      stat_epic: "Epic 🟣",
      stat_enchanted: "Enchanted ✨",
      stat_iconic: "Iconic 👑",
      stat_foils: "Total Foils 🌟",
      lbl_last_pulled: "✨ Latest Pulled Cards (Hover for 3D Holographic Foil Tilt):",
      empty_pull_msg: "Click any product card above or enter a custom pack count to start opening packs with 3D Foil effects!",
      prob_title: "📊 Mathematical Probability & Pull Rate Calculator",
      prob_desc: "Move the slider to calculate expected pulls based on community-verified binomial probabilities.",
      guide_title: "📖 Official Symbols, 3-Eras Evolution & God Packs Guide",
      prod_title: "📦 Complete Official Sealed Products Catalog",
      chal_quest_title: "🎲 Tabletop Quest of the Night (Generator)",
      chal_quest_btn: "✨ Generate New Match Quest",
      chal_coin_title: "🪙 Who Goes First on Turn 1? (3D Coin Flip)",
      chal_ach_title: "🏅 Illumineer Collector & Player Achievements",

      dl_badge: "Tournament Deck Builder & Goldfish Playtester",
      dl_title: "Disney Lorcana · Deck Lab",
      dl_desc: "Build your 60-card deck across all 14 Sets, analyze your ink curve, test opening hands with realistic mulligans, and simulate early turns. Export to duels.ink, inktable, or dreamborn.",
      dl_tab_builder: "🛠️ Deck Builder & Curve",
      dl_tab_goldfish: "🎲 Hand & Goldfish Simulator",
      dl_tab_online: "⚡ Play Online (Duels.ink & Inktable)",
      dl_cat_title: "📚 Card Catalog (Sets 1 – 14)",
      dl_preset_lbl: "Load Competitive Meta Deck:",
      dl_search_ph: "🔍 Search by name, rarity, or keyword (e.g., Mickey, Epic, Shift, Ward)...",
      dl_deck_title: "🃏 Active Deck",
      dl_btn_clear: "🗑️ Clear",
      dl_stat_total: "Total Cards",
      dl_stat_ink: "Inkable",
      dl_stat_noink: "Non-Inkable",
      dl_stat_avg: "Avg Cost",
      dl_curve_lbl: "Ink Curve Distribution:",
      dl_gf_title: "🎲 Goldfish Test Table (Opening Hand, Mulligan & Turn Simulator)",
      dl_btn_newhand: "🔄 New Hand (7 Cards)",
      dl_btn_mulligan: "✨ Mulligan Selected Cards",
      dl_btn_nextturn: "⏭️ Next Turn (+1 Draw)"
    },

    fr: {
      nav_hub: "🌐 Portail",
      nav_decklab: "🃏 Deck Lab",
      nav_vault: "💎 Collection & Tirages",
      nav_guide: "📖 Guide",
      nav_guide_href: "guide/lorcana-guide-fr.html",
      nav_app: "📱 App Officielle",
      nav_forum: "💬 Forum",

      idx_badge: "✦ Le Portail Ultime des Illumineurs ✦",
      idx_subtitle: "Référentiel complet de la communauté, guides stratégiques interactifs en 5 langues, historique des 14 Sets, raretés et collection, simulateur de boosters Foil et créateur de decks.",
      idx_cta_deck: "🃏 Ouvrir Deck Lab & Playtester",
      idx_cta_vault: "💎 Ouvrir Collector's Vault & Tirages",
      idx_cta_guide: "📖 Lire le Guide Interactif",
      idx_cta_app: "📱 App Officielle Ravensburger",
      idx_lang_title: "Choisissez Votre Langue · 5 Éditions",
      idx_lang_desc: "Guides interactifs complets avec compteur d'éclats de Lore, anatomie des cartes et simulateur de mulligan.",
      idx_apps_title: "✨ Applications Web & Simulateurs de Jeu",
      idx_apps_desc: "Outils interactifs avec effets Foil holographiques CSS pour la création de decks, le test Goldfish et les taux de drop.",
      idx_deck_title: "Deck Lab & Playtester",
      idx_deck_desc: "Construisez votre deck de 60 cartes avec la base de données des 14 Sets, analysez la courbe d'encre, testez votre main de départ avec mulligan et simulez vos tours. Export en 1 clic vers duels.ink, inktable et dreamborn.",
      idx_deck_btn: "Lancer Deck Lab & Playtester ➔",
      idx_vault_title: "Collector's Vault & Tirages",
      idx_vault_desc: "Simulez l'ouverture de n'importe quel nombre de boosters (1, 8, 10, Display de 24, Case de 96 ou nombre libre) avec effets Foil CSS, cartes Épiques et Iconiques, guide des 3 Ères et calculateur binomial.",
      idx_vault_btn: "Ouvrir Collector's Vault ➔",
      idx_kb_title: "Base de Connaissances & Documentation",
      idx_kb_desc: "Documentation markdown complète et fichiers de données disponibles dans les 5 langues dans le dossier docs/.",
      idx_app_badge: "Application Officielle Ravensburger",
      idx_app_title: "Disney Lorcana TCG Companion App",
      idx_app_desc: "L'application gratuite officielle pour iOS et Android par Ravensburger : catalogue complet avec effet foil 3D gyroscopique, gestion de collection et liste de souhaits, compteur de Lore et actualités.",

      vault_badge: "Simulateur de Collection, Effets Foil & Taux de Drop",
      vault_title: "Disney Lorcana · Collector's Vault",
      vault_desc: "Simulez l'ouverture de boosters, Troves, Displays et Cases avec effets Foil holographiques. Calculez les probabilités sur les 14 Sets (incluant Épiques et Iconiques).",
      disclaimer_html: "<strong>AVERTISSEMENT STATISTIQUE & TAUX EXPÉRIMENTAUX :</strong> Disney Lorcana™ est une marque déposée de Disney et Ravensburger. <strong>Ravensburger ne publie pas de taux officiels.</strong> Toutes les probabilités sont des estimations expérimentales de la communauté (études sur 44+ displays par <em>The Gamers Lodge</em> et <em>Reddit r/Lorcana</em>) et des modèles binomiaux.",
      tab_sim: "🎴 Simulateur Boosters",
      tab_prob: "📊 Calculateur Probabilités",
      tab_guide: "📖 Ères, Symboles & God Packs",
      tab_prod: "📦 Catalogue Produits",
      tab_chal: "🏆 Défis & Pièce 3D",
      sim_panel_title: "🎴 Simulateur d'Ouverture Holographique",
      btn_reset_col: "🔄 Réinitialiser",
      lbl_set_select: "Extension :",
      lbl_custom_packs: "🔢 Nombre libre :",
      btn_open_custom: "🚀 Ouvrir Boosters",
      act_1_title: "1 Booster",
      act_1_sub: "1 Booster · 12 Cartes (ou Starter)",
      act_4_title: "Coffret Cadeau (Gift Set)",
      act_4_sub: "4 Boosters · 48 Cartes",
      act_8_title: "Illumineer's Trove",
      act_8_sub: "8 Boosters · 96 Cartes",
      act_24_title: "1 Display (Box)",
      act_24_sub: "24 Boosters · 288 Cartes",
      act_96_title: "1 Master Case",
      act_96_sub: "96 Boosters · 4 Displays",
      stat_packs: "Boosters",
      stat_common: "Communes ⚪",
      stat_uncommon: "Inhabituelles 📖",
      stat_rare: "Rares 🔺",
      stat_super: "Très Rares 🔷",
      stat_legendary: "Légendaires 🟡",
      stat_epic: "Épiques 🟣",
      stat_enchanted: "Enchantées ✨",
      stat_iconic: "Iconiques 👑",
      stat_foils: "Total Foils 🌟",
      lbl_last_pulled: "✨ Dernières Cartes Tirées (Survolez pour l'effet Foil 3D) :",
      empty_pull_msg: "Cliquez sur un produit ci-dessus ou entrez un nombre personnalisé de boosters pour commencer l'ouverture !",
      prob_title: "📊 Calculateur Mathématique de Probabilités & Pull Rates",
      prob_desc: "Déplacez le curseur pour calculer vos tirages attendus selon la loi binomiale.",
      guide_title: "📖 Guide des Symboles, Évolution des 3 Ères & God Packs",
      prod_title: "📦 Catalogue Complet des Produits Scellés",
      chal_quest_title: "🎲 Défi de la Soirée (Générateur de Quêtes)",
      chal_quest_btn: "✨ Générer un Nouveau Défi",
      chal_coin_title: "🪙 Qui Commence au Tour 1 ? (Lancer de Pièce 3D)",
      chal_ach_title: "🏅 Succès du Collectionneur & Joueur",

      dl_badge: "Créateur de Deck & Playtester Goldfish",
      dl_title: "Disney Lorcana · Deck Lab",
      dl_desc: "Construisez votre deck de 60 cartes parmi les 14 Sets, analysez votre courbe d'encre, testez votre main avec mulligan et simulez vos premiers tours. Exportez vers duels.ink, inktable ou dreamborn.",
      dl_tab_builder: "🛠️ Créateur & Courbe",
      dl_tab_goldfish: "🎲 Simulateur Main & Goldfish",
      dl_tab_online: "⚡ Jouer en Ligne (Duels.ink & Inktable)",
      dl_cat_title: "📚 Catalogue de Cartes (Sets 1 – 14)",
      dl_preset_lbl: "Charger un Deck Méta Compétitif :",
      dl_search_ph: "🔍 Rechercher par nom, rareté ou mot-clé (ex. Mickey, Epic, Shift, Ward)...",
      dl_deck_title: "🃏 Deck Actif",
      dl_btn_clear: "🗑️ Vider",
      dl_stat_total: "Total Cartes",
      dl_stat_ink: "Encrables",
      dl_stat_noink: "Non-Encrables",
      dl_stat_avg: "Coût Moyen",
      dl_curve_lbl: "Distribution de la Courbe d'Encre :",
      dl_gf_title: "🎲 Table de Test Goldfish (Main de Départ, Mulligan & Tours)",
      dl_btn_newhand: "🔄 Nouvelle Main (7 Cartes)",
      dl_btn_mulligan: "✨ Mulligan de la Sélection",
      dl_btn_nextturn: "⏭️ Tour Suivant (+1 Pioche)"
    },

    de: {
      nav_hub: "🌐 Portal",
      nav_decklab: "🃏 Deck Lab",
      nav_vault: "💎 Sammlung & Pulls",
      nav_guide: "📖 Leitfaden",
      nav_guide_href: "guide/lorcana-guide-de.html",
      nav_app: "📱 Offizielle App",
      nav_forum: "💬 Forum",

      idx_badge: "✦ Das Ultimative Luminari-Portal ✦",
      idx_subtitle: "Vollständiges Community-Repository, interaktive Strategieleitfäden in 5 Sprachen, Historie aller 14 Sets, Seltenheiten & Sammlung, holografischer Booster-Simulator und Turnier-Deckbuilder.",
      idx_cta_deck: "🃏 Deck Lab & Playtester Öffnen",
      idx_cta_vault: "💎 Collector's Vault & Pulls Öffnen",
      idx_cta_guide: "📖 Interaktiven Leitfaden Lesen",
      idx_cta_app: "📱 Offizielle Ravensburger App",
      idx_lang_title: "Wähle Deine Sprache · 5 Offizielle Ausgaben",
      idx_lang_desc: "Eigenständige interaktive Web-Guides mit Legenden-Zähler, Kartenanatomie und Mulligan-Simulator.",
      idx_apps_title: "✨ Interaktive Web-Apps & Tabletop-Simulatoren",
      idx_apps_desc: "Moderne Tools mit holografischen CSS-Foil-Effekten für Deckbau, Goldfish-Playtesting und Pull-Rate-Analyse.",
      idx_deck_title: "Deck Lab & Playtester",
      idx_deck_desc: "Baue dein 60-Karten-Deck mit der Datenbank aller 14 Sets, analysiere die Tintenkurve, teste deine Starthand mit Mulligan und simuliere Züge. 1-Klick-Export für duels.ink, inktable und dreamborn.",
      idx_deck_btn: "Deck Lab & Playtester Starten ➔",
      idx_vault_title: "Collector's Vault & Pulls",
      idx_vault_desc: "Simuliere das Öffnen beliebig vieler Booster (1, 8, 10, 24er Display, 96er Case oder freie Anzahl) mit 3D-CSS-Foil-Effekten, Episch & Ikonisch, 3-Ären-Vergleich und Binomial-Rechner.",
      idx_vault_btn: "Collector's Vault Öffnen ➔",
      idx_kb_title: "Wissensdatenbank & Dokumentation",
      idx_kb_desc: "Umfassende Markdown-Dokumentation und Datenbanken in allen 5 Sprachen im Ordner docs/.",
      idx_app_badge: "Offizielle Ravensburger Sammler-App",
      idx_app_title: "Disney Lorcana TCG Companion App",
      idx_app_desc: "Die offizielle kostenlose iOS- und Android-App von Ravensburger: kompletter Kartenkatalog mit 3D-Foil-Effekt, Sammlungsverwaltung und Wunschliste, Legenden-Zähler und Neuigkeiten.",

      vault_badge: "Sammler-Simulator, Holografische Foil-FX & Pull Rates",
      vault_title: "Disney Lorcana · Collector's Vault",
      vault_desc: "Simuliere das Öffnen von Boostern, Troves, Displays und Cases mit holografischen Foil-Effekten. Berechne Wahrscheinlichkeiten für alle 14 Sets (inkl. Episch & Ikonisch).",
      disclaimer_html: "<strong>STATISTISCHER HINWEIS & EXPERIMENTELLE PULL RATES:</strong> Disney Lorcana™ ist eine eingetragene Marke von Disney und Ravensburger. <strong>Ravensburger veröffentlicht keine offiziellen Ziehungsraten.</strong> Alle Wahrscheinlichkeiten sind experimentelle Schätzungen der Community (44+ Display-Studien von <em>The Gamers Lodge</em> und <em>Reddit r/Lorcana</em>) sowie Binomialmodelle.",
      tab_sim: "🎴 Booster-Simulator",
      tab_prob: "📊 Wahrscheinlichkeitsrechner",
      tab_guide: "📖 Ären, Symbole & God Packs",
      tab_prod: "📦 Produktkatalog",
      tab_chal: "🏆 Quests & 3D-Münze",
      sim_panel_title: "🎴 Realistischer Holografischer Booster-Simulator",
      btn_reset_col: "🔄 Zurücksetzen",
      lbl_set_select: "Erweiterung:",
      lbl_custom_packs: "🔢 Freie Anzahl:",
      btn_open_custom: "🚀 Booster Öffnen",
      act_1_title: "1 Booster Pack",
      act_1_sub: "1 Booster · 12 Karten (oder Starter)",
      act_4_title: "Geschenkset (Gift Set)",
      act_4_sub: "4 Booster · 48 Karten",
      act_8_title: "Illumineer's Trove",
      act_8_sub: "8 Booster · 96 Karten",
      act_24_title: "1 Booster-Display",
      act_24_sub: "24 Booster · 288 Karten",
      act_96_title: "1 Master Case",
      act_96_sub: "96 Booster · 4 Displays",
      stat_packs: "Booster",
      stat_common: "Gewöhnlich ⚪",
      stat_uncommon: "Ungewöhnlich 📖",
      stat_rare: "Selten 🔺",
      stat_super: "Episch Selten 🔷",
      stat_legendary: "Legendär 🟡",
      stat_epic: "Episch 🟣",
      stat_enchanted: "Verzaubert ✨",
      stat_iconic: "Ikonisch 👑",
      stat_foils: "Foils Gesamt 🌟",
      lbl_last_pulled: "✨ Zuletzt Gezogene Karten (Hover für 3D-Foil-Effekt):",
      empty_pull_msg: "Klicke oben auf ein Produkt oder gib eine beliebige Booster-Anzahl ein, um mit 3D-Foil-Effekten zu starten!",
      prob_title: "📊 Mathematischer Wahrscheinlichkeits- & Pull-Rate-Rechner",
      prob_desc: "Bewege den Schieberegler, um deine erwarteten Hits nach der Binomialverteilung zu berechnen.",
      guide_title: "📖 Offizielle Symbole, 3-Ären-Evolution & God Packs",
      prod_title: "📦 Vollständiger Katalog Offizieller Produkte",
      chal_quest_title: "🎲 Herausforderung des Abends (Quest-Generator)",
      chal_quest_btn: "✨ Neue Quest Generieren",
      chal_coin_title: "🪙 Wer Beginnt in Zug 1? (3D-Münzwurf)",
      chal_ach_title: "🏅 Luminari Sammler- & Spieler-Erfolge",

      dl_badge: "Turnier-Deckbuilder & Goldfish-Playtester",
      dl_title: "Disney Lorcana · Deck Lab",
      dl_desc: "Baue dein 60-Karten-Deck aus allen 14 Sets, analysiere deine Tintenkurve, teste Starthände mit Mulligan und simuliere Züge. Exportiere zu duels.ink, inktable oder dreamborn.",
      dl_tab_builder: "🛠️ Deckbuilder & Kurve",
      dl_tab_goldfish: "🎲 Starthand & Goldfish",
      dl_tab_online: "⚡ Online Spielen (Duels.ink & Inktable)",
      dl_cat_title: "📚 Kartenkatalog (Set 1 – 14)",
      dl_preset_lbl: "Turnier-Meta-Deck Laden:",
      dl_search_ph: "🔍 Suche nach Name, Seltenheit oder Fähigkeit (z.B. Mickey, Epic, Shift, Ward)...",
      dl_deck_title: "🃏 Aktives Deck",
      dl_btn_clear: "🗑️ Leeren",
      dl_stat_total: "Karten Gesamt",
      dl_stat_ink: "Tintenbar",
      dl_stat_noink: "Nicht-Tintenbar",
      dl_stat_avg: "Ø Kosten",
      dl_curve_lbl: "Tintenkurven-Verteilung:",
      dl_gf_title: "🎲 Goldfish-Testtisch (Starthand, Mulligan & Zug-Simulator)",
      dl_btn_newhand: "🔄 Neue Hand (7 Karten)",
      dl_btn_mulligan: "✨ Ausgewählte Mulligan",
      dl_btn_nextturn: "⏭️ Nächster Zug (+1 Ziehen)"
    },

    es: {
      nav_hub: "🌐 Portal",
      nav_decklab: "🃏 Deck Lab",
      nav_vault: "💎 Colección y Sobres",
      nav_guide: "📖 Guía",
      nav_guide_href: "guide/lorcana-guide-es.html",
      nav_app: "📱 App Oficial",
      nav_forum: "💬 Foro",

      idx_badge: "✦ El Portal Definitivo para Iluminadores ✦",
      idx_subtitle: "Repositorio completo de la comunidad, guías estratégicas interactivas en 5 idiomas, historia de los 14 Sets, rarezas y coleccionismo, simulador de sobres Foil y constructor de mazos.",
      idx_cta_deck: "🃏 Abrir Deck Lab y Playtester",
      idx_cta_vault: "💎 Abrir Collector's Vault y Sobres",
      idx_cta_guide: "📖 Leer Guía Interactiva",
      idx_cta_app: "📱 App Oficial Ravensburger",
      idx_lang_title: "Selecciona Tu Idioma · 5 Ediciones Oficiales",
      idx_lang_desc: "Guías web interactivas con contador de Lore, anatomía de cartas y simulador matemático de mulligan.",
      idx_apps_title: "✨ Aplicaciones Web Interactivas y Simuladores",
      idx_apps_desc: "Herramientas avanzadas con efectos Foil holográficos CSS para creación de mazos, test Goldfish y cálculo de pull rates.",
      idx_deck_title: "Deck Lab y Playtester",
      idx_deck_desc: "Construye tu mazo de 60 cartas con la base de datos de los 14 Sets, analiza la curva de tinta, prueba tu mano inicial con mulligan y simula turnos. Exportación en 1 clic a duels.ink, inktable y dreamborn.",
      idx_deck_btn: "Lanzar Deck Lab y Playtester ➔",
      idx_vault_title: "Collector's Vault y Sobres",
      idx_vault_desc: "Simula la apertura de cualquier cantidad de sobres (1, 8, 10, Caja de 24, Case de 96 o cantidad libre) con efectos Foil CSS, rarezas Épicas e Icónicas, guía de las 3 Eras y calculadora binomial.",
      idx_vault_btn: "Abrir Collector's Vault ➔",
      idx_kb_title: "Base de Conocimientos y Documentación",
      idx_kb_desc: "Documentación markdown completa y bases de datos disponibles en los 5 idiomas dentro de docs/.",
      idx_app_badge: "Aplicación Oficial de Ravensburger",
      idx_app_title: "Disney Lorcana TCG Companion App",
      idx_app_desc: "La aplicación gratuita oficial para iOS y Android desarrollada por Ravensburger: catálogo completo con efecto foil 3D giroscópico, gestión de colección y lista de deseos, contador de Lore y novedades.",

      vault_badge: "Simulador de Coleccionismo, Efectos Foil y Pull Rates",
      vault_title: "Disney Lorcana · Collector's Vault",
      vault_desc: "Simula la apertura de sobres, Troves, Cajas y Cases con efectos Foil holográficos. Calcula probabilidades matemáticas para los 14 Sets (incluyendo Épicas e Icónicas).",
      disclaimer_html: "<strong>AVISO ESTADÍSTICO Y TASAS EXPERIMENTALES:</strong> Disney Lorcana™ es una marca registrada de Disney y Ravensburger. <strong>Ravensburger no publica probabilidades oficiales de aparición.</strong> Todas las tasas y simulaciones son estimaciones experimentales de la comunidad (estudios de 44+ cajas de <em>The Gamers Lodge</em> y <em>Reddit r/Lorcana</em>) y modelos binomiales.",
      tab_sim: "🎴 Simulador de Sobres",
      tab_prob: "📊 Calculadora Probabilidad",
      tab_guide: "📖 Eras, Símbolos y God Packs",
      tab_prod: "📦 Catálogo Productos",
      tab_chal: "🏆 Retos y Moneda 3D",
      sim_panel_title: "🎴 Simulador Holográfico de Apertura de Sobres",
      btn_reset_col: "🔄 Reiniciar Colección",
      lbl_set_select: "Expansión:",
      lbl_custom_packs: "🔢 Cantidad libre:",
      btn_open_custom: "🚀 Abrir Sobres",
      act_1_title: "1 Sobre (Booster)",
      act_1_sub: "1 Sobre · 12 Cartas (o Starter)",
      act_4_title: "Gift Set (Caja Regalo)",
      act_4_sub: "4 Sobres · 48 Cartas",
      act_8_title: "Illumineer's Trove",
      act_8_sub: "8 Sobres · 96 Cartas",
      act_24_title: "1 Booster Box",
      act_24_sub: "24 Sobres · 288 Cartas",
      act_96_title: "1 Master Case",
      act_96_sub: "96 Sobres · 4 Cajas Selladas",
      stat_packs: "Sobres",
      stat_common: "Comunes ⚪",
      stat_uncommon: "Poco Comunes 📖",
      stat_rare: "Raras 🔺",
      stat_super: "Súper Raras 🔷",
      stat_legendary: "Legendarias 🟡",
      stat_epic: "Épicas 🟣",
      stat_enchanted: "Encantadas ✨",
      stat_iconic: "Icónicas 👑",
      stat_foils: "Foils Totales 🌟",
      lbl_last_pulled: "✨ Últimas Cartas Abiertas (Pasa el ratón para efecto Foil 3D):",
      empty_pull_msg: "¡Haz clic en un producto arriba o introduce una cantidad personalizada de sobres para abrir con efectos Foil 3D!",
      prob_title: "📊 Calculadora Matemática de Probabilidades y Pull Rates",
      prob_desc: "Mueve el control deslizante para calcular tus cartas esperadas según el modelo binomial.",
      guide_title: "📖 Guía de Símbolos Oficiales, 3 Eras y God Packs",
      prod_title: "📦 Catálogo Completo de Productos Sellados",
      chal_quest_title: "🎲 Reto de la Noche (Generador de Misiones)",
      chal_quest_btn: "✨ Generar Nuevo Reto",
      chal_coin_title: "🪙 ¿Quién Empieza en el Turno 1? (Moneda 3D)",
      chal_ach_title: "🏅 Logros del Coleccionista y Jugador",

      dl_badge: "Constructor de Mazos de Torneo y Playtester Goldfish",
      dl_title: "Disney Lorcana · Deck Lab",
      dl_desc: "Construye tu mazo de 60 cartas con los 14 Sets, analiza tu curva de tinta, prueba tu mano inicial con mulligan y simula turnos. Exporta a duels.ink, inktable o dreamborn.",
      dl_tab_builder: "🛠️ Constructor y Curva",
      dl_tab_goldfish: "🎲 Simulador Mano y Goldfish",
      dl_tab_online: "⚡ Jugar Online (Duels.ink e Inktable)",
      dl_cat_title: "📚 Catálogo de Cartas (Sets 1 – 14)",
      dl_preset_lbl: "Cargar Mazo Meta Competitivo:",
      dl_search_ph: "🔍 Buscar por nombre, rareza o habilidad (ej. Mickey, Epic, Shift, Ward)...",
      dl_deck_title: "🃏 Mazo Activo",
      dl_btn_clear: "🗑️ Vaciar",
      dl_stat_total: "Cartas Totales",
      dl_stat_ink: "Entintables",
      dl_stat_noink: "No-Entintables",
      dl_stat_avg: "Coste Medio",
      dl_curve_lbl: "Distribución de Curva de Tinta:",
      dl_gf_title: "🎲 Mesa de Prueba Goldfish (Mano Inicial, Mulligan y Turnos)",
      dl_btn_newhand: "🔄 Nueva Mano (7 Cartas)",
      dl_btn_mulligan: "✨ Mulligan Seleccionadas",
      dl_btn_nextturn: "⏭️ Siguiente Turno (+1 Robo)"
    }
  };

  // Localized Quests for Collector Vault
  window.LORCANA_QUESTS_I18N = {
    it: [
      "Vinci una partita senza mai sfidare un personaggio avversario (vittoria pacifista tramite sole missioni).",
      "Risolvi la combinazione 'Duo Shift' entro il Turno 3 giocando Mickey e Minnie.",
      "Canta almeno 3 canzoni diverse nella stessa partita usando personaggi con la keyword Singer.",
      "Raggiungi 10 inchiostri nel Calamaio prima che il tuo avversario ne abbia accumulati 6.",
      "Vinci mantenendo in gioco almeno 3 personaggi protetti da Ward contemporaneamente.",
      "Gioca e mantieni attiva una carta Luogo per almeno 3 turni consecutivi.",
      "Accumula 8 o più Lore in un singolo turno per chiudere la partita!"
    ],
    en: [
      "Win a game without ever challenging an opposing character (pure pacifist questing victory).",
      "Resolve the 'Duo Shift' combo by Turn 3 playing Mickey and Minnie.",
      "Sing at least 3 different Songs in a single match using characters with the Singer keyword.",
      "Reach 10 ink in your Inkwell before your opponent reaches 6.",
      "Win while controlling at least 3 characters with Ward simultaneously.",
      "Play and keep a Location card active for at least 3 consecutive turns.",
      "Gain 8 or more Lore in a single turn to close out the match!"
    ],
    fr: [
      "Gagnez une partie sans jamais défier un personnage adverse (victoire pacifiste uniquement par l'aventure).",
      "Résolvez la combinaison 'Duo Shift' dès le Tour 3 avec Mickey et Minnie.",
      "Chantez au moins 3 chansons différentes dans la même partie avec des personnages Mélomane (Singer).",
      "Atteignez 10 encres dans votre réserve avant que votre adversaire n'en ait 6.",
      "Gagnez en contrôlant au moins 3 personnages avec Hors d'atteinte (Ward) simultanément.",
      "Jouez et gardez un Lieu actif pendant au moins 3 tours consécutifs.",
      "Gagnez 8 éclats de Lore ou plus en un seul tour pour remporter la victoire !"
    ],
    de: [
      "Gewinne ein Spiel, ohne jemals einen gegnerischen Charakter herauszufordern (reiner Erkundungs-Sieg).",
      "Löse die 'Duo Shift'-Kombo bis Zug 3 mit Micky und Minnie aus.",
      "Singe mindestens 3 verschiedene Lieder im selben Spiel mit Singen-Charakteren (Singer).",
      "Erreiche 10 Tinte im Tintenvorrat, bevor dein Gegner 6 erreicht.",
      "Gewinne mit mindestens 3 Charakteren mit Behütet (Ward) gleichzeitig im Spiel.",
      "Spiele einen Ort und halte ihn mindestens 3 Züge in Folge aktiv.",
      "Sammle 8 oder mehr Legenden in einem einzigen Zug für den Sieg!"
    ],
    es: [
      "Gana una partida sin desafiar nunca a un personaje rival (victoria pacifista solo con misiones).",
      "Resuelve la combinación 'Duo Shift' antes del Turno 3 jugando a Mickey y Minnie.",
      "Canta al menos 3 canciones diferentes en la misma partida usando personajes con Cantante (Singer).",
      "Alcanza 10 cartas en tu Tintero antes de que tu rival tenga 6.",
      "Gana manteniendo en juego al menos 3 personajes con Guardián (Ward) simultáneamente.",
      "Juega y mantén activa una carta de Lugar durante al menos 3 turnos consecutivos.",
      "¡Consigue 8 o más puntos de Lore en un solo turno para ganar la partida!"
    ]
  };

  window.LORCANA_I18N = I18N;

  function detectLang() {
    const params = new URLSearchParams(window.location.search);
    const qLang = (params.get("lang") || "").toLowerCase();
    if (I18N[qLang]) {
      localStorage.setItem("lorcana_lang", qLang);
      return qLang;
    }
    const saved = localStorage.getItem("lorcana_lang");
    if (saved && I18N[saved]) return saved;
    return "it";
  }

  window.currentLorcanaLang = detectLang();

  window.setLorcanaLanguage = function (lang) {
    if (!I18N[lang]) return;
    window.currentLorcanaLang = lang;
    localStorage.setItem("lorcana_lang", lang);
    document.documentElement.lang = lang;

    const dict = I18N[lang];

    // Update all [data-i18n] elements
    document.querySelectorAll("[data-i18n]").forEach((el) => {
      const key = el.getAttribute("data-i18n");
      if (dict[key] !== undefined) {
        el.innerText = dict[key];
      }
    });

    // Update all [data-i18n-html] elements
    document.querySelectorAll("[data-i18n-html]").forEach((el) => {
      const key = el.getAttribute("data-i18n-html");
      if (dict[key] !== undefined) {
        el.innerHTML = dict[key];
      }
    });

    // Update all [data-i18n-placeholder] inputs
    document.querySelectorAll("[data-i18n-placeholder]").forEach((el) => {
      const key = el.getAttribute("data-i18n-placeholder");
      if (dict[key] !== undefined) {
        el.setAttribute("placeholder", dict[key]);
      }
    });

    // Update guide link href dynamically based on selected language
    const isSubdir = window.location.pathname.includes("/guide/");
    const prefix = isSubdir ? "../" : "";
    document.querySelectorAll("[data-i18n-guide-link]").forEach((el) => {
      el.setAttribute("href", prefix + dict.nav_guide_href);
    });

    // Highlight active language pill
    document.querySelectorAll(".lang-pill-btn").forEach((btn) => {
      btn.classList.toggle("active", btn.getAttribute("data-lang") === lang);
    });

    // Update quest text if present
    const questEl = document.getElementById("questText");
    if (questEl && window.LORCANA_QUESTS_I18N[lang]) {
      questEl.innerText = `"${window.LORCANA_QUESTS_I18N[lang][0]}"`;
    }
  };

  function injectLanguageSwitcher() {
    const topBar = document.querySelector(".top-bar");
    if (!topBar || document.querySelector(".lang-switcher-bar")) return;

    const langs = [
      { code: "it", flag: "🇮🇹", label: "IT" },
      { code: "en", flag: "🇬🇧", label: "EN" },
      { code: "fr", flag: "🇫🇷", label: "FR" },
      { code: "de", flag: "🇩🇪", label: "DE" },
      { code: "es", flag: "🇪🇸", label: "ES" }
    ];

    const bar = document.createElement("div");
    bar.className = "lang-switcher-bar";
    bar.setAttribute("aria-label", "Language Switcher");

    langs.forEach((l) => {
      const btn = document.createElement("button");
      btn.type = "button";
      btn.className = "lang-pill-btn" + (l.code === window.currentLorcanaLang ? " active" : "");
      btn.setAttribute("data-lang", l.code);
      btn.innerHTML = `<span>${l.flag}</span><span>${l.label}</span>`;
      btn.onclick = () => {
        // If we are inside /guide/*.html standalone guide, navigate to the matching localized guide
        if (window.location.pathname.includes("/guide/")) {
          const map = {
            it: "guida-lorcana-it.html",
            en: "lorcana-guide-en.html",
            fr: "lorcana-guide-fr.html",
            de: "lorcana-guide-de.html",
            es: "lorcana-guide-es.html"
          };
          localStorage.setItem("lorcana_lang", l.code);
          window.location.href = map[l.code];
          return;
        }
        window.setLorcanaLanguage(l.code);
      };
      bar.appendChild(btn);
    });

    topBar.appendChild(bar);
  }

  // Lightweight 3D Card Tilt & Foil Glare Tracker
  function initFoilTiltEngine() {
    const selector = ".pulled-card, .play-card, .foil-card-fx, .pack-action-card, .lang-card";
    document.addEventListener("pointermove", (e) => {
      const card = e.target.closest(selector);
      if (!card) return;
      const rect = card.getBoundingClientRect();
      const x = e.clientX - rect.left;
      const y = e.clientY - rect.top;
      const px = Math.max(0, Math.min(100, (x / rect.width) * 100));
      const py = Math.max(0, Math.min(100, (y / rect.height) * 100));
      const ry = ((px - 50) / 50) * 8;
      const rx = ((50 - py) / 50) * 8;
      card.style.setProperty("--rx", `${rx.toFixed(2)}deg`);
      card.style.setProperty("--ry", `${ry.toFixed(2)}deg`);
      card.style.setProperty("--gx", `${px.toFixed(1)}%`);
      card.style.setProperty("--gy", `${py.toFixed(1)}%`);
    }, { passive: true });

    document.addEventListener("pointerout", (e) => {
      const card = e.target.closest(selector);
      if (!card) return;
      if (!card.contains(e.relatedTarget)) {
        card.style.setProperty("--rx", "0deg");
        card.style.setProperty("--ry", "0deg");
      }
    }, { passive: true });
  }

  window.addEventListener("DOMContentLoaded", () => {
    injectLanguageSwitcher();
    window.setLorcanaLanguage(window.currentLorcanaLang);
    initFoilTiltEngine();
  });
})();
