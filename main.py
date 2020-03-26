from algoritmo import AlgoritmoBarrido
from Punto import Punto
from Segmento import Segmento
from Reader import getSegments
from helpers import resetMemDir, addIntersectionsToModel


def main():
    # Linked Lists
    VERTEX = []
    EDGES = []

    # Intersections Lists
    names = ["ejemplo_01/layer01", "ejemplo_01/layer02"]
    segmentos = getSegments(names, VERTEX, EDGES)

    barr = AlgoritmoBarrido(segmentos)
    barr.barrer()
    # print(barr.R)

    # Double Linked Intersections
    print("\n\n")
    resetMemDir(VERTEX, EDGES)
    addIntersectionsToModel(barr.R, EDGES, VERTEX)
    resetMemDir(VERTEX, EDGES)
    print(len(EDGES), EDGES)


if __name__ == "__main__":
    main()



