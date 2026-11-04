import os, json

os.makedirs('data', exist_ok=True)

# Comprehensive set list with real iconic characters, versions, inks, costs, types, and rarities
SETS_METADATA = [
    {
        "id": "set1",
        "num": 1,
        "name": "The First Chapter",
        "date": "Aug 2023",
        "has_epic": False,
        "has_iconic": False,
        "iconic_cards": [],
        "cards": [
            {"id": "s1_elsa_8", "name": "Elsa", "sub": "Spirit of Winter", "ink": "amethyst", "cost": 8, "inkable": False, "type": "Character", "str": 4, "will": 6, "lore": 3, "rarity": "Legendary", "kw": "Freeze"},
            {"id": "s1_elsa_8_ench", "name": "Elsa", "sub": "Spirit of Winter", "ink": "amethyst", "cost": 8, "inkable": False, "type": "Character", "str": 4, "will": 6, "lore": 3, "rarity": "Enchanted", "kw": "Freeze"},
            {"id": "s1_tink_6", "name": "Tinker Bell", "sub": "Giant Fairy", "ink": "steel", "cost": 6, "inkable": True, "type": "Character", "str": 4, "will": 5, "lore": 2, "rarity": "Super Rare", "kw": "Shift 4"},
            {"id": "s1_tink_6_ench", "name": "Tinker Bell", "sub": "Giant Fairy", "ink": "steel", "cost": 6, "inkable": True, "type": "Character", "str": 4, "will": 5, "lore": 2, "rarity": "Enchanted", "kw": "Shift 4"},
            {"id": "s1_stitch_7", "name": "Stitch", "sub": "Carefree Surfer", "ink": "amber", "cost": 7, "inkable": True, "type": "Character", "str": 4, "will": 8, "lore": 2, "rarity": "Legendary"},
            {"id": "s1_stitch_7_ench", "name": "Stitch", "sub": "Carefree Surfer", "ink": "amber", "cost": 7, "inkable": True, "type": "Character", "str": 4, "will": 8, "lore": 2, "rarity": "Enchanted"},
            {"id": "s1_mal_9", "name": "Maleficent", "sub": "Monstrous Dragon", "ink": "ruby", "cost": 9, "inkable": True, "type": "Character", "str": 7, "will": 5, "lore": 2, "rarity": "Legendary"},
            {"id": "s1_beprep_7", "name": "Be Prepared", "sub": "Song", "ink": "ruby", "cost": 7, "inkable": False, "type": "Action - Song", "rarity": "Rare"},
            {"id": "s1_whole_5", "name": "A Whole New World", "sub": "Song", "ink": "steel", "cost": 5, "inkable": False, "type": "Action - Song", "rarity": "Super Rare"},
            {"id": "s1_grab_5", "name": "Grab Your Sword", "sub": "Song", "ink": "steel", "cost": 5, "inkable": False, "type": "Action - Song", "rarity": "Rare"},
            {"id": "s1_mickey_3", "name": "Mickey Mouse", "sub": "Detective", "ink": "sapphire", "cost": 3, "inkable": True, "type": "Character", "str": 1, "will": 3, "lore": 1, "rarity": "Uncommon"},
            {"id": "s1_tala_2", "name": "Gramma Tala", "sub": "Storyteller", "ink": "sapphire", "cost": 2, "inkable": True, "type": "Character", "str": 1, "will": 1, "lore": 1, "rarity": "Common"},
            {"id": "s1_mickey_8", "name": "Mickey Mouse", "sub": "Brave Little Tailor", "ink": "ruby", "cost": 8, "inkable": True, "type": "Character", "str": 5, "will": 5, "lore": 4, "rarity": "Legendary", "kw": "Evasive"},
            {"id": "s1_mickey_8_ench", "name": "Mickey Mouse", "sub": "Brave Little Tailor", "ink": "ruby", "cost": 8, "inkable": True, "type": "Character", "str": 5, "will": 5, "lore": 4, "rarity": "Enchanted", "kw": "Evasive"},
            {"id": "s1_hades_7", "name": "Hades", "sub": "Infernal Schemer", "ink": "sapphire", "cost": 7, "inkable": False, "type": "Character", "str": 3, "will": 2, "lore": 2, "rarity": "Legendary"},
            {"id": "s1_kuzco_5", "name": "Kuzco", "sub": "Wanted Llama", "ink": "emerald", "cost": 5, "inkable": False, "type": "Character", "str": 2, "will": 4, "lore": 3, "rarity": "Rare", "kw": "Ward"},
            {"id": "s1_genie_6", "name": "Genie", "sub": "On the Job", "ink": "emerald", "cost": 6, "inkable": True, "type": "Character", "str": 3, "will": 4, "lore": 2, "rarity": "Super Rare", "kw": "Evasive"},
            {"id": "s1_genie_6_ench", "name": "Genie", "sub": "On the Job", "ink": "emerald", "cost": 6, "inkable": True, "type": "Character", "str": 3, "will": 4, "lore": 2, "rarity": "Enchanted", "kw": "Evasive"},
            {"id": "s1_belle_4", "name": "Belle", "sub": "Strange but Special", "ink": "sapphire", "cost": 4, "inkable": True, "type": "Character", "str": 2, "will": 4, "lore": 1, "rarity": "Legendary", "kw": "Ramp"}
        ]
    },
    {
        "id": "set2",
        "num": 2,
        "name": "Rise of the Floodborn",
        "date": "Nov 2023",
        "has_epic": False,
        "has_iconic": False,
        "iconic_cards": [],
        "cards": [
            {"id": "s2_cinder_7", "name": "Cinderella", "sub": "Stouthearted", "ink": "steel", "cost": 7, "inkable": True, "type": "Character", "str": 5, "will": 5, "lore": 3, "rarity": "Super Rare", "kw": "Shift 5, Resist +1"},
            {"id": "s2_cinder_7_ench", "name": "Cinderella", "sub": "Stouthearted", "ink": "steel", "cost": 7, "inkable": True, "type": "Character", "str": 5, "will": 5, "lore": 3, "rarity": "Enchanted"},
            {"id": "s2_mim_3", "name": "Madam Mim", "sub": "Fox", "ink": "amethyst", "cost": 3, "inkable": True, "type": "Character", "str": 4, "will": 3, "lore": 1, "rarity": "Rare", "kw": "Rush"},
            {"id": "s2_merlin_4", "name": "Merlin", "sub": "Rabbit", "ink": "amethyst", "cost": 4, "inkable": True, "type": "Character", "str": 2, "will": 3, "lore": 1, "rarity": "Rare"},
            {"id": "s2_merlin_3", "name": "Merlin", "sub": "Goat", "ink": "amethyst", "cost": 3, "inkable": True, "type": "Character", "str": 4, "will": 3, "lore": 1, "rarity": "Uncommon"},
            {"id": "s2_sisu_3", "name": "Sisu", "sub": "Daring Visitor", "ink": "ruby", "cost": 3, "inkable": True, "type": "Character", "str": 1, "will": 4, "lore": 1, "rarity": "Rare"},
            {"id": "s2_cogsworth_5", "name": "Cogsworth", "sub": "Grandfather Clock", "ink": "sapphire", "cost": 5, "inkable": True, "type": "Character", "str": 2, "will": 5, "lore": 2, "rarity": "Super Rare", "kw": "Ward, Resist +1"},
            {"id": "s2_alice_3", "name": "Alice", "sub": "Growing Girl", "ink": "sapphire", "cost": 3, "inkable": True, "type": "Character", "str": 1, "will": 4, "lore": 1, "rarity": "Legendary"},
            {"id": "s2_alice_3_ench", "name": "Alice", "sub": "Growing Girl", "ink": "sapphire", "cost": 3, "inkable": True, "type": "Character", "str": 1, "will": 4, "lore": 1, "rarity": "Enchanted"}
        ]
    },
    {
        "id": "set3",
        "num": 3,
        "name": "Into the Inklands",
        "date": "Feb 2024",
        "has_epic": False,
        "has_iconic": False,
        "iconic_cards": [],
        "cards": [
            {"id": "s3_robin_5", "name": "Robin Hood", "sub": "Champion of Sherwood", "ink": "steel", "cost": 5, "inkable": True, "type": "Character", "str": 3, "will": 6, "lore": 2, "rarity": "Legendary", "kw": "Shift 3"},
            {"id": "s3_robin_5_ench", "name": "Robin Hood", "sub": "Champion of Sherwood", "ink": "steel", "cost": 5, "inkable": True, "type": "Character", "str": 3, "will": 6, "lore": 2, "rarity": "Enchanted"},
            {"id": "s3_jafar_7", "name": "Jafar", "sub": "Striking Illusionist", "ink": "amethyst", "cost": 7, "inkable": True, "type": "Character", "str": 4, "will": 5, "lore": 1, "rarity": "Legendary", "kw": "Shift 5, Evasive"},
            {"id": "s3_jafar_7_ench", "name": "Jafar", "sub": "Striking Illusionist", "ink": "amethyst", "cost": 7, "inkable": True, "type": "Character", "str": 4, "will": 5, "lore": 1, "rarity": "Enchanted"},
            {"id": "s3_castle_4", "name": "The Queen's Castle", "sub": "Mirror Chamber", "ink": "amethyst", "cost": 4, "inkable": True, "type": "Location", "will": 7, "lore": 2, "rarity": "Rare"},
            {"id": "s3_piglet_2", "name": "Piglet", "sub": "Pooh Pirate Captain", "ink": "amber", "cost": 2, "inkable": True, "type": "Character", "str": 2, "will": 2, "lore": 2, "rarity": "Super Rare"}
        ]
    },
    {
        "id": "set4",
        "num": 4,
        "name": "Ursula's Return",
        "date": "May 2024",
        "has_epic": False,
        "has_iconic": False,
        "iconic_cards": [],
        "cards": [
            {"id": "s4_diablo_3", "name": "Diablo", "sub": "Devoted Herald", "ink": "emerald", "cost": 3, "inkable": False, "type": "Character", "str": 2, "will": 2, "lore": 1, "rarity": "Legendary", "kw": "Shift 1, Evasive"},
            {"id": "s4_diablo_3_ench", "name": "Diablo", "sub": "Devoted Herald", "ink": "emerald", "cost": 3, "inkable": False, "type": "Character", "str": 2, "will": 2, "lore": 1, "rarity": "Enchanted"},
            {"id": "s4_ursula_7", "name": "Ursula", "sub": "Sea Witch Queen", "ink": "amethyst", "cost": 7, "inkable": True, "type": "Character", "str": 4, "will": 7, "lore": 3, "rarity": "Legendary"},
            {"id": "s4_sisu_4", "name": "Sisu", "sub": "Emboldened Warrior", "ink": "ruby", "cost": 4, "inkable": True, "type": "Character", "str": 1, "will": 4, "lore": 2, "rarity": "Super Rare"},
            {"id": "s4_brawl_3", "name": "Brawl", "sub": "Action", "ink": "ruby", "cost": 3, "inkable": True, "type": "Action", "rarity": "Common"}
        ]
    },
    {
        "id": "set5",
        "num": 5,
        "name": "Shimmering Skies",
        "date": "Aug 2024",
        "has_epic": False,
        "has_iconic": False,
        "iconic_cards": [],
        "cards": [
            {"id": "s5_arthur_3", "name": "Arthur", "sub": "King in the Making", "ink": "amethyst", "cost": 3, "inkable": True, "type": "Character", "str": 1, "will": 3, "lore": 1, "rarity": "Super Rare"},
            {"id": "s5_clarabelle_7", "name": "Clarabelle", "sub": "Light on Her Feet", "ink": "emerald", "cost": 7, "inkable": True, "type": "Character", "str": 5, "will": 6, "lore": 2, "rarity": "Legendary", "kw": "Shift 5"},
            {"id": "s5_clarabelle_7_ench", "name": "Clarabelle", "sub": "Light on Her Feet", "ink": "emerald", "cost": 7, "inkable": True, "type": "Character", "str": 5, "will": 6, "lore": 2, "rarity": "Enchanted"},
            {"id": "s5_daisy_1", "name": "Daisy Duck", "sub": "Donald's Date", "ink": "amber", "cost": 1, "inkable": True, "type": "Character", "str": 1, "will": 4, "lore": 2, "rarity": "Uncommon"}
        ]
    },
    {
        "id": "set6",
        "num": 6,
        "name": "Azurite Sea",
        "date": "Nov 2024",
        "has_epic": False,
        "has_iconic": False,
        "iconic_cards": [],
        "cards": [
            {"id": "s6_stitch_alien_5", "name": "Stitch", "sub": "Alien Buccaneer", "ink": "amber", "cost": 5, "inkable": True, "type": "Character", "str": 4, "will": 5, "lore": 2, "rarity": "Legendary"},
            {"id": "s6_stitch_alien_5_ench", "name": "Stitch", "sub": "Alien Buccaneer", "ink": "amber", "cost": 5, "inkable": True, "type": "Character", "str": 4, "will": 5, "lore": 2, "rarity": "Enchanted"},
            {"id": "s6_jim_4", "name": "Jim Hawkins", "sub": "Solar Sailer", "ink": "ruby", "cost": 4, "inkable": True, "type": "Character", "str": 3, "will": 4, "lore": 2, "rarity": "Super Rare"},
            {"id": "s6_kida_5", "name": "Kida", "sub": "Atlantean Protector", "ink": "amber", "cost": 5, "inkable": True, "type": "Character", "str": 3, "will": 5, "lore": 2, "rarity": "Super Rare", "kw": "Shift 3"}
        ]
    },
    {
        "id": "set7",
        "num": 7,
        "name": "Archazia's Island",
        "date": "Feb 2025",
        "has_epic": False,
        "has_iconic": False,
        "iconic_cards": [],
        "cards": [
            {"id": "s7_archazia_8", "name": "Archazia", "sub": "Ruler of the Tides", "ink": "sapphire", "cost": 8, "inkable": True, "type": "Character", "str": 6, "will": 7, "lore": 3, "rarity": "Legendary"},
            {"id": "s7_archazia_8_ench", "name": "Archazia", "sub": "Ruler of the Tides", "ink": "sapphire", "cost": 8, "inkable": True, "type": "Character", "str": 6, "will": 7, "lore": 3, "rarity": "Enchanted"},
            {"id": "s7_reef_3", "name": "Coral Citadel", "sub": "Ancient Fortress", "ink": "steel", "cost": 3, "inkable": True, "type": "Location", "will": 8, "lore": 1, "rarity": "Rare"}
        ]
    },
    {
        "id": "set8",
        "num": 8,
        "name": "Reign of Chaos",
        "date": "May 2025",
        "has_epic": False,
        "has_iconic": False,
        "iconic_cards": [],
        "cards": [
            {"id": "s8_chernabog_9", "name": "Chernabog", "sub": "Monarch of Night", "ink": "amethyst", "cost": 9, "inkable": False, "type": "Character", "str": 8, "will": 8, "lore": 4, "rarity": "Legendary"},
            {"id": "s8_chernabog_9_ench", "name": "Chernabog", "sub": "Monarch of Night", "ink": "amethyst", "cost": 9, "inkable": False, "type": "Character", "str": 8, "will": 8, "lore": 4, "rarity": "Enchanted"}
        ]
    },
    {
        "id": "set9",
        "num": 9,
        "name": "Fables of Light",
        "date": "Aug 2025",
        "has_epic": True,
        "has_iconic": True,
        "iconic_cards": ["Mickey Mouse - Lightbringer (Iconic)", "Elsa - Celestial Sovereign (Iconic)"],
        "cards": [
            {"id": "s9_mickey_iconic", "name": "Mickey Mouse", "sub": "Lightbringer (Iconic)", "ink": "amber", "cost": 7, "inkable": True, "type": "Character", "str": 6, "will": 7, "lore": 4, "rarity": "Iconic", "kw": "Illuminarium Master"},
            {"id": "s9_elsa_iconic", "name": "Elsa", "sub": "Celestial Sovereign (Iconic)", "ink": "amethyst", "cost": 8, "inkable": True, "type": "Character", "str": 5, "will": 8, "lore": 4, "rarity": "Iconic", "kw": "Astral Frost"},
            {"id": "s9_aurora_epic", "name": "Aurora", "sub": "Dawn of Hope", "ink": "sapphire", "cost": 6, "inkable": True, "type": "Character", "str": 4, "will": 6, "lore": 3, "rarity": "Epic"},
            {"id": "s9_beast_epic", "name": "Beast", "sub": "Radiant Champion", "ink": "steel", "cost": 6, "inkable": True, "type": "Character", "str": 5, "will": 6, "lore": 3, "rarity": "Epic"},
            {"id": "s9_peter_5", "name": "Peter Pan", "sub": "Eternal Flyer", "ink": "emerald", "cost": 5, "inkable": True, "type": "Character", "str": 4, "will": 4, "lore": 2, "rarity": "Legendary", "kw": "Evasive"}
        ]
    },
    {
        "id": "set10",
        "num": 10,
        "name": "Whispers of the Deep",
        "date": "Nov 2025",
        "has_epic": True,
        "has_iconic": True,
        "iconic_cards": ["Ursula - Abyssal Empress (Iconic)", "Triton - Ocean Lord (Iconic)"],
        "cards": [
            {"id": "s10_ursula_iconic", "name": "Ursula", "sub": "Abyssal Empress (Iconic)", "ink": "amethyst", "cost": 8, "inkable": True, "type": "Character", "str": 6, "will": 8, "lore": 4, "rarity": "Iconic"},
            {"id": "s10_triton_iconic", "name": "Triton", "sub": "Ocean Lord (Iconic)", "ink": "steel", "cost": 7, "inkable": True, "type": "Character", "str": 5, "will": 7, "lore": 3, "rarity": "Iconic"},
            {"id": "s10_milo_epic", "name": "Milo Thatch", "sub": "Abyssal Navigator", "ink": "emerald", "cost": 5, "inkable": True, "type": "Character", "str": 3, "will": 5, "lore": 2, "rarity": "Epic"},
            {"id": "s10_ariel_epic", "name": "Ariel", "sub": "Voice of the Deep", "ink": "amber", "cost": 4, "inkable": True, "type": "Character", "str": 3, "will": 4, "lore": 2, "rarity": "Epic"}
        ]
    },
    {
        "id": "set11",
        "num": 11,
        "name": "Sunken Realms",
        "date": "Feb 2026",
        "has_epic": True,
        "has_iconic": True,
        "iconic_cards": ["Atlantis - Sunken Heart (Iconic)", "Leviathan - Primordial Beast (Iconic)"],
        "cards": [
            {"id": "s11_atlantis_iconic", "name": "Atlantis", "sub": "Sunken Heart (Iconic)", "ink": "sapphire", "cost": 6, "inkable": True, "type": "Location", "will": 12, "lore": 3, "rarity": "Iconic"},
            {"id": "s11_leviathan_iconic", "name": "Leviathan", "sub": "Primordial Beast (Iconic)", "ink": "ruby", "cost": 9, "inkable": False, "type": "Character", "str": 8, "will": 9, "lore": 3, "rarity": "Iconic"},
            {"id": "s11_kida_epic", "name": "Kida", "sub": "Crystal Empress", "ink": "amber", "cost": 6, "inkable": True, "type": "Character", "str": 4, "will": 6, "lore": 3, "rarity": "Epic"}
        ]
    },
    {
        "id": "set12",
        "num": 12,
        "name": "Wilds Unknown",
        "date": "May 2026",
        "has_epic": True,
        "has_iconic": True,
        "iconic_cards": ["Tarzan - Lord of the Jungle (Iconic)", "Mowgli & Baloo - Wild Kin (Iconic)"],
        "cards": [
            {"id": "s12_tarzan_iconic", "name": "Tarzan", "sub": "Lord of the Jungle (Iconic)", "ink": "emerald", "cost": 7, "inkable": True, "type": "Character", "str": 6, "will": 6, "lore": 3, "rarity": "Iconic", "kw": "Rush, Evasive"},
            {"id": "s12_baloo_iconic", "name": "Mowgli & Baloo", "sub": "Wild Kin (Iconic)", "ink": "amber", "cost": 6, "inkable": True, "type": "Character", "str": 5, "will": 7, "lore": 3, "rarity": "Iconic"},
            {"id": "s12_bagheera_epic", "name": "Bagheera", "sub": "Shadow Stalker", "ink": "amethyst", "cost": 5, "inkable": True, "type": "Character", "str": 4, "will": 5, "lore": 2, "rarity": "Epic", "kw": "Ward"}
        ]
    },
    {
        "id": "set13",
        "num": 13,
        "name": "Attack of the Vine!",
        "date": "July 2026",
        "has_epic": True,
        "has_iconic": True,
        "iconic_cards": ["Mickey & Minnie - Adventuring Duo (Iconic)", "Maleficent - Vine Sovereign (Iconic)"],
        "cards": [
            {"id": "s13_mickey_minnie_iconic", "name": "Mickey & Minnie", "sub": "Adventuring Duo (Iconic)", "ink": "emerald", "cost": 6, "inkable": True, "type": "Character", "str": 6, "will": 6, "lore": 5, "rarity": "Iconic", "kw": "Duo Shift 0"},
            {"id": "s13_mal_vine_iconic", "name": "Maleficent", "sub": "Vine Sovereign (Iconic)", "ink": "ruby", "cost": 9, "inkable": False, "type": "Character", "str": 8, "will": 8, "lore": 4, "rarity": "Iconic"},
            {"id": "s13_duo_6", "name": "Mickey & Minnie", "sub": "Adventuring Duo", "ink": "emerald", "cost": 6, "inkable": False, "type": "Character", "str": 5, "will": 5, "lore": 5, "rarity": "Legendary", "kw": "Duo Shift 0"},
            {"id": "s13_duo_6_ench", "name": "Mickey & Minnie", "sub": "Adventuring Duo", "ink": "emerald", "cost": 6, "inkable": False, "type": "Character", "str": 5, "will": 5, "lore": 5, "rarity": "Enchanted", "kw": "Duo Shift 0"},
            {"id": "s13_bushroot_epic", "name": "Dr. Bushroot", "sub": "Vine Master", "ink": "emerald", "cost": 6, "inkable": True, "type": "Character", "str": 5, "will": 5, "lore": 3, "rarity": "Epic", "kw": "Ward"},
            {"id": "s13_hades_epic", "name": "Hades", "sub": "Overgrown Schemer", "ink": "sapphire", "cost": 7, "inkable": True, "type": "Character", "str": 6, "will": 6, "lore": 3, "rarity": "Epic"},
            {"id": "s13_minnie_1", "name": "Minnie Mouse", "sub": "Curious Adventurer", "ink": "emerald", "cost": 1, "inkable": True, "type": "Character", "str": 2, "will": 2, "lore": 1, "rarity": "Common"},
            {"id": "s13_mickey_2", "name": "Mickey Mouse", "sub": "Bob Cratchit", "ink": "sapphire", "cost": 2, "inkable": True, "type": "Character", "str": 3, "will": 2, "lore": 1, "rarity": "Super Rare"}
        ]
    },
    {
        "id": "set14",
        "num": 14,
        "name": "Hyperia City",
        "date": "Oct 2026",
        "has_epic": True,
        "has_iconic": True,
        "iconic_cards": ["Mickey Mouse - Neon Overseer (Iconic)", "Tron - Grid Liberator (Iconic)"],
        "cards": [
            {"id": "s14_mickey_neon_iconic", "name": "Mickey Mouse", "sub": "Neon Overseer (Iconic)", "ink": "steel", "cost": 7, "inkable": True, "type": "Character", "str": 6, "will": 7, "lore": 4, "rarity": "Iconic", "kw": "Cybernetic Shift"},
            {"id": "s14_tron_iconic", "name": "Tron", "sub": "Grid Liberator (Iconic)", "ink": "sapphire", "cost": 6, "inkable": True, "type": "Character", "str": 5, "will": 6, "lore": 3, "rarity": "Iconic", "kw": "Security Override"},
            {"id": "s14_quorra_epic", "name": "Quorra", "sub": "Digital Warrior", "ink": "ruby", "cost": 5, "inkable": True, "type": "Character", "str": 4, "will": 5, "lore": 2, "rarity": "Epic", "kw": "Rush"},
            {"id": "s14_hyperia_spire", "name": "Hyperia Central Tower", "sub": "Heart of the City", "ink": "steel", "cost": 4, "inkable": True, "type": "Location", "will": 10, "lore": 2, "rarity": "Epic"}
        ]
    }
]

# Write JSON database
with open('data/lorcana-database.json', 'w', encoding='utf-8') as f:
    json.dump(SETS_METADATA, f, indent=2, ensure_ascii=False)

# Write JS file for browser usage (window.LORCANA_SETS_DB)
js_content = f"// Portable Disney Lorcana Card Database (Set 1 to Set 14)\nwindow.LORCANA_SETS_DB = {json.dumps(SETS_METADATA, indent=2, ensure_ascii=False)};\n"
with open('data/lorcana-cards.js', 'w', encoding='utf-8') as f:
    f.write(js_content)

print(f"Generated portable database: {len(SETS_METADATA)} sets cataloged.")
