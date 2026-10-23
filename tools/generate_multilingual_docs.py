import os

def create_pull_rates_docs():
    # French
    fr_content = """# Guide Complet des Taux de Drop (Pull Rates), Raretés, Évolution des 3 Ères et Produits Scellés

> ⚠️ **AVERTISSEMENT STATISTIQUE & TAUX EXPÉRIMENTAUX :**
> Disney Lorcana™ et toutes les marques associées sont la propriété de Disney et Ravensburger.
> **Ravensburger ne publie pas de probabilités ou de pourcentages officiels d'apparition des cartes.**
> Tous les taux, probabilités et calculs présentés dans ce document sont des estimations expérimentales élaborées par la communauté internationale (études empiriques sur plus de 44 displays documentées par *The Gamers Lodge* et discussions sur *Reddit r/Lorcana*) combinées à la loi binomiale.

---

## 1. Ressource Éducative Recommandée : Reddit r/Lorcana (Educational)
Pour des analyses approfondies des règles, des statistiques de tournois et des études d'ouverture de caisses :
👉 [**Reddit r/Lorcana — Flair Educational**](https://www.reddit.com/r/Lorcana/?f=flair_name%3A%22Educational%22)

---

## 2. Anatomie d'un Booster et Symboles Officiels des Raretés

Chaque booster standard contient **12 cartes** :
- **Slots 1 – 6 (6 Cartes) :** Communes garanties.
- **Slots 7 – 9 (3 Cartes) :** Inhabituelles garanties.
- **Slots 10 – 11 (2 Cartes) :** Rare, Très Rare, Épique (Set 9+) ou Légendaire.
- **Slot 12 (1 Carte Foil Garantie) :** Toute carte du set en version brillante (Foil), incluant les **Enchantées (Enchanted)** et **Iconiques (Iconic)**.

| Symbole Géométrique | Rareté | Slot | Fréquence Moyenne Estimée |
| :--- | :--- | :--- | :--- |
| **⚪ Cercle Gris** | Commune (Common) | 1 – 6 | 6 par booster (100%) |
| **📖 Livre Blanc** | Inhabituelle (Uncommon) | 7 – 9 | 3 par booster (100%) |
| **🔺 Triangle Bronze** | Rare | 10 – 11 | ~1,5 par booster |
| **🔷 Diamant Argent** | Très Rare (Super Rare) | 10 – 11 | 1 tous les 2 à 3 boosters (~12-14 par display) |
| **🪭 Éventail Arc-en-ciel** | Épique (Epic) *(Set 9+)* | 10 – 11 ou Foil (12) | **1 tous les 16 boosters** (~1,5 - 2,5 par display) |
| **🟡 Pentagone Doré** | Légendaire (Legendary) | 10 – 11 | 1 tous les 5 à 6 boosters (~4 - 6 par display) |
| **✨ Hexagone Arc-en-ciel** | Enchantée (Enchanted) | 12 (Foil) | **1 tous les 96 boosters** (~1 par Case de 4 displays) |
| **👑 Sceau Iconique** | Iconique (Iconic Chase) *(Set 13+)* | 12 (Foil) | **1 tous les ~384 à 1 500 boosters** |

---

## 3. Comparaison Set par Set : L'Évolution à travers les 3 Ères

### 🏛️ 1. L'Ère Classique (Sets 1–4)
*Le Premier Chapitre, L'Ascension des Floodborn, Les Terres d'Encres, Le Retour d'Ursula.*
- **Les Maths :** 4 à 5 Légendaires par display. Les Enchantées étaient strictement à 1 pour 96 boosters (1 par carton scellé de 4 displays).

### 🌿 2. L'Ère de l'Expansion (Sets 5–8)
*Ciel Scintillant, La Mer Azurite, L'Île d'Archazia, Le Règne de Jafar.*
- **Les Maths :** Introduction des Lieux (Locations). Taux stable à ~5 Légendaires par display.

### 👑 3. L'Ère Moderne (Set 9+)
*Fables, Lueurs dans les Profondeurs, Sorts d'Hiver, Terres Sauvages, L'Attaque de la Vigne, Hyperia City.*
- **Cartes Épiques (🟣) :** Environ 1 tous les 16 boosters (~2,5 par display).
- **Cartes Iconiques (👑) :** Le nouveau Saint Graal en Slot 12 Foil.
- **Légendaires en hausse :** Jusqu'à 5,5 - 6 par display (269 Légendaires sur 44 displays dans *Hyperia City*).

---

## 4. La Hiérarchie des « God Packs »
1. **The Double Hit :** 2 Légendaires dans les slots 10 et 11 (~1 sur 35 boosters).
2. **The Triple Hit :** 2 Légendaires + 1 Légendaire Foil en slot 12.
3. **The Ultimate Pull :** 2 Légendaires (slots 10-11) + 1 Iconique ou Enchantée en slot 12 !

---

## 5. Application Officielle Companion
- **Application Officielle :** [Page Officielle Ravensburger](https://www.disneylorcana.com/it-IT/app) · [Télécharger sur iOS (App Store)](https://apps.apple.com/us/app/disney-lorcana-tcg-companion/id6444333831) · [Télécharger sur Android (Google Play)](https://play.google.com/store/apps/details?id=com.ravensburger.disney.lorcana&hl=en_US)
"""
    with open("docs/cards-and-rarities/pull-rates-and-products.fr.md", "w", encoding="utf-8") as f:
        f.write(fr_content)

    # German
    de_content = """# Vollständiger Leitfaden zu Pull Rates, Seltenheiten, den 3 Ären & Versiegelten Produkten

> ⚠️ **STATISTISCHER HINWEIS & EXPERIMENTELLE PULL RATES:**
> Disney Lorcana™ und alle zugehörigen Marken sind Eigentum von Disney und Ravensburger.
> **Ravensburger veröffentlicht keine offiziellen Ziehungsraten oder Wahrscheinlichkeiten.**
> Alle hier aufgeführten Wahrscheinlichkeiten basieren auf experimentellen Auswertungen der internationalen Community (Mass-Openings von 44+ Displays durch *The Gamers Lodge* sowie Analysen auf *Reddit r/Lorcana*) und Binomialverteilungsmodellen.

---

## 1. Empfohlene Lernressource: Reddit r/Lorcana (Educational)
Für komplexe Regelfragen, Turnierstatistiken und empirische Display-Studien:
👉 [**Reddit r/Lorcana — Flair Educational**](https://www.reddit.com/r/Lorcana/?f=flair_name%3A%22Educational%22)

---

## 2. Booster-Aufbau & Offizielle Seltenheitssymbole

Jedes Standard-Boosterpack enthält **12 Karten**:
- **Slots 1 – 6 (6 Karten):** Garantierte Gewöhnliche (Common).
- **Slots 7 – 9 (3 Karten):** Garantierte Ungewöhnliche (Uncommon).
- **Slots 10 – 11 (2 Karten):** Selten, Episch Selten, Episch (ab Set 9+) oder Legendär.
- **Slot 12 (1 Garantierte Foil-Karte):** Beliebige Foil-Karte des Sets, inkl. Chance auf **Verzauberte (Enchanted)** oder **Ikonische (Iconic)** Chase-Karten.

| Geometrisches Symbol | Seltenheit | Pack-Slot | Geschätzte Häufigkeit |
| :--- | :--- | :--- | :--- |
| **⚪ Grauer Kreis** | Gewöhnlich (Common) | 1 – 6 | 6 pro Booster (100%) |
| **📖 Weißes Buch** | Ungewöhnlich (Uncommon) | 7 – 9 | 3 pro Booster (100%) |
| **🔺 Bronzenes Dreieck** | Selten (Rare) | 10 – 11 | ~1,5 pro Booster |
| **🔷 Silberner Diamant** | Episch Selten (Super Rare) | 10 – 11 | 1 in 2 bis 3 Boostern (~12-14 pro Display) |
| **🪭 Regenbogen-Fächer** | Episch (Epic) *(Set 9+)* | 10 – 11 oder Foil (12) | **1 in 16 Boostern** (~1,5 - 2,5 pro Display) |
| **🟡 Goldenes Fünfeck** | Legendär (Legendary) | 10 – 11 | 1 in 5 bis 6 Boostern (~4 - 6 pro Display) |
| **✨ Regenbogen-Sechseck** | Verzaubert (Enchanted) | 12 (Foil) | **1 in 96 Boostern** (~1 pro 4er-Display-Case) |
| **👑 Ikonisches Siegel** | Ikonisch (Iconic Chase) *(Set 13+)* | 12 (Foil) | **1 in ~384 bis 1.500 Boostern** |

---

## 3. Set-für-Set-Vergleich: Die Evolution durch 3 Ären

### 🏛️ 1. Die Klassische Ära (Sets 1–4)
*Das Erste Kapitel, Aufstieg der Flutgestalten, Die Tintenlande, Ursulas Rückkehr.*
- **Die Mathematik:** 4 bis 5 Legendäre pro Display. Verzauberte lagen strikt bei 1 pro 96 Boostern (1 pro versiegeltem Case).

### 🌿 2. Die Expansions-Ära (Sets 5–8)
*Himmelsleuchten, Azurblaues Meer, Archazias Insel, Jafars Herrschaft.*
- **Die Mathematik:** Einführung von Orten (Locations). Konstant ~5 Legendäre pro Display.

### 👑 3. Die Moderne Ära (Ab Set 9+)
*Fables of Light, Wilds Unknown, Attack of the Vine, Hyperia City.*
- **Epische Karten (🟣):** Etwa 1 in 16 Boostern (~2,5 pro Display).
- **Ikonische Karten (👑):** Der neue Heilige Gral in Slot 12 Foil.
- **Erhöhte Legendäre-Rate:** 5,5 bis 6 pro Display (269 Legendäre in 44 Displays bei *Hyperia City*).

---

## 4. Die Hierarchie der „God Packs“
1. **The Double Hit:** 2 Legendäre in Slot 10 und 11 (~1 in 35 Boostern).
2. **The Triple Hit:** 2 Legendäre + 1 Foil-Legendäre in Slot 12.
3. **The Ultimate Pull:** 2 Legendäre (Slot 10-11) + 1 Ikonische oder Verzauberte in Slot 12!

---

## 5. Offizielle Companion App
- **Offizielle App:** [Offizielle Ravensburger-Seite](https://www.disneylorcana.com/it-IT/app) · [iOS Download (App Store)](https://apps.apple.com/us/app/disney-lorcana-tcg-companion/id6444333831) · [Android Download (Google Play)](https://play.google.com/store/apps/details?id=com.ravensburger.disney.lorcana&hl=en_US)
"""
    with open("docs/cards-and-rarities/pull-rates-and-products.de.md", "w", encoding="utf-8") as f:
        f.write(de_content)

    # Spanish
    es_content = """# Guía Completa de Pull Rates, Rarezas, Evolución de las 3 Eras y Productos Sellados

> ⚠️ **AVISO ESTADÍSTICO Y TASAS EXPERIMENTALES:**
> Disney Lorcana™ y todas las marcas asociadas son propiedad de Disney y Ravensburger.
> **Ravensburger no publica probabilidades ni porcentajes oficiales de aparición.**
> Todas las tasas y probabilidades en esta guía son estimaciones experimentales de la comunidad global (estudios empíricos de 44+ cajas por *The Gamers Lodge* y análisis en *Reddit r/Lorcana*) combinadas con distribución binomial.

---

## 1. Recurso Educativo Recomendado: Reddit r/Lorcana (Educational)
Para análisis profundos de reglas, estadísticas de torneos y estudios de apertura masiva:
👉 [**Reddit r/Lorcana — Etiqueta Educational**](https://www.reddit.com/r/Lorcana/?f=flair_name%3A%22Educational%22)

---

## 2. Anatomía del Sobre y Símbolos Oficiales de Rareza

Cada sobre estándar contiene **12 cartas**:
- **Slots 1 – 6 (6 Cartas):** Comunes garantizadas.
- **Slots 7 – 9 (3 Cartas):** Poco Comunes garantizadas.
- **Slots 10 – 11 (2 Cartas):** Rara, Súper Rara, Épica (Set 9+) o Legendaria.
- **Slot 12 (1 Carta Foil Garantizada):** Cualquier carta del set en versión foil, con posibilidad de **Encantada (Enchanted)** o **Icónica (Iconic)**.

| Símbolo Geométrico | Rareza | Posición | Frecuencia Media Estimada |
| :--- | :--- | :--- | :--- |
| **⚪ Círculo Gris** | Común (Common) | 1 – 6 | 6 por sobre (100%) |
| **📖 Libro Blanco** | Poco Común (Uncommon) | 7 – 9 | 3 por sobre (100%) |
| **🔺 Triángulo Bronce** | Rara (Rare) | 10 – 11 | ~1,5 por sobre |
| **🔷 Diamante Plata** | Súper Rara (Super Rare) | 10 – 11 | 1 cada 2 o 3 sobres (~12-14 por caja) |
| **🪭 Abanico Arcoíris** | Épica (Epic) *(Set 9+)* | 10 – 11 o Foil (12) | **1 cada 16 sobres** (~1,5 - 2,5 por caja) |
| **🟡 Pentágono Dorado** | Legendaria (Legendary) | 10 – 11 | 1 cada 5 o 6 sobres (~4 - 6 por caja) |
| **✨ Hexágono Arcoíris** | Encantada (Enchanted) | 12 (Foil) | **1 cada 96 sobres** (~1 por Case de 4 cajas) |
| **👑 Sello Icónico** | Icónica (Iconic Chase) *(Set 13+)* | 12 (Foil) | **1 cada ~384 a 1.500 sobres** |

---

## 3. Comparación Set por Set: Evolución en las 3 Eras

### 🏛️ 1. La Era Clásica (Sets 1–4)
*El Primer Capítulo, El Ascenso de los Floodborn, Hacia las Tierras de Tinta, El Regreso de Úrsula.*
- **Las Matemáticas:** 4 a 5 Legendarias por caja. Encantadas estrictamente a 1 cada 96 sobres (1 por Case sellado de 4 cajas).

### 🌿 2. La Era de la Expansión (Sets 5–8)
*Cielos Resplandecientes, Mar Azurita, La Isla de Archazia, El Reinado de Jafar.*
- **Las Matemáticas:** Introducción de Lugares (Locations). Tasa estable de ~5 Legendarias por caja.

### 👑 3. La Era Moderna (Set 9+)
*Fables of Light, Wilds Unknown, Attack of the Vine, Hyperia City.*
- **Cartas Épicas (🟣):** Aproximadamente 1 cada 16 sobres (~2,5 por caja).
- **Cartas Icónicas (👑):** El nuevo Santo Grial en el Slot 12 Foil.
- **Más Legendarias:** 5,5 a 6 por caja (269 Legendarias en 44 cajas de *Hyperia City*).

---

## 4. La Jerarquía de los «God Packs»
1. **The Double Hit:** 2 Legendarias en los slots 10 y 11 (~1 cada 35 sobres).
2. **The Triple Hit:** 2 Legendarias + 1 Legendaria Foil en el slot 12.
3. **The Ultimate Pull:** 2 Legendarias (slots 10-11) + 1 Icónica o Encantada en el slot 12.

---

## 5. Aplicación Oficial Companion
- **App Oficial Companion:** [Página Oficial Ravensburger](https://www.disneylorcana.com/it-IT/app) · [Descargar en iOS (App Store)](https://apps.apple.com/us/app/disney-lorcana-tcg-companion/id6444333831) · [Descargar en Android (Google Play)](https://play.google.com/store/apps/details?id=com.ravensburger.disney.lorcana&hl=en_US)
"""
    with open("docs/cards-and-rarities/pull-rates-and-products.es.md", "w", encoding="utf-8") as f:
        f.write(es_content)
    print("Created pull-rates-and-products in FR, DE, ES!")


