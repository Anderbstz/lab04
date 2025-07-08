from graph_list import Vertex, Graph

# DFS : Depth First Search
def dfs(g, currentVert, visited):
    # mark the visited node
    visited[currentVert] = True
    print("traversal: " + currentVert.getId())
    # take a neighbouring node
    for nbr in currentVert.getAdjLists():
        # condition to check whether the neighbour node is already visited
        if nbr not in visited:
            # recursively traverse the neighbouring node
            dfs(g, nbr, visited)

def DFSTraversal(g):
    # Dictionary to mark the visited nodes
    visited = {}
    # G contains vertex objects
    for currentVert in g.vertices.values():
        # Start traversing from the root node only if its not visited
        if currentVert not in visited:
            # For a connected graph this is called only once
            dfs(g, currentVert, visited)

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
    
    DFSTraversal(g)