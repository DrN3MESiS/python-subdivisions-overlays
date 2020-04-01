from Cycle import Cycle

class Cycles:
    def __init__(self,layer):
        self.layer = layer
        self.cycles = []
        while(len(self.layer.E) > 0):
            key = self.layer.E.popitem()
            cycle = Cycle(key[0],self.layer.Elements)
            cycle.removeEdges(self.layer.E)
            self.cycles.append(cycle)

    def get_segmentos(self): 
        for cycle in self.cycles:
            print(cycle.get_segmento(self.layer.Elements))

    def __repr__(self):
        return repr(self.cycles)        