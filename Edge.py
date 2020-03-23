class Edge:
    def __init__(self, name, startVertex, pair=None, incidentFace=None, nextEdge=None, previousEdge=None):
        super().__init__()
        self.name = name
        self.start = startVertex
        self.incidentFace = incidentFace
        self.pair = pair
        self.next = nextEdge
        self.previous = previousEdge

    def __repr__(self):
        return f"|{self.name} -> S:{self.start}|"

    def gS(self):
        return self.start

    def setStart(self, start):
        self.start = start

    def setIncidentFace(self, incidentFace):
        self.incidentFace = incidentFace

    def setPair(self, pair):
        self.pair = pair

    def setNext(self, next):
        self.next = next

    def setPrevious(self, previous):
        self.previous = previous
