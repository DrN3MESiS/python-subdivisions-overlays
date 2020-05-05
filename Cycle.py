from Punto import Punto
from Punto import Punto
from Edge import Edge
import pygame

class Cycle:

    def __init__(self, origin, elements):
        self.Edges = [origin]
        next = elements[origin].next
        self.lefter = [elements[origin],elements[elements[origin].origin]]
        while next != origin:
            vertex = elements[elements[next].origin]
            if(vertex.x < self.lefter[1].x):
                self.lefter = [elements[next],vertex]
            self.Edges.append(next)
            next = elements[next].next 
        index = self.Edges.index(self.lefter[0].name)
        v = elements[elements[self.Edges[index]].origin]
        a = Punto.vector(v,elements[elements[self.Edges[index+1]].origin])
        b = Punto.vector(elements[elements[self.Edges[index-1]].origin],v)
        if(Edge.cross(a,b) >= 0):
            self.clockwise = True
        else:
            self.clockwise = False

    def setNext(self,next):        
        self.next = next

    def setPrevious(self,previous):
        self.previous = previous 

    def removeEdges(self, edges):
        for edge in self.Edges:
            if edge in edges:
                del edges[edge]

    def set_name(self,number):
        self.name = "C" + str(number)            

    def __str__(self):
        return self.name

    def __repr__(self):
        return repr(self.Edges)     

    def draw(self,window,elements,scale=20,inside=True):
        white = (255,255,255)
        black = (0,0,0)     

        print(self)

        points = self.get_points(elements,scale)

        if self.clockwise:
            window.fill(black)
            pygame.draw.polygon(window,white,points)
        else:
            pygame.draw.polygon(window,black,points)
        
        return points

    def get_points(self,elements,scale):
        points = []

        for edge in self.Edges:
            points.append(elements[elements[edge].origin].pygame_point(scale))

        return points