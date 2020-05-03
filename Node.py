class Node:
    next = None
    previous = None

    def __init__(self,cycle):
        self.cycle = cycle

    def set_next(self,next):
        self.next = next 

    def set_previous(self,previous):
        self.previous = previous 

    def __repr__(self):
        return str(self.cycle) + "->" + repr(self.next)

    def get_last(self):
        if self.next:
            return self.next.get_last()
        else:    
            return self   
