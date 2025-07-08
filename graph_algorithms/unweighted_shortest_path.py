from graph_list import Vertex, Graph
from queue_implementation import Queue

# Unweighted Shortest Path with BFS
def UnweightedShortestPath(g, s):
    source = g.getVertex(s)
    source.setDistance(0)
    source.setPrevious(None)
    vertQueue = Queue()
    vertQueue.enQueue(source)
    while (vertQueue.size > 0):
        currentVert = vertQueue.deQueue()
        for nbr in currentVert.getAdjLists():
            if nbr.getDistance() == -1:
                nbr.setDistance(currentVert.getDistance() + 1)
                nbr.setPrevious(currentVert)
                vertQueue.enQueue(nbr)

    for v in g.vertices.values():
        print(source.getId(), " to ", v.getId(), "-->", v.getDistance())

if __name__ == '__main__':
    g = Graph()
    g.addVertex('a', -1)
    g.addVertex('b', -1)
    g.addVertex('c', -1)
    g.addVertex('d', -1)
    g.addVertex('e', -1)
    g.addVertex('f', -1)
    g.addVertex('g', -1)
    g.addVertex('h', -1)
    g.addEdge('a', 'b')
    g.addEdge('b', 'h')
    g.addEdge('b', 'c')
    g.addEdge('c', 'd')
    g.addEdge('c', 'e')
    g.addEdge('h', 'e')
    g.addEdge('e', 'g')
    g.addEdge('e', 'f')

    UnweightedShortestPath(g,"a")