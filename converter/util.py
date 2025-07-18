import json
from pathlib import Path
import logging
import requests


try:
    import foundry as foundry
except ImportError:
    import converter.foundry as foundry

PROJECT = Path(__file__).parent.parent
CONVERTER = PROJECT / "converter"

BUILD = PROJECT / "build"
BUILD_POKEMON = BUILD / "pokemon"
BUILD_MOVES = BUILD / "moves"
BUILD_ABILITIES = BUILD / "abilities"

DIST = PROJECT / "dist"
DIST_MODULE = DIST / foundry.module_name
DIST_PACKS = DIST_MODULE / "packs"

DATA = PROJECT / "p5e-data" / "data"
CACHE = PROJECT / "cache"

ASSETS = PROJECT / "assets"


def download():
    CACHE.mkdir(exist_ok=True)
    files = ['leveling.json', 'pokedex_extra.json', 'abilities.json']
    for f in files:
        cache_file = CACHE / f
        if cache_file.exists():
            continue  # Skip download if file already exists
        try:
            r = requests.get(f'https://raw.githubusercontent.com/Jerakin/Pokedex5E/master/assets/datafiles/{f}', allow_redirects=True)
            if r.status_code == 200:
                with open(cache_file, 'w', encoding="utf-8") as fp:
                    fp.write(json.dumps(r.json(), ensure_ascii=False))
        except Exception as e:
            print(f"Warning: Could not download {f}: {e}")
            # Create empty file if download fails
            if not cache_file.exists():
                with open(cache_file, 'w', encoding="utf-8") as fp:
                    json.dump({}, fp)


def __load(path):
    with path.open(encoding="utf-8") as fp:
        json_data = json.load(fp)
    return json_data


def load_datafile(name):
    p = (DATA / name).with_suffix(".json")
    if p.exists():
        return __load(p)
    else:
        logging.error(f"Could not load data file {p}")


def load_cached_file(name):
    p = (CACHE / name).with_suffix(".json")
    if p.exists():
        return __load(p)
    else:
        logging.error(f"Could not load data file {p}")


def load_extra(name):
    p = Path(ASSETS / "data" / name).with_suffix(".json")
    return __load(p)


def load_template(name):
    p = Path(ASSETS / "templates" / name).with_suffix(".json")
    return __load(p)


download()
LEVEL_DATA = load_cached_file("leveling")
POKEDEX_DATA = load_cached_file("pokedex_extra")
ABILITY_DATA = load_cached_file("abilities")

EXTRA_MOVE_DATA = load_extra("moves_extra")
EXTRA_POKEMON_DATA = load_extra("pokemon_extra")
MERGE_MOVE_DATA = load_extra("moves")
MERGE_POKEMON_DATA = load_extra("pokemon")
EXTRA_MOVE_ICON_DATA = load_extra("move_icons")
EXTRA_POKEMON_IMAGE_DATA = load_extra("pokemon_images")
MERGE_ABILITY_DATA = load_extra("abilities")

TRANSLATE_NAME = {
  "Flabebe": "Flabébé",
  "Meowstic-f": "Meowstic ♀",
  "Meowstic-m": "Meowstic ♂",
  "Nidoran-m": "Nidoran ♂",
  "Nidoran-f": "Nidoran ♀",
  "Type Null": "Type: Null"
}


def merge(a, b, path=None):
    """merges b into a"""
    if path is None: path = []
    for key in b:
        if key in a:
            if isinstance(a[key], dict) and isinstance(b[key], dict):
                merge(a[key], b[key], path + [str(key)])
            elif a[key] == b[key]:
                pass  # same value
            else:  # Overwrite value
                a[key] = b[key]
                # raise Exception('Conflict at %s' % '.'.join(path + [str(key)]))
        else:
            a[key] = b[key]
    return a
