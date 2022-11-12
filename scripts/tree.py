import pickle
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent

class Tree:
    def __init__(self, name=None):
        self.name = name
        self.children = {}
        self.parents = {}
        self.doc = ""

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()


def do_dfs(children: dict, tree: Tree, parent: Tree, nodes) -> Tree:

    if children == None:
        return None
    else:
        for i in children:
            if i not in nodes:
                tree.children[i] = Tree(i)
                nodes[i] = tree.children[i]
                tree.children[i].doc = children[i][0]
                
                do_dfs(children[i][1], tree.children[i], tree.children[i], nodes)
            child = nodes[i]
            child.parents[parent.name] = parent


def build_tree(file):
    tree = None
    nodes = {}
    import json
    with open(BASE_DIR/file, "r") as f:
        jsn_asDict = json.load(f)
        tree = Tree("class")
        tree.doc = jsn_asDict["class"][0]
        nodes["class"] = tree
        do_dfs(jsn_asDict["class"][1], tree, tree, nodes)
        return tree, nodes


def save_tree(tree, nodes, file):
    with open(BASE_DIR/file, "wb") as f:
        pickle.dump(tree, f, protocol=pickle.HIGHEST_PROTOCOL)
        pickle.dump(nodes, f, protocol=pickle.HIGHEST_PROTOCOL)

def load_tree(file):
    with open(BASE_DIR/file, "rb") as f:
        a = pickle.load(f)
        b = pickle.load(f)
        return (a,b)



def query_obj(nodes, name: str):
    return nodes.get(name,None)


def search_term(tree, nodes, term):
    words = term.split()
    tree_pts = []
    for i in words:
        if i in nodes:
            tree_pts.append(i);
    return tuple(tree_pts)
    tree_pt = query_obj(nodes, term)
    # read from actual document
    doc = tree_pt.doc
    return {
        "doc": doc,
        "parents": list(parents(tree,nodes,term).keys()),
        "children": list(children(tree,nodes,term).keys()),
        "related": list(siblings(tree,nodes,term).keys()),
    }

def children(root,nodes,searchTerm):
    print(nodes[searchTerm])
    return nodes[searchTerm].children

def parents(root,nodes,searchTerm):
    return nodes[searchTerm].parents

def siblings(root,nodes,searchTerm):
    t= (nodes[searchTerm].parents).values()
    t2={}
    for i in t:
        t2.update(i.children)
    del t2[searchTerm]
    return t2
    
if __name__ == "__main__":
    from utils import get_config
    config = get_config()
    
    tree, nodes = build_tree(config["tree"])
    save_tree(tree,nodes,config["tree_serialized"])
    # config = get_config()
    # tree, nodes = load_tree(config["tree_serialized"])
    # term = "functions"
    # print(search_term(tree, nodes, term))
    # tree,nodes = load_tree("tree.dat")
    # from pprint import pprint
    # pprint(tree)
    # pprint(nodes)
