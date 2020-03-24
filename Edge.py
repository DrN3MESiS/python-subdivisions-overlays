class Edge:    
  
  def __init__(self, line):
    self.name = line[0]
    self.origin = line[1]
    self.couple = line[2]
    self.face = line[3]
    self.next = line[4]
    self.previous = line[5]

  def setName(self):
    self.name = self.name + "'"

  def setOrigin(self,origin):
    self.origin = origin

  def setCouple(self,couple):
    self.couple = couple

  def setFace(self,face):
    self.face = face

  def setNext(self,next):
    self.next = next

  def setPrevious(self,previous):
    self.previous = previous 

  def __repr__(self):
    return self.name

  def __str__(self):
    return self.name + "\t\t" + self.origin + "\t\t" + self.couple + "\t\t" + self.face + "\t\t" + self.next + "\t\t" + self.previous + "\n"
