import pickle


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
    with open(file, "r") as f:
        jsn_asDict = json.load(f)
        tree = Tree("class")
        tree.doc = jsn_asDict["class"][0]
        nodes["class"] = tree
        do_dfs(jsn_asDict["class"][1], tree, tree, nodes)
        return tree, nodes


def save_tree(tree, nodes, file):
    with open(file, "wb") as f:
        pickle.dump(tree, f, protocol=pickle.HIGHEST_PROTOCOL)
        pickle.dump(nodes, f, protocol=pickle.HIGHEST_PROTOCOL)

def load_tree(file):
    with open(file, "rb") as f:
        a = pickle.load(f)
        b = pickle.load(f)
        return (a,b)



if __name__ == "__main__":
    from utils import *
    config = get_config()
    
    tree, nodes = build_tree(config["tree"])
    save_tree(tree,nodes,config["tree_serialized"])
    # tree,nodes = load_tree("tree.dat")
    # from pprint import pprint
    # pprint(tree)
    # pprint(nodes)
