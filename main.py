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


def load_tree(file):
    with open(file, "rb") as f:
        a = pickle.load(f)
        b = pickle.load(f)
        return (a, b)


def query_obj(nodes, name: str):
    return nodes[name]


def search_term(tree, nodes, term):
    tree_pt = query_obj(nodes, term)
    #read from actual document
    doc = tree_pt.doc
    parents = tree_pt.parents
    children = tree_pt.children
    return {
        "doc":doc,
        "parents":parents,
        "children":children,
        "tree_pt":tree_pt
    }


def main():
    tree, nodes = load_tree("tree.dat")
    term = "functions"
    print(search_term(tree, nodes, term))



if __name__ == "__main__":
    main()
