from algoritmo import AlgoritmoBarrido
from Punto import Punto
from Segmento import Segmento
from Reader import getSegments


def main():
    # Linked Lists
    VERTEX = []
    EDGES = []

    # Intersections Lists
    names = ["ejemplo_01/layer01", "ejemplo_01/layer02"]
    segmentos = getSegments(names, VERTEX, EDGES)
    resetMemDir(VERTEX, EDGES)

    barr = AlgoritmoBarrido(segmentos)
    barr.barrer()
    print(barr.R)

    # Double Linked Intersections

    print(VERTEX)
    print(EDGES)


if __name__ == "__main__":
    main()


def resetMemDir(VERTEX, EDGES):
    pass
