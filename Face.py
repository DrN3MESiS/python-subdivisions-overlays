import pygame

class Face:

  def __init__(self,line):
    self.name = line[0]
    self.external = line[1]
    self.internal = line[2]
    self.cycles = []

  def setExternal(self,external):
    self.external = external

  def setInternal(self,internal):
    self.internal = internal  

  def __repr__(self):
      return self.name

  def __str__(self):
    return self.name + "\t\t" + self.internal + "\t\t" + self.external + "\n"

  def set_cycle(self,cycle):
    if cycle not in self.cycles:
      self.cycles.append(cycle)

  def union(self,other):
    cycles = []

    for cycle in self.cycles:
      cycles.append(cycle)

    for cycle in other.cycles:
      if cycle not in cycles:
        cycles.append(cycle)

    line = [self.name+"|"+other.name,None,None]
    face = Face(line)

    face.cycles = cycles
    return face 

  def intersection(self,other):
    cycles = []

    for cycle in self.cycles:
      if cycle in other.cycles:
        cycles.append(cycle)

    line = [self.name+"&"+other.name,None,None]
    face = Face(line)

    face.cycles = cycles
    return face

  def diferential(self,other):
    cycles = []

    for cycle in self.cycles:
      if cycle not in other.cycles:
        cycles.append(cycle)

    for cycle in other.cycles:
      if cycle not in self.cycles:
        cycles.append(cycle)

    line = [self.name+"-"+other.name,None,None]
    face = Face(line)

    face.cycles = cycles
    return face    

  def draw(self,layer):
    white = (255,255,255)

    elements = layer.Elements
    graph = layer.graph

    window = pygame.display.set_mode((400,400))
    window.fill(white)

    for cycle in self.cycles:
      cycle.draw(window,elements,graph)

    while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            pygame.display.update()  

