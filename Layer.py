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
    self.file = file
    self.graph = None
    
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
    i = 0
    R = []
    for index in range(0,len(barr.R),2):
      coord = barr.R[index]
      isVertex = self.is_vertex(other,coord)
      if not isVertex:
        vertex = Punto(0,0,["pi"+str(i),str(coord.x),str(coord.y),list(barr.R[index+1])[0].Edge.name])
        f.write(str(vertex))
        i += 1
        R.append(barr.R[index+1])
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

    replace = []
    for index in range(0,len(R)):
      S = R[index]
      CW = []
      CWD = dict()
      for segmento in S:
        v = layer.V["pi"+str(index)]
        edge = layer.Elements[segmento.Edge.name]
        couple = layer.Elements[segmento.Edge.couple]
        edge.setCouple(edge.couple+"\'")
        couple.setCouple(couple.couple+"\'")
        newEdge = Edge([edge.name+"\'","pi"+str(index),couple.name,edge.face,edge.next,edge.name])
        newCouple = Edge([couple.name+"\'","pi"+str(index),edge.name,couple.face,couple.next,couple.name])
        layer.Elements[edge.name+"\'"] = newEdge
        layer.Elements[couple.name+"\'"] = newCouple
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
        replace.append([couple.next,couple.name])
    
    for r in replace:
      self.replace_element(file,r[0],r[1],5)

    layer_union = Layer(file)
    cycles = Cycles(layer_union)
    graph = cycles.get_graph()

    f = open(self.file+".ari","r")
    for line in f:
      splittedLine = line.split()
      if splittedLine[0][0] == 's':
        face = self.F[splittedLine[3]]
        edge = splittedLine[0]
        
        cycle = cycles.get_cycle(edge)
        if cycle:
          face.set_cycle(cycle)

    f.close()

    f = open(other.file+".ari","r")
    for line in f:
      splittedLine = line.split()
      if splittedLine[0][0] == 's':
        face = other.F[splittedLine[3]]
        edge = splittedLine[0]
        
        cycle = cycles.get_cycle(edge)
        if cycle:
          face.set_cycle(cycle)

    f.close()

    f = open(file+".car","w")
    f.write("Archivo de caras\n#######################\nNombre  Interno Externo\n#######################\n")
    f.close()
    f = open(file+".car","a")
    count = 1  
    for node in graph.nodes:
      internal = node.cycle.Edges[0]
      external = node.get_last().cycle.Edges[0]
      line = ["f"+str(count),str(None),str(None)]
      if internal != external:
        line[1] = external
        line[2] = internal
        for cycle in node:
          for edge in cycle.Edges:
            self.replace_element(file,edge,"f"+str(count),3)          
      else:
        if node.cycle.clockwise:
          line[2] = internal
          cycle = node.cycle
          for edge in cycle.Edges:
            self.replace_element(file,edge,"f"+str(count),3)
        else:
          line[1] = external
          for edge in node.get_last().cycle.Edges:
            self.replace_element(file,edge,"f"+str(count),3)    
      count += 1
      face = Face(line)  
      f.write(str(face))
    f.close() 

    layer_union = Layer(file)
    layer_union.graph = graph
    return layer_union  

  def is_vertex(self,other,coord):
    for key in self.V:
      vertex = self.V[key]
      if vertex.x == coord.x and vertex.y == coord.y:
        return True
    for key in other.V:
      vertex = other.V[key]
      if vertex.x == coord.x and vertex.y == coord.y:
        return True
    return False  

  def replace_line(self,file,newLine):
    newSplittedLine = newLine.split()
    newFileContent = ""
    found = False

    f = open(file+".ari","r")
    for line in f:
      splittedLine = line.split()
      if newSplittedLine[0] == splittedLine[0]:
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

  def replace_element(self,file,edge,element,index):
    newFileContent = ""

    f = open(file+".ari","r")
    for line in f:
      splittedLine = line.split()
      if edge == splittedLine[0]:
        splittedLine[index] = element
        e = Edge(splittedLine)
        newFileContent += str(e)
      else:
        newFileContent += line  
    f.close()

    f = open(file+".ari","w")
    f.write(newFileContent)
    f.close()