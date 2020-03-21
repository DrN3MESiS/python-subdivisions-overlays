class Face:

  def __init__(self,line):
    self.name = line[0]
    self.external = line[1]
    self.internal = line[2]

  def setExternal(self,external):
    self.external = external

  def setInternal(self,internal):
    self.internal = internal  

  def __repr__(self):
      return self.name

  def __str__(self):
    return self.name + " " + repr(self.external) + " " + repr(self.internal)