from Cycle import Cycle
from Graph import Graph
from Node import Node

class Cycles:
    def __init__(self,layer):
        counter = 1
        self.layer = layer
        self.cycles = []
        while(len(self.layer.E) > 0):
            key = self.layer.E.popitem()
            cycle = Cycle(key[0],self.layer.Elements)
            cycle.set_name(counter)
            cycle.removeEdges(self.layer.E)
            self.cycles.append(cycle)
            counter += 1

    def __repr__(self):
        return repr(self.cycles)   

    def get_graph(self):
        graph = Graph()

        for cycle in self.cycles:
            node = Node(cycle)
            if cycle.clockwise:   
                lefter = self.get_lefter(cycle)
                if lefter:
                    node.set_next(Node(lefter))
            graph.set_node(node)
                
        return graph   

    def get_lefter(self,cycle):
        for left in self.cycles:
            if left.lefter[1].x < cycle.lefter[1].x:
                return left 

        return          

    def __iter__(self):
        return iter(self.cycles)

    def get_cycle(self,edge):
        for cycle in self:
            if edge in cycle.Edges:
                return cycle

        return          