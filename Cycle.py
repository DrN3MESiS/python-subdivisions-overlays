class Cycle():
    def __init__(self, name, inf):
        self.name = name
        self.edges = []
        self.mLv = None
        self.inf = inf
        self.isHole = False
    def addEdge(self, e):
        self.edges.append(e)

    def __repr__(self):
        return f"<< - {self.name} - [Edges:{len(self.edges)}] [isHole?:{self.isHole}] [isInf?:{self.inf}]>> "

    def __iter__(self):
        return iter(self.edges)

    def gN(self): #GetName
        return self.name

    def setMLV(self, mlv):
        self.mLv  = mlv

    def aC(self, cycle):
        for e in self.edges:
            e.sC(cycle)