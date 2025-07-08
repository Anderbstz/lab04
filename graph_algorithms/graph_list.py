class Vertex:
    def __init__(self, key, distance=float('inf')):
        self.id = key
        self.adjList = {}
        self.visited = False
        self.distance = distance
        self.previous = None

    def addNeighbor(self, nbr, weight=0):
        self.adjList[nbr] = weight

    def getAdjLists(self):
        return self.adjList.keys()

    def getId(self):
        return self.id

    def getWeight(self, nbr):
        return self.adjList[nbr]
    
    def setDistance(self, dist):
        self.distance = dist
    
    def getDistance(self):
        return self.distance
    
    def setPrevious(self, prev):
        self.previous = prev
    
    def getPrevious(self):
        return self.previous
    
    def setVisited(self):
        self.visited = True
    
    def __lt__(self, other):
        return self.distance < other.distance
    
    def __le__(self, other):
        return self.distance <= other.distance
    
    def __gt__(self, other):
        return self.distance > other.distance
    
    def __ge__(self, other):
        return self.distance >= other.distance
    
    def __eq__(self, other):
        return self.distance == other.distance
    
    def __hash__(self):
        return hash(self.id)

class Graph:
    def __init__(self):
        self.vertices = {}
        self.numVertices = 0

    def addVertex(self, key, distance=float('inf')):
        self.numVertices += 1
        newVertex = Vertex(key, distance)
        self.vertices[key] = newVertex
        return newVertex

    def getVertex(self, n):
        return self.vertices.get(n)

    def addEdge(self, f, t, weight=0):
        if f not in self.vertices:
            self.addVertex(f)
        if t not in self.vertices:
            self.addVertex(t)
        self.vertices[f].addNeighbor(self.vertices[t], weight)

    def getVertices(self):
        return self.vertices.keys()

    def getEdges(self):
        edges = []
        for v in self.vertices.values():
            for w in v.getAdjLists():
                edges.append((v.getId(), w.getId(), v.getWeight(w)))
        return edges

if __name__ == '__main__':
    g = Graph()
    for i in range(6):
        g.addVertex(i)
    g.addEdge(0, 1, 5)
    g.addEdge(0, 5, 2)
    g.addEdge(1, 2, 4)
    g.addEdge(2, 3, 9)
    g.addEdge(3, 4, 7)
    g.addEdge(3, 5, 3)
    g.addEdge(4, 0, 1)
    g.addEdge(5, 4, 8)
    g.addEdge(5, 2, 1)

    for v in g.vertices.values():
        for w in v.getAdjLists():
            print(f"({v.getId()}, {w.getId()}, {v.getWeight(w)})")