from algoritmo import AlgoritmoBarrido
from Punto import Punto
from Face import Face
from Segmento import Segmento
from Reader import getSegments
from Cycle import Cycle
import math

import helpers
import copy

def main():
    cInf = Cycle('Cinf', True)
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
            r = math.sqrt( math.pow((i[0].x - curX),2)+math.pow((i[0].y - curY),2))
            if r < closestEdgeDistance:
                closestEdge = i[1]
                closestEdgeDistance = r
            
        v.closestEdge = closestEdge
        if v.closestEdge == None:
            v.sC(cInf)
    # Determine Cycles


    CYCLES = []
    markedEdges = []
    i = 1
    for firstEdge in EDGES:
        if markedEdges.__contains__(firstEdge):
            continue
        else:
            curCycle = Cycle('c'+str(i), False)
            curCycle.addEdge(firstEdge)
            
            curEdge = firstEdge
            while True:
                nextEdge = curEdge.gNe()
                curCycle.addEdge(nextEdge)
                if helpers.checkIfCycleHasBeenCompleted(curCycle):
                    break
                curEdge = nextEdge

            curCycle.aC(curCycle)            
            CYCLES.append(curCycle)
            markedEdges.extend(curCycle.edges)
                
        i+=1
    
    CYCLES.append(cInf)
    
    #For each cycle, save it's left most vertex
    LMVs = []
    for c in CYCLES:
        if c.inf:
            continue

        curX = math.inf
        curY = math.inf
        curLMV = None
        for e in c.edges:
            if e.gS().x == curX:
                eY = e.gS().y
                if eY < curY:
                    curX = e.gS().x
                    curY = e.gS().y
                    curLMV = e.gS()
            if e.gS().x < curX:
                curX = e.gS().x
                curY = e.gS().y
                curLMV = e.gS()
        c.mLv = curLMV
        curLMV.sC(c)
        curLMV.sCLC(cInf)
        LMVs.append(curLMV)
    
    #For each Cycle, determine if is hole or not (Angle from Edges (if angle > 180))
    for c in CYCLES:
        if c.inf:
            continue
        MLV = c.mLv
        eA = helpers.getEdgeByStart(c.edges, MLV.gN())
        eB = helpers.getEdgeByEnd(c.edges, MLV.gN())

        z1 = helpers.getEdgeSegment(eA)
        z2 = helpers.getEdgeSegment(eB)
        s1 = (z1.puntos[1], z1.puntos[0])
        s2 = (z2.puntos[1], z2.puntos[0])
        
        theta1 = math.atan2(s1[0].y-s1[1].y,s1[0].x-s1[1].x)
        theta2 = math.atan2(s2[0].y-s2[1].y,s2[0].x-s2[1].x)
        
        diff = abs(theta1-theta2)
        angle = min(diff,abs(180-diff))
        if angle > 180:
            c.isHole = False
        else:
            c.isHole = True

    #Generate Graf from each cycle
    # Cycle is Node
    # Arista is Cycle that is not Hole
    Graf = []
    for mlv in LMVs:
        curComponent = [mlv.gC(), mlv.gCLC()]
        Graf.append(curComponent)


    # For each connected component in the Graf
    print(Graf)
    FACES =   []
    i = 1


    Graf = [1,2,3,4,5,6,7,8,8]
    for i in range(len(Graf)):
        curFace = []
        F = Face('f'+str(i))
        rem = Graf[i+1:]
        
        i+=1

if __name__ == "__main__":
    main()