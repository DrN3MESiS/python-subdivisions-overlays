class Face:
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.internalEdges = []
        self.externalEdges = []

    def pushInternal(self, internal):
        self.internalEdges.append(internal)

    def pushExternal(self, external):
        self.externalEdges.append(external)
