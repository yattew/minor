class Tree:
    def __init__(self, name=None):
        self.name = name
        self.children = {}
        self.parents = {}
        self.doc = ""



def do_dfs(root:dict, tree:Tree) -> Tree:
    children = root[1]
    if not children:
        return None
    
    
    

def build_tree(file):
    tree = None
    import json
    with open(file,"r") as f:
        jsn = json.load(f)
        root = jsn["class"]
        tree = Tree("class")
        do_dfs(root,tree)
        print(jsn)
build_tree("tree.json")
