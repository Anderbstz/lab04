import matplotlib.pyplot as plt
import networkx as nx
from collections import deque
import sys
import os

# Agregar el directorio padre para importar graph_list
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'graph_algorithms'))
from graph_list import Graph

def create_bfs_graph():
    """Crear el grafo usado en el ejemplo de BFS"""
    g = Graph()
    
    # Agregar vértices
    vertices = ['a', 'b', 'c', 'd', 'e', 'f']
    for vertex in vertices:
        g.addVertex(vertex)
    
    # Agregar aristas (grafo no dirigido)
    edges = [
        ('a', 'b'), ('a', 'c'),
        ('b', 'd'), ('b', 'e'),
        ('c', 'f'),
        ('d', 'e')
    ]
    
    for v1, v2 in edges:
        g.addEdge(v1, v2)
        g.addEdge(v2, v1)  # Para grafo no dirigido
    
    return g

def bfs_with_visualization(graph, start_vertex):
    """BFS que retorna el orden de visita y las distancias"""
    start = graph.getVertex(start_vertex)
    if start is None:
        return [], {}
    
    # Inicializar todos los vértices
    for vertex in graph.vertices.values():
        vertex.setDistance(float('inf'))
        vertex.setPrevious(None)
        vertex.visited = False
    
    start.setDistance(0)
    queue = deque([start])
    visit_order = []
    distances = {}
    
    while queue:
        current = queue.popleft()
        if not current.visited:
            current.visited = True
            visit_order.append(current.getId())
            distances[current.getId()] = current.getDistance()
            
            for neighbor in current.getAdjLists():
                if not neighbor.visited and neighbor.getDistance() == float('inf'):
                    neighbor.setDistance(current.getDistance() + 1)
                    neighbor.setPrevious(current)
                    queue.append(neighbor)
    
    return visit_order, distances

def visualize_bfs_graph():
    """Crear visualización del grafo BFS"""
    # Crear el grafo
    graph = create_bfs_graph()
    
    # Ejecutar BFS desde 'a'
    visit_order, distances = bfs_with_visualization(graph, 'a')
    
    # Crear grafo de NetworkX para visualización
    G = nx.Graph()
    
    # Agregar nodos
    for vertex_id in ['a', 'b', 'c', 'd', 'e', 'f']:
        G.add_node(vertex_id)
    
    # Agregar aristas
    edges = [
        ('a', 'b'), ('a', 'c'),
        ('b', 'd'), ('b', 'e'),
        ('c', 'f'),
        ('d', 'e')
    ]
    G.add_edges_from(edges)
    
    # Configurar la visualización
    plt.figure(figsize=(12, 8))
    
    # Posiciones de los nodos
    pos = nx.spring_layout(G, seed=42)
    
    # Colores basados en el orden de visita BFS
    colors = []
    for node in G.nodes():
        if node in visit_order:
            # Color más intenso para nodos visitados antes
            intensity = 1 - (visit_order.index(node) / len(visit_order))
            colors.append(plt.cm.Blues(0.3 + 0.7 * intensity))
        else:
            colors.append('lightgray')
    
    # Dibujar el grafo
    nx.draw(G, pos, 
            node_color=colors,
            node_size=1500,
            font_size=16,
            font_weight='bold',
            with_labels=True,
            edge_color='gray',
            width=2)
    
    # Agregar etiquetas de distancia
    distance_labels = {node: f"d={distances.get(node, '∞')}" for node in G.nodes()}
    pos_labels = {node: (pos[node][0], pos[node][1] - 0.1) for node in pos}
    
    for node, label in distance_labels.items():
        plt.text(pos_labels[node][0], pos_labels[node][1], label, 
                horizontalalignment='center', fontsize=10, 
                bbox=dict(boxstyle='round,pad=0.2', facecolor='white', alpha=0.8))
    
    plt.title(f"BFS Traversal desde '{visit_order[0] if visit_order else 'a'}'\n" +
              f"Orden de visita: {' → '.join(visit_order)}", 
              fontsize=14, fontweight='bold')
    
    # Agregar leyenda
    legend_elements = [
        plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=plt.cm.Blues(0.9), 
                  markersize=10, label='Visitado primero'),
        plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=plt.cm.Blues(0.3), 
                  markersize=10, label='Visitado después'),
        plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='lightgray', 
                  markersize=10, label='No visitado')
    ]
    plt.legend(handles=legend_elements, loc='upper right')
    
    plt.tight_layout()
    plt.savefig('c:\\Users\\Usuario\\lab04\\creacion_grafos\\bfs_graph.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    print(f"Orden de visita BFS: {visit_order}")
    print(f"Distancias desde 'a': {distances}")

if __name__ == "__main__":
    print("=== Visualización del Algoritmo BFS ===")
    visualize_bfs_graph()