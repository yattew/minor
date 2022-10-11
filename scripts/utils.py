from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent
def get_config():
    import json
    config = None
    with open(BASE_DIR/"config.json", "r") as config_fd:
        config = json.load(config_fd)
    return config