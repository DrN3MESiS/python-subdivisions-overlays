from Layer import Layer
import math

def main():
  dir = "ejemplo_01/"

  layer01 = Layer(dir +"layer01")
  print(layer01)

  layer02 = Layer(dir+"layer02")
  print(layer02)

  layer01.layer_union(layer02)

if __name__=="__main__":
    main()
