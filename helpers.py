from Edge import Edge

def resetMemDir(VERTEX, EDGES):
    for edge in EDGES:
        
        for v in VERTEX:
            if edge.gS() == v.gN():
                edge.setStart(v)
                break

        for e in EDGES:
            if edge.pair == e.gN():
                edge.pair = e
                
            if edge.next == e.gN():
                edge.next = e

            if edge.previous == e.gN():
                edge.previous = e
        
        
    
