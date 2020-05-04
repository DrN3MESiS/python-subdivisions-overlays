from Layer import Layer
import math

def main():
  dir = "ejemplo_01/"

  layer01 = Layer(dir +"layer01")

  layer02 = Layer(dir+"layer02")

  layer_union = layer01.layer_union(layer02)

  # print(layer01)
  # print(layer02)
  # print(layer_union)

  for key in layer01.F:
    face = layer01.F[key]
    print(key)
    print(face.cycles)
  for key in layer02.F:
    face = layer02.F[key]
    print(key)
    print(face.cycles)
  # layer_union.F["f1"]

if __name__=="__main__":
    main()
