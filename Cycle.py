from Punto import Punto
from Punto import Punto
from Edge import Edge

class Cycle:

    def __init__(self, origin, elements):
        self.Edges = [origin]
        next = elements[origin].next
        self.lefter = [elements[origin],elements[elements[origin].origin]]
        while next != origin:
            vertex = elements[elements[next].origin]
            if(vertex.x < self.lefter[1].x):
                self.lefter = [elements[next],vertex]
            self.Edges.append(next)
            next = elements[next].next 
        index = self.Edges.index(self.lefter[0].name)
        v = elements[elements[self.Edges[index]].origin]
        a = Punto.vector(v,elements[elements[self.Edges[index+1]].origin])
        b = Punto.vector(elements[elements[self.Edges[index-1]].origin],v)
        if(Edge.cross(a,b) >= 0):
            self.clockwise = True
        else:
            self.clockwise = False

    def setNext(self,next):        
        self.next = next

    def setPrevious(self,previous):
        self.previous = previous 

    def removeEdges(self, edges):
        for edge in self.Edges:
            if edge in edges:
                del edges[edge]

    # def get_segmento(self, elements):
    #     origin = self.lefter[1]
    #     end = elements[elements[self.lefter[0].next].origin]
    #     return Punto.vector(origin, end)



    def __repr__(self):
        return repr(self.Edges)                    