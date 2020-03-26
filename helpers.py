from Edge import Edge
from Punto import Punto
from Vertex import Vertex
import itertools
import copy

def pairwise(iterable):
        "s -> (s0,s1), (s1,s2), (s2, s3), ..."
        a, b = itertools.tee(iterable)
        next(b, None)
        return zip(a, b)  

def getAngle(P0, P1):
    pass

def resetMemDir(VERTEX, EDGES):
    for edge in EDGES:
        for v in VERTEX:
            if type(edge.gS()) == str:
                if edge.gS() == v.gN():
                    edge.setStart(v)
                    break

        for e in EDGES:
            if type(edge.gP()) == str:
                if edge.pair == e.gN():
                    edge.pair = e
            
            if type(edge.gNe()) == str:
                if edge.next == e.gN():
                    edge.next = e

            if type(edge.gPe()) == str:
                if edge.previous == e.gN():
                    edge.previous = e

def reconstructSegments(data, EDGES):
    newEDGES = []
    i = 0
    
    for d in data: # Por cada elemento en el barr.R (Objeto de intersecciones)
        curIntersectPoint = data[i-1] #Tomar el punto de interseccion y guardarlo
        if i % 2 != 0: # Cada dos posiciones (cuando d sea los segmentos que intersectan en el p de interseccion) tomar el diccionario de segmentos
            for segment in d:  # Por cada segmento de la interseccion
                s_start = segment.puntos[0]
                s_end = segment.puntos[1]
                for edge in EDGES: # Buscar el edge que es igual a ese segmento
                    e_start = edge.start
                    e_end = edge.pair.start
                    if s_start == e_start and s_end == e_end: #Cuando encuentra un match, crear los nuevos segmentos
                        name1 = edge.gN() + "'"
                        name2 = edge.gN() + "''"
                        name3 = edge.gN() + "'''"
                        name4 = edge.gN() + "'''"
                        newEDGES.append(Edge(name1, curIntersectPoint, name2))
                        newEDGES.append(Edge(name2, e_start, name1))
                        newEDGES.append(Edge(name3, e_end, name4))
                        newEDGES.append(Edge(name4, curIntersectPoint, name3))
                        EDGES.remove(edge.pair) #Remover la pareja del edge que hace match al segmento
                        EDGES.remove(edge) #Remover el edge que hace match al asegmento
        i += 1
    EDGES.extend(newEDGES)

    return newEDGES

def constructFromIALG(data, EDGES):
    vs = []
    i = 0
    for d in pairwise(data):
        if i % 2 == 0:
            inter_coord = d[0]
            segments = d[1]
            start_edge = segments.pop()
            v = Vertex("v1", inter_coord.x, inter_coord.y, start_edge)
            vs.append(v)
        i+=1
    return vs

def addIntersectionsToModel(data, EDGES, VERTEX):
    tempData = copy.deepcopy(data)
    vs = constructFromIALG(tempData, EDGES) # Crear los Vertex: Intersecciones con sus respectivos datos
    tempData = copy.deepcopy(data)
    i = 1
    for item in tempData:
        if type(item) == Punto:
            tempData[i-1] = f"v{i}"
    VERTEX.extend(vs) # Agregar V: interseccion al array de puntos
    EDGES = reconstructSegments(tempData, EDGES) # Reconstruir el modelo con los nuevos puntos
    


