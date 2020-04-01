class Cycle():
    def __init__(self, name):
        self.name = name
        self.edges = []
        self.mLv = None

    def addEdge(self, e):
        self.edges.append(e)

    def __repr__(self):
        return f"< {self.name} {self.edges} > "

    def __iter__(self):
        return iter(self.edges)

    def setMLV(self, mlv):
        self.mLv  = mlv