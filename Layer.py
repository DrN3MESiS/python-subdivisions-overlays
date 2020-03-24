from Edge import Edge
from Face import Face
from Vertex import Vertex
from Segmento import Segmento
from Punto import Punto
from algoritmo import AlgoritmoBarrido
from copy import deepcopy

class Layer:

  def __init__(self, file):
    self.Elements = dict()
    self.V = dict()
    self.E = dict()
    self.F = dict()

    self.assign_values(file)

  def assign_values(self,file):
    f = open(file+".ver","r")
    for vertex in f.readlines():
        line = vertex.split()
        if(line[0][0] == 'p'):
          self.Elements[line[0]] = Vertex(line)
          self.V[line[0]] = Vertex(line)
    f.close()

    f = open(file+".car","r")
    for face in f.readlines():
        line = face.split()
        if(line[0][0] == 'f'):
          self.Elements[line[0]] = Face(line)
          self.F[line[0]] = Face(line)
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
      segmentos.append(Segmento(edge,Punto(int(origin.x),int(origin.y)),Punto(int(end.x),int(end.y))))

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

    file = "union_layer"

    f = open(file+".ver","w")
    f.write("Archivo de vértices\n#################################\nNombre  x       y       Incidente\n#################################\n")
    f.close()
    f = open(file+".ver","a")
    for key in self.V:
      vertex = self.V[key]
      f.write(str(vertex))
    for key in other.V:
      vertex = other.V[key]
      f.write(str(vertex))
    for index in range(0,len(barr.R),2):
      coord = barr.R[index]
      vertex = Vertex(["pi"+str(index),str(coord.x),str(coord.y),list(barr.R[index+1])[0].Edge.name])
      f.write(str(vertex))
    f.close()

    f = open(file+".car","w")
    f.write("Archivo de caras\n#######################\nNombre  Interno Externo\n#######################\n")
    f.close()
    f = open(file+".car","a")
    for key in self.F:
      face = self.F[key]
      f.write(str(face))
    for key in other.F:
      face = other.F[key]
      f.write(str(face))
    f.close()

    Edges = deepcopy(self.Elements)
    Edges.update(other.Elements)

    f = open(file+".ari","w")
    f.write("Archivo de vértices\n#################################\nNombre  x       y       Incidente\n#################################\n")
    f.close()
    f = open(file+".ari","a")
    for index in range(0,len(barr.R),2):
      S = barr.R[index+1]
      for segmento in S:
        edge = Edges[segmento.Edge.name]
        couple = Edges[segmento.Edge.couple]
        edge.setCouple(edge.couple+"'")
        couple.setCouple(couple.couple+"'")
        edge.setPrevious(edge.couple)
        couple.setPrevious(couple.couple) 
        newEdge = Edge([edge.name+"'","pi"+str(index),couple.name,edge.face,edge.next,edge.name])
        newCouple = Edge([couple.name+"'","pi"+str(index),edge.name,couple.face,couple.next,couple.name])        
        edge.setNext("")
        couple.setNext("")  
        newEdge.setPrevious("")
        newCouple.setPrevious("")   
        f.write(str(edge))
        f.write(str(couple))
        f.write(str(newEdge))
        f.write(str(newCouple))
    
    f.close()