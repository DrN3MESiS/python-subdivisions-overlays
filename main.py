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
  for key in layer02.F:
    face = layer02.F[key]
  
  # face = layer01.F['f1'].union(layer02.F['f2'])
  # face = layer01.F['f1'].intersection(layer02.F['f2'])
  # face = layer01.F['f1'].diferential(layer02.F['f2'])
  # face.draw(layer_union.Elements)
  # layer01.F['f2'].draw(layer_union.Elements)
  # layer02.F['f4'].draw(layer_union.Elements)

if __name__=="__main__":
    main()
