import matplotlib.pyplot as plt
import networkx as nx
from collections import deque
import sys
import os

# Agregar el directorio padre para importar graph_list
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'graph_algorithms'))
from graph_list import Graph

def create_unweighted_graph():
    """Crear el grafo usado en el ejemplo de camino más corto sin pesos"""
    g = Graph()
    
    # Agregar vértices
    vertices = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    for vertex in vertices:
        g.addVertex(vertex)
    
    # Agregar aristas (grafo dirigido)
    edges = [
        ('a', 'b'), ('a', 'c'),
        ('b', 'd'), ('b', 'e'),
        ('c', 'f'),
        ('d', 'e'), ('d', 'g'),
        ('e', 'g'),
        ('f', 'g')
    ]
    
    for v1, v2 in edges:
        g.addEdge(v1, v2)
    
    return g

def unweighted_shortest_path_with_visualization(graph, start_vertex):
    """Algoritmo de camino más corto sin pesos que retorna distancias y caminos"""
    start = graph.getVertex(start_vertex)
    if start is None:
        return {}, {}
    
    # Inicializar todos los vértices
    for vertex in graph.vertices.values():
        vertex.setDistance(-1)
        vertex.setPrevious(None)
    
    start.setDistance(0)
    queue = deque([start])
    distances = {}
    paths = {}
    
    while queue:
        current = queue.popleft()
        distances[current.getId()] = current.getDistance()
        
        for neighbor in current.getAdjLists():
            if neighbor.getDistance() == -1:  # No visitado
                neighbor.setDistance(current.getDistance() + 1)
                neighbor.setPrevious(current)
                queue.append(neighbor)
    
    # Reconstruir caminos
    for vertex_id in distances:
        path = []
        current = graph.getVertex(vertex_id)
        while current is not None:
            path.append(current.getId())
            current = current.getPrevious()
        paths[vertex_id] = path[::-1]
    
    return distances, paths

def visualize_unweighted_shortest_path():
    """Crear visualización del grafo de camino más corto sin pesos"""
    # Crear el grafo
    graph = create_unweighted_graph()
    
    # Ejecutar algoritmo desde 'a'
    distances, paths = unweighted_shortest_path_with_visualization(graph, 'a')
    
    # Crear grafo dirigido de NetworkX para visualización
    G = nx.DiGraph()
    
    # Agregar nodos
    for vertex_id in ['a', 'b', 'c', 'd', 'e', 'f', 'g']:
        G.add_node(vertex_id)
    
    # Agregar aristas
    edges = [
        ('a', 'b'), ('a', 'c'),
        ('b', 'd'), ('b', 'e'),
        ('c', 'f'),
        ('d', 'e'), ('d', 'g'),
        ('e', 'g'),
        ('f', 'g')
    ]
    G.add_edges_from(edges)
    
    # Configurar la visualización
    plt.figure(figsize=(14, 10))
    
    # Posiciones de los nodos (layout jerárquico)
    pos = nx.spring_layout(G, seed=42)
    
    # Colores basados en la distancia desde 'a'
    colors = []
    max_distance = max(distances.values()) if distances else 1
    
    for node in G.nodes():
        if node in distances:
            # Color más intenso para nodos más cercanos
            intensity = 1 - (distances[node] / max_distance)
            colors.append(plt.cm.Reds(0.3 + 0.7 * intensity))
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
            width=2,
            arrows=True,
            arrowsize=20,
            arrowstyle='->')
    
    # Agregar etiquetas de distancia
    distance_labels = {node: f"d={distances.get(node, '∞')}" for node in G.nodes()}
    pos_labels = {node: (pos[node][0], pos[node][1] - 0.15) for node in pos}
    
    for node, label in distance_labels.items():
        plt.text(pos_labels[node][0], pos_labels[node][1], label, 
                horizontalalignment='center', fontsize=10, 
                bbox=dict(boxstyle='round,pad=0.2', facecolor='white', alpha=0.8))
    
    plt.title("Camino Más Corto Sin Pesos (BFS)\n" +
              "Desde vértice 'a' - Grafo Dirigido", 
              fontsize=14, fontweight='bold')
    
    # Agregar leyenda
    legend_elements = [
        plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=plt.cm.Reds(0.9), 
                  markersize=10, label='Distancia 0'),
        plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=plt.cm.Reds(0.6), 
                  markersize=10, label='Distancia 1-2'),
        plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=plt.cm.Reds(0.3), 
                  markersize=10, label='Distancia 3+'),
        plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='lightgray', 
                  markersize=10, label='No alcanzable')
    ]
    plt.legend(handles=legend_elements, loc='upper right')
    
    plt.tight_layout()
    plt.savefig('c:\\Users\\Usuario\\lab04\\creacion_grafos\\unweighted_shortest_path_graph.png', 
                dpi=300, bbox_inches='tight')
    plt.show()
    
    print("=== Distancias desde 'a' ===")
    for vertex, distance in sorted(distances.items()):
        print(f"Vértice {vertex}: distancia {distance}")
    
    print("\n=== Caminos más cortos ===")
    for vertex, path in sorted(paths.items()):
        if len(path) > 1:
            print(f"Camino a {vertex}: {' → '.join(path)}")

if __name__ == "__main__":
    print("=== Visualización del Algoritmo de Camino Más Corto Sin Pesos ===")
    visualize_unweighted_shortest_path()