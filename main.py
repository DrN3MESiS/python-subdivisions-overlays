from algoritmo import AlgoritmoBarrido
from Punto import Punto
from Segmento import Segmento
from Reader import getSegments
from Cycle import Cycle
import math

import helpers
import copy

def main():
    # Linked Lists
    VERTEX = []
    EDGES = []

    # Intersections Lists
    names = ["ejemplo_01/layer01", "ejemplo_01/layer02"]
    segmentos = getSegments(names, VERTEX, EDGES)

    barr = AlgoritmoBarrido(segmentos)
    barr.barrer()

    # Double Linked Intersections
    print("\n\n")
    helpers.resetMemDir(VERTEX, EDGES) # Funcion para cambiar los nombres str de los segmentos y puntos, por sus objetos
    helpers.addIntersectionsToModel(barr.R, EDGES, VERTEX) # Funcion para añadir las intersecciones al modelo
    helpers.resetMemDir(VERTEX, EDGES) # Funcion para cambiar los nombres str de los segmentos y puntos, por sus objetos

    # for e in EDGES:
    #     print("////")
    #     print("\tCUR: ", e.gN())
    #     print("\tPAIR: ", e.gP().gN())
    #     print("////")
    
    # SORT NEXT AND PREV
    OrderedVertex = copy.deepcopy(VERTEX)
    OrderedVertex.sort(key=lambda v: v.y, reverse=True)
    
    V0 = None
    for v in OrderedVertex:
        if str(v.gN()).startswith('v'):
            V0 = v
            OrderedVertex.remove(v)

    Angles = []
    for v1 in OrderedVertex:
        alpha = helpers.getAngle(V0, v1)
        Angles.append((alpha, v1))

    Angles.sort(key=lambda z: z[0], reverse=True)
    helpers.orderNextPrev(Angles, VERTEX, EDGES)

    
    # print()
    # for e in EDGES:
    #     print("CURRENT: ", e.gN())
    #     print("\t-> Pre: ", e.gPe().gN(), "\n\t-> Ne: ", e.gNe().gN(), "\n")

    # For each VERTEX, save the immidiate edge to the left
    for v in VERTEX:
        curY = v.gY()
        curX = v.gX()
        intersections = []

        for e in EDGES:
            segment = helpers.getEdgeSegment(e)
            x1 = segment.puntos[0].x
            x2 = segment.puntos[1].x
            barrLine = Segmento(Punto(x1, curY),Punto(x2, curY))
            data = barrLine.interseccion(segment)
            if data:
                if data.x < curX:
                    intersections.append( (data, e) )

        closestEdge = None
        closestEdgeDistance = math.inf
        for i in intersections:
            r = math.sqrt( math.pow((i[0].x-curX),2)+math.pow((i[0].y-curY),2))
            if r < closestEdgeDistance:
                closestEdge = i[1]
                closestEdgeDistance = r
            
        v.closestEdge = closestEdge
    # Determine Cycles
    for e in EDGES:
        print(e)

    print("\n\n\n")
    cycles = []
    markedEdges = []
    i = 1
    for firstEdge in EDGES:
        if markedEdges.__contains__(curEdge):
            continue
        else:
            curCycle = Cycle('c'+str(i)) #Start new cycle
            curCycle.addEdge(firstEdge) #Add the current Edge as the init cycle
            
            curEdge = firstEdge
            while True:
                nextEdge = curEdge.gNe()
                curCycle.addEdge(nextEdge)
                if helpers.checkIfCycleHasBeenCompleted(curCycle):
                    break
                curEdge = nextEdge

            for newEdge in EDGES:
                if curEdge == newEdge:
                    continue
                if newEdge == curEdge.gNe():
                    curCycle.addEdge(newEdge)
                    if helpers.checkIfCycleHasBeenCompleted(curCycle):
                        break

            cycles.append(curCycle)
            print(curCycle)
            markedEdges.extend(curCycle.edges)
                
        i+=1
                


        


if __name__ == "__main__":
    main()