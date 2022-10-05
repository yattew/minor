from flask import Flask
from utils import *

app = Flask(__name__)

if __name__ == "__main__":
    config = get_config()
    debug = False
    if config["env"] == "dev":
        debug = True
    app.run(debug=debug)
