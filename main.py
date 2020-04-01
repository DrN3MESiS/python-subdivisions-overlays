from Layer import Layer
from Cycles import Cycles
from Segmento import Segmento
import math

def main():
  dir = "ejemplo_01/"

  layer01 = Layer(dir +"layer01")
  print(layer01)

  layer02 = Layer(dir+"layer02")
  print(layer02)

  layer_union = layer01.layer_union(layer02)
  cycles = Cycles(layer_union)
  #cycles.get_segmentos()
  print(cycles)


if __name__=="__main__":
    main()
