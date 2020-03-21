from Segmento import Segmento
from Punto import Punto


def getSegments(names=[], points=[]):
    if len(names) == 0:
        return BaseException
    segments = []

    for name in names:
        vertexFile = name+".ver"
        edgeFile = name+".ari"
        found_edges = readContentFromFiles(vertexFile, edgeFile, points)
        for edge in found_edges:
            segments.append(edge)

    return segments


def readContentFromFiles(vertFile, edgeFile, points=[]):
    edges = []
    try:
        __readPoints__(vertFile, points)
    except Exception as e:
        print(e)

    # print(points)  # delete

    try:
        edges = __convertToSegments__(edgeFile, points)
    except Exception as e:
        print(e)
    return edges


def __readPoints__(file, points):
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


def __convertToSegments__(file, points):
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
