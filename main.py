from Layer import Layer
import math

def main():
  dir = "ejemplo_01/"

  layer01 = Layer(dir +"layer01")
  print(layer01)

  layer02 = Layer(dir+"layer02")
  print(layer02)

  layer_union = layer01.layer_union(layer02)
  print(layer_union)


if __name__=="__main__":
    main()
