from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[2]
ASSETS_DIR = PROJECT_ROOT / "assets"
SPRITES_DIR = ASSETS_DIR / "sprites"
AUDIO_DIR = ASSETS_DIR / "audio"
MAPS_DIR = ASSETS_DIR / "maps"
CUSTOM_MAP_PATH = MAPS_DIR / "custom.txt"


def sprite_path(name):
    return str(SPRITES_DIR / name)


def audio_path(name):
    return str(AUDIO_DIR / name)
