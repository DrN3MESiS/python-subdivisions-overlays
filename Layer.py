from Edge import Edge
from Face import Face
from Punto import Punto
from Segmento import Segmento
from Punto import Punto
from Cycles import Cycles
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
          self.Elements[line[0]] = Punto(0,0,line)
          self.V[line[0]] = Punto(0,0,line)
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

    barr = AlgoritmoBarrido(segmentos)
    barr.barrer()

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
      vertex = Punto(0,0,["pi"+str(index),str(coord.x),str(coord.y),list(barr.R[index+1])[0].Edge.name])
      f.write(str(vertex))
    f.close()

    f = open(file+".ari","w")
    f.write("Archivo de aristas\n#############################################\nNombre  Origen  Pareja  Cara    Sigue   Antes\n#############################################\n")
    f.close()
    f = open(file+".ari","a")
    for key in self.E:
      edge = self.E[key]
      couple = self.Elements[edge.couple]
      f.write(str(edge))
      f.write(str(couple))
    for key in other.E:
      edge = other.E[key]
      couple = other.Elements[edge.couple]
      f.write(str(edge))
      f.write(str(couple))

    f.close()   
    
    layer = Layer(file) 

    for index in range(0,len(barr.R),2):
      S = barr.R[index+1]
      CW = []
      CWD = dict()
      for segmento in S:
        v = layer.V["pi"+str(index)]
        edge = layer.Elements[segmento.Edge.name]
        couple = layer.Elements[segmento.Edge.couple]
        edge.setCouple(edge.couple+"'")
        couple.setCouple(couple.couple+"'")
        edge.setPrevious(edge.couple)
        couple.setPrevious(couple.couple) 
        newEdge = Edge([edge.name+"'","pi"+str(index),couple.name,edge.face,edge.next,edge.name])
        newCouple = Edge([couple.name+"'","pi"+str(index),edge.name,couple.face,couple.next,couple.name])
        layer.Elements[edge.name+"'"] = newEdge
        layer.Elements[couple.name+"'"] = newCouple
        edgeCW = Punto.cw(v,layer.Elements[edge.origin])
        coupleCW = Punto.cw(v,layer.Elements[couple.origin])
        CWD[edgeCW] = edge 
        CWD[coupleCW] = couple         
        CW.append(edgeCW)
        CW.append(coupleCW)    
      CW.sort() 
      for index in range(len(CW)):
        edge = layer.Elements[CWD[CW[index]].name]
        couple = layer.Elements[edge.couple]
        previous = layer.Elements[CWD[CW[index-1]].name]
        aux = index + 1
        if(aux >= len(CW)):
          aux = 0
        next = layer.Elements[layer.Elements[CWD[CW[aux]].name].couple]
        couple.setPrevious(previous.name)
        edge.setNext(next.name)
        self.replace_line(file,str(edge))
        self.replace_line(file,str(couple))


    layer_union = Layer(file)
    cycles = Cycles(layer_union)
    graph = cycles.get_graph()

    file = "union_layer"
    f = open(file+".car","w")
    f.write("Archivo de caras\n#######################\nNombre  Interno Externo\n#######################\n")
    f.close()
    f = open(file+".car","a")
    count = 1  
    for node in graph.nodes:
      internal = node.cycle.Edges[0]
      external = node.get_last().cycle.Edges[0]
      line = ["f"+str(count),str(None),internal]
      if internal != external:
        line[1] = external
      face = Face(line)  
      f.write(str(face))
    f.close() 
    return layer_union  

  def replace_line(self,file,newLine):
    newSplittedLine = newLine.split()
    newFileContent = ""
    found = False

    f = open(file+".ari","r")
    for line in f:
      splittedLine = line.split()
      if newSplittedLine[0] == splittedLine[0]:
        print(line + "->" + newLine)
        found = True
        newFileContent += newLine
      else:
        newFileContent += line  
    f.close()

    f = open(file+".ari","w")
    f.write(newFileContent)
    f.close()

    if not found: 
      f = open(file+".ari","a")
      f.write(newLine)
      f.close() 