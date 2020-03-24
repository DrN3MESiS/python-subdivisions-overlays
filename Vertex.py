class Vertex:

  def __init__(self,line):
    self.name = line[0]
    self.x = float(line[1])
    self.y = float(line[2])
    self.edge = line[3]

  def setEdge(self,edge):
    self.edge = edge

  def __repr__(self):
    return self.name

  def __str__(self):
    return self.name + "\t\t" + str(self.x) + "\t\t" + str(self.y) + "\t\t" + self.edge + "\n"