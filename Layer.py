from Edge import Edge
from Face import Face
from Vertex import Vertex
from Segmento import Segmento
from Punto import Punto
from algoritmo import AlgoritmoBarrido


class Layer:

  def __init__(self, file):
    self.Elements = dict()
    self.E = dict()

    self.assign_values(file)

  def assign_values(self,file):
    f = open(file+".ver","r")
    for vertex in f.readlines():
        line = vertex.split()
        if(line[0][0] == 'p'):
          self.Elements[line[0]] = Vertex(line)
    f.close()

    f = open(file+".car","r")
    for face in f.readlines():
        line = face.split()
        if(line[0][0] == 'f'):
          self.Elements[line[0]] = Face(line)
    f.close()

    f = open(file+".ari","r")
    for edge in f.readlines():
        line = edge.split()
        if(line[0][0] == 's'):
          self.Elements[line[0]] = Edge(line)          
          edge = Edge(line)
          if(self.E.get(edge.couple) == None):
            self.E[line[0]] = edge
    f.close()

  def __str__(self):
    return str(self.Elements)  
  
  def get_segmentos(self):
    segmentos = []
    for key in self.E:
      edge = self.E[key]
      origin = self.Elements[self.E[key].origin]
      end = self.Elements[self.Elements[edge.next].origin]
      segmentos.append(Segmento(Punto(origin.x,origin.y),Punto(end.x,end.y)))

    return segmentos  

  def layer_union(self,other):
    segmentos = self.get_segmentos()

    segmentos.extend(other.get_segmentos())
    
    # s3 = Segmento(Punto(0,10),Punto(10,0))
    # s4 = Segmento(Punto(0,0),Punto(10,10))

    # segmentos = [s3,s4]

    for s in segmentos:
        print(s)

    barr = AlgoritmoBarrido(segmentos)
    barr.barrer()
    print(barr.R)  