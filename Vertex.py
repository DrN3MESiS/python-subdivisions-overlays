from Constantes import eps

class Vertex:
    def __init__(self, name, x, y, edges=[]):
        super().__init__()
        self.name = name
        self.x = x
        self.y = y
        self.edges = edges
        self.closestEdge = None
        

    def __repr__(self):
        return f"{self.name} -> ({self.x},{self.y})"

    def gN(self):
        return self.name
    
    def gX(self):
        return self.x
        
    def gY(self):
        return self.y

    def gE(self):
        return self.edges

    def __eq__(self, otro):
        if abs(self.x-otro.x)<eps and abs(self.y-otro.y)<eps: return True 
        return False

    def __lt__(self, otro):
        if self.y> otro.y: return True
        if self.y< otro.y: return False
        if self.x< otro.x: return True
        return False