def create_deck_building_docs():
    fr_deck = """# Guide de Construction de Deck, Courbe d'Encre et Simulateurs en Ligne

Guide complet pour construire un deck compétitif de 60 cartes à Disney Lorcana et le tester sur notre **[Deck Lab](../deck-lab.html)** ainsi que sur les plateformes communautaires.

## 1. Règles Fondamentales de Construction
- **Minimum 60 cartes** (jouer exactement 60 cartes maximise la régularité statistique).
- **Maximum 2 couleurs d'encre** par deck.
- **Maximum 4 exemplaires** d'une carte portant exactement le même nom complet (Nom + Sous-titre).
- **Seuil de cartes Non-Encrables (Uninkables) :** Idéalement entre **8 et 14 maximum** pour éviter les mains bloquées.

## 2. Plateformes de Test & Simulateurs
- **[Deck Lab & Goldfish Playtester](../deck-lab.html) :** Constructeur intégré avec base de données des 14 Sets et testeur de main de départ.
- **[Duels.ink](https://duels.ink/) :** Simulateur automatisé dans le navigateur.
- **[Inktable.net](https://www.inktable.net/) :** Testez vos decks contre une IA intelligente.
- **[Dreamborn.ink](https://dreamborn.ink/) :** Gestionnaire de decks et de collection.
"""
    with open("docs/decks/deck-building-and-testing.fr.md", "w", encoding="utf-8") as f:
        f.write(fr_deck)

    de_deck = """# Leitfaden zum Deckbau, Tintenkurve & Online-Simulatoren

Vollständiger Leitfaden für den Bau eines turnierfähigen 60-Karten-Decks in Disney Lorcana und das Testen im **[Deck Lab](../deck-lab.html)**.

## 1. Grundregeln des Deckbaus
- **Mindestens 60 Karten** (exakt 60 Karten für maximale Konsistenz empfohlen).
- **Maximal 2 Tintenfarben** pro Deck.
- **Maximal 4 Kopien** derselben Karte (gleicher Name + Untertitel).
- **Limit für Nicht-Tintenbare Karten (Uninkables):** Maximal **8 bis 14 Karten**, um Tintenprobleme zu vermeiden.

## 2. Test-Plattformen & Simulatoren
- **[Deck Lab & Goldfish Playtester](../deck-lab.html):** Integrierter Builder mit allen 14 Sets und Starthand-Simulator.
- **[Duels.ink](https://duels.ink/):** Browserbasierter Wettkampf-Simulator.
- **[Inktable.net](https://www.inktable.net/):** Spiele gegen eine KI zum Testen deiner Kurve.
- **[Dreamborn.ink](https://dreamborn.ink/):** Deck-Datenbank und Sammlungsverwaltung.
"""
    with open("docs/decks/deck-building-and-testing.de.md", "w", encoding="utf-8") as f:
        f.write(de_deck)

    es_deck = """# Guía de Construcción de Mazos, Curva de Tinta y Simuladores Online

Guía completa para construir un mazo competitivo de 60 cartas en Disney Lorcana y probarlo en nuestro **[Deck Lab](../deck-lab.html)**.

## 1. Reglas Fundamentales de Construcción
- **Mínimo 60 cartas** (se recomienda exactamente 60 cartas para máxima consistencia).
- **Máximo 2 colores de tinta** por mazo.
- **Máximo 4 copias** de una carta con el mismo nombre completo (Nombre + Subtítulo).
- **Límite de cartas No-Entintables (Uninkables):** Entre **8 y 14 como máximo**.

## 2. Plataformas de Prueba y Simuladores
- **[Deck Lab & Goldfish Playtester](../deck-lab.html):** Constructor integrado con los 14 Sets y simulador de mano inicial.
- **[Duels.ink](https://duels.ink/):** Simulador competitivo en el navegador.
- **[Inktable.net](https://www.inktable.net/):** Juega contra la IA para probar tus turnos.
- **[Dreamborn.ink](https://dreamborn.ink/):** Base de datos de mazos y colección.
"""
    with open("docs/decks/deck-building-and-testing.es.md", "w", encoding="utf-8") as f:
        f.write(es_deck)
    print("Created deck-building-and-testing in FR, DE, ES!")


