from flask import Flask
from tree import *
from utils import *


app = Flask(__name__)
config = get_config()
tree, nodes = load_tree(config["tree_serialized"])


@app.route("/query/<query>")
def query(query):
    result = search_term(tree, nodes, query)
    return result["tree_pt"].name


if __name__ == "__main__":
    debug = False
    if config["env"] == "dev":
        debug = True
    app.run(debug=debug, host=config["host"], port=config["port"])
