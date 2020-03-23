from algoritmo import AlgoritmoBarrido
from Punto import Punto
from Segmento import Segmento
from Reader import getSegments


def main():
    names = ["ejemplo_01/layer01", "ejemplo_01/layer02"]
    points = []
    segmentos = getSegments(names, points)

    for s in segmentos:
        print(s)

    barr = AlgoritmoBarrido(segmentos)
    barr.barrer()
    print(barr.R)


if __name__ == "__main__":
    main()
