class Vertex:
    def __init__(self, coords=(), edges=[]):
        super().__init__()
        self.coords = coords
        self.edges = edges

    def pushEdge(self, edge):
        self.edges.append(edge)

    def setCoords(self, coords):
        self.coords = coords
