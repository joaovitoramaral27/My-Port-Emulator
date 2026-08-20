import json
from pathlib import Path

SETTINGS_FILE = Path("APP/Settings/rom_folders.json")


def load_folders():
    if not SETTINGS_FILE.exists():
        return {}

    try:
        with open(SETTINGS_FILE, "r", encoding="utf-8") as file:
            content = file.read().strip()

            if not content:
                return {}

            return json.loads(content)

    except json.JSONDecodeError:
        return {}


def save_folder(system_name, folder_path):
    folders = load_folders()

    folders[system_name] = folder_path

    SETTINGS_FILE.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    with open(SETTINGS_FILE, "w", encoding="utf-8") as file:
        json.dump(
            folders,
            file,
            indent=4,
            ensure_ascii=False
        )


def get_folder(system_name):
    folders = load_folders()

    return folders.get(system_name)