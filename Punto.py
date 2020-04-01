from Constantes import eps
import math

class Punto:
  def __init__(self, x=0, y=0, line=None):
    self.x = x
    self.y = y
    self.name = f"({self.x},{self.y})"
    self.edge = ""
    if(line != None):
      self.name = line[0]
      self.x = float(line[1])
      self.y = float(line[2])
      self.edge = line[3]
  def __eq__(self, otro):
     if abs(self.x-otro.x)<eps and abs(self.y-otro.y)<eps: return True 
     return False 
  def __lt__(self, otro):
    if self.y> otro.y: return True
    if self.y< otro.y: return False
    if self.x< otro.x: return True
    return False 
  def __hash__(self):
    return self.x<<8 + self.y

  def setEdge(self,edge):
    self.edge = edge

  def __repr__(self):
    return self.name

  def __str__(self):
    return self.name + "\t\t" + str(self.x) + "\t\t" + str(self.y) + "\t\t" + self.edge + "\n"

  @staticmethod
  def cw(origin,end):
    y = end.y - origin.y
    x = end.x - origin.x
    cw = math.atan2(x,y)  
    if(cw < 0):
      cw = cw + 6
    return cw

  @staticmethod
  def vector(origin, end):
    return Punto(end.x - origin.x, end.y - end.x) 