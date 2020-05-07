class Graph:
    
    def __init__(self):
        self.nodes = []

    def set_node(self,node):
        if node.previous == None:
            self.nodes.append(node)

    def get_node(self,cycle):
        for node in self:
            for c in node:
                if cycle == c:
                    return node

    def __repr__(self):
        return repr(self.nodes)   

    def __iter__(self):
        return iter(self.nodes)       