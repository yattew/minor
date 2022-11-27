print(1)
from flask import Flask
from flask_cors import CORS, cross_origin
from tree import *
from utils import *
import sys


app = Flask(__name__)
config = get_config()
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
tree, nodes = load_tree(config["tree_serialized"])


@app.route("/query/<query>")
@cross_origin()
def query(query):
    print(nodes)
    result = tuple(set(list(search_term(tree, nodes, query))))
    return {"res":result}

@app.route("/result/<query>")
@cross_origin()
def result(query):
    return {
        "url":"https://www.geeksforgeeks.org/maximum-sum-path-across-two-arrays/",
        "related":[],
        "more":[]
    }

@app.route("/doc/<item>")
@cross_origin()
def doc(item):
    doc_p = nodes[item].doc
    doc = "halo frandz"
    # with open(doc_p,"r") as f:
    #     doc= f.read()
    return {"doc":doc}



if __name__ == "__main__":
    debug = False
    if config["env"] == "dev":
        debug = True
    app.run(debug=debug, host=config["host"], port=config["port"])
