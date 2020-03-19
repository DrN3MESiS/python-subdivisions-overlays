from Segmento import Segmento
from Punto import Punto


def getSegments(names=[]):
    if len(names) == 0:
        return BaseException
    segments = []

    for name in names:
        vertexFile = name+".ver"
        edgeFile = name+".ari"
        segments.append(readContentFromFiles(vertexFile, edgeFile))


def readContentFromFiles(vertFile, edgeFile):
    points = []
    edges = []
    try:
        points = __readPoints__(vertFile)
    except Exception as e:
        print(e)

    print(points)

    try:
        edges = __convertToSegments__(edgeFile, points)
    except Exception as e:
        print(e)


def __readPoints__(file):
    points = []
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
    return points


def __convertToSegments__(file, points):
    edges = []
    f = open(file, "r")
    if f.mode != "r":
        return Exception
    content = f.readlines()
    content = content[4:]
    for line in content:
        data = " ".join(line.split())
        data = data.split(" ")
        print(data)
