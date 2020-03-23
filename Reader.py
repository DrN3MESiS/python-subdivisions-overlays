from Segmento import Segmento
from Punto import Punto
from Vertex import Vertex
from Edge import Edge


def getSegments(names=[], VERTEX=[], EDGES=[]):
    if len(names) == 0:
        return BaseException
    points = []
    segments = []

    for name in names:
        vertexFile = name+".ver"
        edgeFile = name+".ari"
        found_edges = readContentFromFiles(
            vertexFile, edgeFile, points, VERTEX, EDGES)
        for edge in found_edges:
            segments.append(edge)

    return segments


def readContentFromFiles(vertFile, edgeFile, points=[], VERTEX=[], EDGES=[]):
    edges = []
    try:
        __readPoints__(vertFile, points, VERTEX)
    except Exception as e:
        print(e)
    try:
        edges = __convertToSegments__(edgeFile, points, VERTEX, EDGES)
    except Exception as e:
        print(e)
    return edges


def __readPoints__(file, points, VERTEX=[]):
    f = open(file, "r")
    if f.mode != "r":
        return Exception
    content = f.readlines()
    content = content[4:]
    for line in content:
        data = " ".join(line.split())
        data = data.split(" ")
        x = int(data[1])
        y = int(data[2])
        points.append(Punto(x, y))
        VERTEX.append(Vertex(data[0], x, y, [data[3]]))


def __convertToSegments__(file, points, VERTEX=[], EDGES=[]):
    edges = []
    f = open(file, "r")
    if f.mode != "r":
        return Exception
    content = f.readlines()
    content = content[4:]
    origin_points = []
    i = 1
    for line in content:
        data = " ".join(line.split())
        data = data.split(" ")

        e = Edge(data[0], data[1], data[2], data[3], data[4], data[5])
        EDGES.append(e)
        origin = data[1]
        origin = str(origin).replace("p", "")
        origin = int(origin)
        origin_points.append(origin)
        i += 1
        if i % 2 != 0:
            PA = origin_points[0]
            PB = origin_points[1]
            edges.append(Segmento(points[PA-1], points[PB-1]))
            origin_points.pop()
            origin_points.pop()
    return edges
