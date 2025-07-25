from pathlib import Path

skill_name_to_abv = {
    "Acrobatics": "acr",
    "Animal Handling": "ani",
    "Arcana": "arc",
    "Athletics": "ath",
    "Deception": "dec",
    "History": "his",
    "Insight": "ins",
    "Intimidation": "itm",
    "Investigation": "inv",
    "Medicine": "med",
    "Nature": "nat",
    "Persuasion": "prc",
    "Performance": "prf",
    "Perception": "per",
    "Religion": "rel",
    "Sleight of Hand": "slt",
    "Stealth": "ste",
    "Survival": "sur"
}

token_size_map = {
    "tiny": {"width": 1, "height": 1, "scale": 0.5},
    "sm": {"width": 1, "height": 1, "scale": 0.8},
    "med": {"width": 1, "height": 1, "scale": 1},
    "lg": {"width": 2, "height": 2, "scale": 1},
    "huge": {"width": 3, "height": 3, "scale": 1},
    "grg": {"width": 4, "height": 4, "scale": 1},
}

abv_size = {
    "Tiny": "tiny",
    "Small": "sm",
    "Medium": "med",
    "Large": "lg",
    "Huge": "huge",
    "Gargantuan": "grg",
    "Varies": "med"
}


skill_abv_to_name = {
     "acr": "Acrobatics",
     "ani": "Animal Handling",
     "arc": "Arcana",
     "ath": "Athletics",
     "dec": "Deception",
     "his": "History",
     "ins": "Insight",
     "itm": "Intimidation",
     "inv": "Investigation",
     "med": "Medicine",
     "nat": "Nature",
     "prc": "Persuasion",
     "prf": "Performance",
     "per": "Perception",
     "rel": "Religion",
     "slt": "Sleight of Hand",
     "ste": "Stealth",
     "sur": "Survival",
}

abilities = ["str", "dex", "con", "int", "wis", "cha"]


sr_map = {
    0.125: "1/8",
    0.25: "1/4",
    0.5: "1/2",
}

module_id = "pokemon5e"
module_name = "Pokemon5e"
module_version = (Path(__file__).parent.parent / "VERSION").read_text()
module_definition = {
    "id": module_id,
    "title": module_name,
    "description": "The Wonderful World of Pokémon - in Dungeons & Dragons 5E",
    "authors": [
        {
            "name": "Jerakin"
        }
    ],
    "version": module_version,
    "compatibleCoreVersion": "12",
    "compatibility": {
        "minimum": "10",
        "verified": "12"
    },
    "url": "https://github.com/Albydo/p5e-foundryVTT",
    "manifest": "https://raw.githubusercontent.com/Albydo/p5e-foundryVTT/master/module.json",
    "download": f"https://github.com/Albydo/p5e-foundryVTT/releases/download/v{module_version}/pokemon5e.zip",
    "packs": [
    ]
}


packs = {
    "pokemon": {
        "name": "pokemon",
        "label": "Pokemon",
        "path": "packs/p5e-pokemon.db",
        "type": "Actor",
        "module": module_id
    },
    "moves": {
        "name": "moves",
        "label": "Pokemon Moves",
        "path": "packs/p5e-moves.db",
        "type": "Item",
        "module": module_id
    },
    "abilities": {
        "name": "abilities",
        "label": "Pokemon Abilities",
        "path": "packs/p5e-abilities.db",
        "type": "Item",
        "module": module_id
    }
}
