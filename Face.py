class Face:
    def __init__(self, internalEdges=[], externalEdges=[]):
        super().__init__()
        self.internalEdges = []
        self.externalEdges = []

    def pushInternal(self, internal):
        self.internalEdges.append(internal)

    def pushExternal(self, external):
        self.externalEdges.append(external)
