class Vertex:
    def __init__(self, name, x, y, edges=[]):
        super().__init__()
        self.name = name
        self.x = x
        self.y = y
        self.edges = edges

    def __repr__(self):
        return f"{self.name} -> ({self.x},{self.y})"

    def __str__(self):
        return self.name

    def gN(self):
        return self.name

    def pushEdge(self, edge):
        self.edges.append(edge)
