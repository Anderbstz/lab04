from graph_list import Vertex, Graph
from queue_implementation import Queue

# BFS : Breadth First Search
def BFSTraversal(g, s):
    start = g.getVertex(s)
    start.setDistance(0)
    start.setPrevious(None)
    vertQueue = Queue()
    vertQueue.enQueue(start)

    while (vertQueue.size > 0):
        currentVert = vertQueue.deQueue()
        print(currentVert.getId())
        for nbr in currentVert.getAdjLists():
            if (nbr.visited == False):
                nbr.visited = True
                nbr.setDistance(currentVert.getDistance() + 1)
                nbr.setPrevious(currentVert)
                vertQueue.enQueue(nbr)
        currentVert.visited = True

def BFS(g):
    for v in g.vertices.values():
        if (v.visited == False):
            BFSTraversal(g, v.getId())

if __name__ == '__main__':
    g = Graph()
    g.addVertex('a')
    g.addVertex('b')
    g.addVertex('c')
    g.addVertex('d')
    g.addVertex('e')
    g.addVertex('f')
    g.addVertex('g')
    g.addVertex('h')
    g.addEdge('a', 'b', 1)
    g.addEdge('b', 'h', 1)
    g.addEdge('b', 'c', 1)
    g.addEdge('c', 'd', 1)
    g.addEdge('c', 'e', 1)
    g.addEdge('h', 'e', 1)
    g.addEdge('e', 'g', 1)
    g.addEdge('e', 'f', 1)
    print('Graph data:')
    for row in g.getEdges():
        print("%s -> %s : %s"%(row[0], row[1], row[2]))
    
    BFS(g)

    # Where does the graph start?
    for v in g.vertices.values():
        if v.previous == None :
            print("START IN : {} ".format(v.id))

    # Print
    for v in g.vertices.values():
        print("id:[{}] distance:[{}]".format(v.id, v.distance))