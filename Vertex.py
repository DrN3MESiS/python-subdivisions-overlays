from Constantes import eps

class Vertex:
    def __init__(self, name, x, y, edges=[]):
        super().__init__()
        self.name = name
        self.x = x
        self.y = y
        self.edges = edges
        self.closestEdge = None
        self.cycle = None
        self.closestLeftCycle = None
        

    def __repr__(self):
        return f"{self.name} -> ({self.x},{self.y})"

    def sCLC(self, cInf): #SetClosestLeftCycle
        if self.closestEdge == None:
            self.closestLeftCycle = cInf
            return 
        if self.closestEdge.gC() == self.cycle:
            self.closestLeftCycle = cInf
        else:
            self.closestLeftCycle = self.closestEdge.gC()

    def gCLC(self): #GetClosestLeftCycle
        return self.closestLeftCycle

    def sC(self, c): #SetCycle
        self.cycle = c

    def gC(self): #GetCycle
        return self.cycle

    def gN(self): #GetNext
        return self.name
    
    def gX(self): #GetX
        return self.x
        
    def gY(self): #GetY
        return self.y

    def gE(self): #GetEdges
        return self.edges

    def __eq__(self, otro):
        if abs(self.x-otro.x)<eps and abs(self.y-otro.y)<eps: return True 
        return False

    def __lt__(self, otro):
        if self.y> otro.y: return True
        if self.y< otro.y: return False
        if self.x< otro.x: return True
        return False

