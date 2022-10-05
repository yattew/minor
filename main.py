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


nodes={}
def do_dfs(children:dict, tree:Tree,parent :Tree) -> Tree:
    
    if children==None:
        return None
    else:
        for i in children:
            if i in nodes:
                child=nodes[i]
                child.parents[parent.name]=parent
            else:
                tree.children[i]=Tree(i)
                nodes[i]=tree.children[i]
                tree.children[i].doc=children[i][0]
                do_dfs(children[i][1],tree.children[i],tree.children[i])
        pass
    
    
    

def build_tree(file):
    tree = None
    import json
    with open(file,"r") as f:
        jsn_asDict = json.load(f)
        tree = Tree("class")
        tree.doc=jsn_asDict["class"][0]
        nodes["class"]=tree
        do_dfs(jsn_asDict["class"][1],tree,tree)
        print(jsn_asDict)
build_tree("tree.json")
print(nodes)
