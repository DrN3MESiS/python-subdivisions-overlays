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
      cycles.append(cycle)

    return cycles 

  def intersection(self,other):
    cycles = []

    for cycle in self.cycles:
      if cycle in other.cycles:
        cycles.append(cycle)

    return cycles

  def diferential(self,other):
    cycles = []

    for cycle in self.cycles:
      if cycle not in other.cycles:
        cycles.append(cycle)

    for cycle in other.cycles:
      if cycle not in self.cycles:
        cycles.append(cycle)

    return cycles    


