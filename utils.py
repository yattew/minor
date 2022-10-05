def get_config():
    import json
    config = None
    with open("config.json", "r") as config_fd:
        config = json.load(config_fd)
    return config