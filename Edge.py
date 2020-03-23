class Edge:
    def __init__(self, startVertex=None, incidentFace=None, pair=None, nextEdge=None, previousEdge=None):
        super().__init__()
        self.start = startVertex
        self.incidentFace = incidentFace
        self.pair = pair
        self.next = nextEdge
        self.previous = previousEdge

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
