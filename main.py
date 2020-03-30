from algoritmo import AlgoritmoBarrido
from Punto import Punto
from Segmento import Segmento
from Reader import getSegments
from helpers import resetMemDir, addIntersectionsToModel, vertexY, getAngle, orderNextPrev
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
    resetMemDir(VERTEX, EDGES) # Funcion para cambiar los nombres str de los segmentos y puntos, por sus objetos
    addIntersectionsToModel(barr.R, EDGES, VERTEX) # Funcion para añadir las intersecciones al modelo
    resetMemDir(VERTEX, EDGES) # Funcion para cambiar los nombres str de los segmentos y puntos, por sus objetos
    
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
        alpha = getAngle(V0, v1)
        Angles.append((alpha, v1))
    
    Angles.sort(key=lambda z: z[0], reverse=True)
    orderNextPrev(Angles, VERTEX, EDGES)


        



if __name__ == "__main__":
    main()