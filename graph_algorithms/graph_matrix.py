class Vertex:
    def __init__(self, node):
        self.id = node
    def getId(self):
        return self.id
    def setId(self, id):
        self.id = id

class Graph:
    def __init__(self, numVertices, cost=-1):
        self.adjMatrix = [[cost for _ in range(numVertices)] for _ in range(numVertices)]
        self.numVertices = numVertices
        self.vertices = [Vertex(i) for i in range(numVertices)]

    def setVertex(self, vtx, id):
        if 0 <= vtx < self.numVertices:
            self.vertices[vtx].setId(id)

    def getVertexIndex(self, n):
        for i, v in enumerate(self.vertices):
            if v.getId() == n:
                return i
        return -1

    def addEdge(self, frm, to, cost=0):
        idx_frm = self.getVertexIndex(frm)
        idx_to = self.getVertexIndex(to)
        if idx_frm != -1 and idx_to != -1:
            self.adjMatrix[idx_frm][idx_to] = cost
            self.adjMatrix[idx_to][idx_frm] = cost

    def printMatrix(self):
        for row in self.adjMatrix:
            print(row)

    def getEdges(self):
        edges = []
        for i in range(self.numVertices):
            for j in range(self.numVertices):
                if self.adjMatrix[i][j] != -1:
                    edges.append((self.vertices[i].getId(), self.vertices[j].getId(), self.adjMatrix[i][j]))
        return edges

if __name__ == '__main__':
    G = Graph(6)
    G.setVertex(0, 'a')
    G.setVertex(1, 'b')
    G.setVertex(2, 'c')
    G.setVertex(3, 'd')
    G.setVertex(4, 'e')
    G.setVertex(5, 'f')
    
    G.addEdge('a', 'e', 10)
    G.addEdge('a', 'c', 20)
    G.addEdge('c', 'b', 30)
    G.addEdge('b', 'e', 40)
    G.addEdge('e', 'd', 50)
    G.addEdge('f', 'e', 60)

    print("Matriz de adyacencia:")
    G.printMatrix()
    print("Aristas:")
    print(G.getEdges())