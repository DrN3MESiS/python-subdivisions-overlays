class Edge:
    def __init__(self, name, startVertex, pair=None, incidentFace=None, nextEdge=None, previousEdge=None):
        super().__init__()
        self.name = name
        self.start = startVertex
        self.incidentFace = incidentFace
        self.pair = pair
        self.next = nextEdge
        self.previous = previousEdge
        self.cycle = None

    def __repr__(self):
        return f" < {self.name} -- NE:{self.next.gN()} -- PR:{self.previous.gN()} >"

    def sC(self, c): #SetCycle
        self.cycle = c

    def gC(self): #GetCycle
        return self.cycle

    def gS(self): #GetStart
        return self.start

    def gN(self): #GetName
        return self.name

    def gP(self): #GetPair
        return self.pair

    def gNe(self): #GetNext
        return self.next

    def gPe(self): #GetPrevious
        return self.previous

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

