from graph_list import Vertex, Graph
import heapq

# Dijkstra
def dijkstra(G, source, destination):
    '''Dijkstra's shortest path'''
    # Set the distance for the source node to zero
    source.setDistance(0)

    # Put tuple pair into the priority queue
    unvisitedQueue = [(v.getDistance(), v) for v in G.vertices.values()]
    #print(unvisitedQueue)
    heapq.heapify(unvisitedQueue)

    while len(unvisitedQueue):
        # Pops a vertex with the smallest distance
        uv = heapq.heappop(unvisitedQueue)
        current = uv[1]
        current.setVisited()

        # for next in v.adjacent:
        for next in current.adjList:
            # if visited, skip
            if next.visited:
                continue
            newDist = current.getDistance() + current.getWeight(next)

            if newDist < next.getDistance():
                next.setDistance(newDist)
                next.setPrevious(current)
                print( \
                'Updated : current = %s next = %s newDist = %s' \
                % (current.getId(), next.getId(), next.getDistance()))

            else:
                print( \
                'Not updated : current = %s next = %s newDist = %s' \
                % (current.getId(), next.getId(), next.getDistance()))

        # Rebuild heap
        # 1. Pop every item
        while len(unvisitedQueue):
            heapq.heappop(unvisitedQueue)
        # 2. Put all vertices not visited into the queue
        unvisitedQueue = [(v.getDistance(), v) for v in G.vertices.values() if not v.visited]
        heapq.heapify(unvisitedQueue)


def shortest(v, path):
    ''' make shortest path from v.previous'''
    if v.previous:
        path.append(v.previous.getId())
        shortest(v.previous, path)
    return

if __name__ == '__main__':
    g = Graph()
    g.addVertex('a')
    g.addVertex('b')
    g.addVertex('c')
    g.addVertex('d')
    g.addVertex('e')
    g.addEdge('a', 'b', 4)
    g.addEdge('a', 'c', 1)
    g.addEdge('c', 'b', 2)
    g.addEdge('b', 'e', 4)
    g.addEdge('c', 'd', 4)
    g.addEdge('d', 'e', 4)

    source = g.getVertex('a')
    destination = g.getVertex('e')
    dijkstra(g, source, destination)

    for v in g.vertices.values():
        print(source.getId(), " to ", v.getId(), "-->", v.getDistance())

    path = [destination.getId()]
    shortest(destination, path)
    print('The shortest path from a to e is: %s' % (path[::-1]))