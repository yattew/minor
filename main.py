from tree import *


def query_obj(nodes, name: str):
    return nodes[name]


def search_term(tree, nodes, term):
    tree_pt = query_obj(nodes, term)
    # read from actual document
    doc = tree_pt.doc
    parents = tree_pt.parents
    children = tree_pt.children
    return {
        "doc": doc,
        "parents": parents,
        "children": children,
        "tree_pt": tree_pt
    }


if __name__ == "__main__":
    from utils import *
    config = get_config()
    tree, nodes = load_tree(config["tree_serialized"])
    term = "functions"
    print(search_term(tree, nodes, term))