def upgrade_localized_readmes():
    readmes = {
        "README.fr.md": """# ✦ Disney Lorcana — Portail Communautaire & Encyclopédie (Édition Française)

[![Disney Lorcana](https://img.shields.io/badge/TCG-Disney%20Lorcana-blueviolet.svg)](https://www.disneylorcana.com/)
[![GitHub Pages](https://img.shields.io/badge/Web%20Portal-Live%205%20Languages-ffd700.svg)](https://mrjonam91.github.io/disney-lorcana-companion/)

Bienvenue sur l'édition française du référentiel communautaire **Disney Lorcana**. Toutes les pages web et applications supportent désormais les 5 langues (**IT, EN, FR, DE, ES**).

## 🎮 Applications Web Interactives (Effets Foil CSS & 5 Langues)
- **[🌐 Portail Central Multilingue (index.html)](index.html?lang=fr)**
- **[🃏 Deck Lab & Playtester Goldfish (deck-lab.html)](deck-lab.html?lang=fr)** : Créateur de deck 60 cartes (Sets 1 à 14), courbe d'encre, testeur de mulligan et export vers **duels.ink**, **inktable.net** et **dreamborn.ink**.
- **[💎 Collector's Vault & Simulateur de Boosters (collector-vault.html)](collector-vault.html?lang=fr)** : Simulateur d'ouverture avec effets Foil 3D, quantité personnalisée (1 à 10 000 boosters), cartes Épiques (🟣) et Iconiques (👑), guide des 3 Ères et calculateur binomial.
- **[📖 Guide Interactif Français (lorcana-guide-fr.html)](guide/lorcana-guide-fr.html)**

## 📚 Documentation Complète en Français
- [Historique et Analyse des 14 Sets](docs/sets/set-history.fr.md)
- [Guide des Cartes et Raretés](docs/cards-and-rarities/rarities-guide.fr.md)
- [Taux de Drop (Pull Rates), 3 Ères & Produits Scellés](docs/cards-and-rarities/pull-rates-and-products.fr.md)
- [Règles Officielles Complètes](docs/rules/complete-rules.fr.md)
- [Stratégie et Mathématiques du Mulligan](docs/strategy/mulligan-and-math.fr.md)
- [Construction de Deck & Simulateurs](docs/decks/deck-building-and-testing.fr.md)
- [Deck Débutant Mickey & Minnie (Émeraude/Saphir)](docs/decks/starter-emerald-sapphire.fr.md)
- [Glossaire Multilingue](docs/glossary/glossary.fr.md)

## 📱 Application Officielle Ravensburger
- [Page Officielle Disney Lorcana App](https://www.disneylorcana.com/it-IT/app) · [iOS App Store](https://apps.apple.com/us/app/disney-lorcana-tcg-companion/id6444333831) · [Google Play Store](https://play.google.com/store/apps/details?id=com.ravensburger.disney.lorcana&hl=en_US)
""",
        "README.de.md": """# ✦ Disney Lorcana — Community-Portal & Enzyklopädie (Deutsche Ausgabe)

[![Disney Lorcana](https://img.shields.io/badge/TCG-Disney%20Lorcana-blueviolet.svg)](https://www.disneylorcana.com/)
[![GitHub Pages](https://img.shields.io/badge/Web%20Portal-Live%205%20Languages-ffd700.svg)](https://mrjonam91.github.io/disney-lorcana-companion/)

Willkommen zur deutschen Ausgabe des **Disney Lorcana** Community-Portals. Alle Web-Apps unterstützen alle 5 Sprachen (**IT, EN, FR, DE, ES**).

## 🎮 Interaktive Web-Apps (Holografische Foil-Effekte & 5 Sprachen)
- **[🌐 Zentrales Mehrsprachiges Portal (index.html)](index.html?lang=de)**
- **[🃏 Deck Lab & Goldfish-Playtester (deck-lab.html)](deck-lab.html?lang=de)** : 60-Karten-Deckbuilder (Set 1 bis 14), Tintenkurve, Mulligan-Simulator und Export für **duels.ink**, **inktable.net** und **dreamborn.ink**.
- **[💎 Collector's Vault & Booster-Simulator (collector-vault.html)](collector-vault.html?lang=de)** : Holografischer Booster-Simulator mit freier Anzahl (1 bis 10.000 Booster), Episch (🟣) & Ikonisch (👑), 3-Ären-Vergleich und Binomial-Rechner.
- **[📖 Interaktiver Deutscher Leitfaden (lorcana-guide-de.html)](guide/lorcana-guide-de.html)**

## 📚 Vollständige Dokumentation auf Deutsch
- [Historie & Analyse aller 14 Sets](docs/sets/set-history.de.md)
- [Karten & Seltenheiten Leitfaden](docs/cards-and-rarities/rarities-guide.de.md)
- [Pull Rates, 3 Ären & Produktkatalog](docs/cards-and-rarities/pull-rates-and-products.de.md)
- [Offizielles Regelwerk & Kurzübersicht](docs/rules/complete-rules.de.md)
- [Strategie & Mulligan-Mathematik](docs/strategy/mulligan-and-math.de.md)
- [Deckbau & Online-Simulatoren](docs/decks/deck-building-and-testing.de.md)
- [Einsteigerdeck Micky & Minnie (Smaragd/Saphir)](docs/decks/starter-emerald-sapphire.de.md)
- [Mehrsprachiges Glossar](docs/glossary/glossary.de.md)

## 📱 Offizielle Ravensburger Companion App
- [Offizielle Disney Lorcana App-Seite](https://www.disneylorcana.com/it-IT/app) · [iOS App Store](https://apps.apple.com/us/app/disney-lorcana-tcg-companion/id6444333831) · [Google Play Store](https://play.google.com/store/apps/details?id=com.ravensburger.disney.lorcana&hl=en_US)
""",
        "README.es.md": """# ✦ Disney Lorcana — Portal de la Comunidad y Enciclopedia (Edición en Español)

[![Disney Lorcana](https://img.shields.io/badge/TCG-Disney%20Lorcana-blueviolet.svg)](https://www.disneylorcana.com/)
[![GitHub Pages](https://img.shields.io/badge/Web%20Portal-Live%205%20Languages-ffd700.svg)](https://mrjonam91.github.io/disney-lorcana-companion/)

Bienvenido a la edición en español del portal comunitario de **Disney Lorcana**. Todas las aplicaciones web son compatibles con los 5 idiomas (**IT, EN, FR, DE, ES**).

## 🎮 Aplicaciones Web Interactivas (Efectos Foil CSS y 5 Idiomas)
- **[🌐 Portal Central Multilingüe (index.html)](index.html?lang=es)**
- **[🃏 Deck Lab y Playtester Goldfish (deck-lab.html)](deck-lab.html?lang=es)** : Constructor de mazos de 60 cartas (Sets 1 a 14), curva de tinta, simulador de mulligan y exportación a **duels.ink**, **inktable.net** y **dreamborn.ink**.
- **[💎 Collector's Vault y Simulador de Sobres (collector-vault.html)](collector-vault.html?lang=es)** : Simulador holográfico con cantidad personalizada (1 a 10.000 sobres), cartas Épicas (🟣) e Icónicas (👑), guía de las 3 Eras y calculadora binomial.
- **[📖 Guía Interactiva en Español (lorcana-guide-es.html)](guide/lorcana-guide-es.html)**

## 📚 Documentación Completa en Español
- [Historia y Análisis de los 14 Sets](docs/sets/set-history.es.md)
- [Guía de Cartas y Rarezas](docs/cards-and-rarities/rarities-guide.es.md)
- [Pull Rates, 3 Eras y Catálogo de Productos](docs/cards-and-rarities/pull-rates-and-products.es.md)
- [Reglamento Oficial Completo](docs/rules/complete-rules.es.md)
- [Estrategia y Matemáticas del Mulligan](docs/strategy/mulligan-and-math.es.md)
- [Construcción de Mazos y Simuladores](docs/decks/deck-building-and-testing.es.md)
- [Mazo de Inicio Mickey y Minnie (Esmeralda/Zafiro)](docs/decks/starter-emerald-sapphire.es.md)
- [Glosario Multilingüe](docs/glossary/glossary.es.md)

## 📱 Aplicación Oficial de Ravensburger
- [Página Oficial Disney Lorcana App](https://www.disneylorcana.com/it-IT/app) · [iOS App Store](https://apps.apple.com/us/app/disney-lorcana-tcg-companion/id6444333831) · [Google Play Store](https://play.google.com/store/apps/details?id=com.ravensburger.disney.lorcana&hl=en_US)
"""
    }
    for fname, text in readmes.items():
        with open(fname, "w", encoding="utf-8") as f:
            f.write(text)
    print("Upgraded README.fr.md, README.de.md, README.es.md!")

if __name__ == "__main__":
    create_pull_rates_docs()
    create_deck_building_docs()
    upgrade_localized_readmes()
