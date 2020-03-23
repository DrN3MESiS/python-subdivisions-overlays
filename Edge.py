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
        return f"|Edge: {self.name} -> (S: {type(self.start)} {self.start.name}) - (P: {type(self.pair)} {self.pair.name}) - (N: {type(self.pair)} {self.next.name}) - (Pr: {type(self.pair)} {self.previous.name})|"

    def gS(self):
        return self.start

    def gN(self):
        return self.name

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
