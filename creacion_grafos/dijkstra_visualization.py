import matplotlib.pyplot as plt
import networkx as nx
import heapq
import sys
import os

# Agregar el directorio padre para importar graph_list
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'graph_algorithms'))
from graph_list import Graph

def create_weighted_graph():
    """Crear el grafo ponderado usado en el ejemplo de Dijkstra"""
    g = Graph()
    
    # Agregar vértices
    vertices = ['a', 'b', 'c', 'd', 'e']
    for vertex in vertices:
        g.addVertex(vertex)
    
    # Agregar aristas con pesos (grafo dirigido)
    weighted_edges = [
        ('a', 'b', 4), ('a', 'c', 2),
        ('b', 'c', 1), ('b', 'd', 5),
        ('c', 'd', 8), ('c', 'e', 10),
        ('d', 'e', 2)
    ]
    
    for v1, v2, weight in weighted_edges:
        g.addEdge(v1, v2, weight)
    
    return g, weighted_edges

def dijkstra_with_visualization(graph, start_vertex):
    """Algoritmo de Dijkstra que retorna distancias y caminos"""
    start = graph.getVertex(start_vertex)
    if start is None:
        return {}, {}
    
    # Inicializar todos los vértices
    unvisited = []
    for vertex in graph.vertices.values():
        vertex.setDistance(float('inf'))
        vertex.setPrevious(None)
        vertex.visited = False
        unvisited.append(vertex)
    
    start.setDistance(0)
    heapq.heapify(unvisited)
    
    distances = {}
    paths = {}
    
    while unvisited:
        current = heapq.heappop(unvisited)
        current.setVisited()
        distances[current.getId()] = current.getDistance()
        
        for neighbor in current.getAdjLists():
            if not neighbor.visited:
                new_distance = current.getDistance() + current.getWeight(neighbor)
                if new_distance < neighbor.getDistance():
                    neighbor.setDistance(new_distance)
                    neighbor.setPrevious(current)
        
        # Re-heapify después de cambios
        heapq.heapify(unvisited)
    
    # Reconstruir caminos
    for vertex_id in distances:
        if distances[vertex_id] != float('inf'):
            path = []
            current = graph.getVertex(vertex_id)
            while current is not None:
                path.append(current.getId())
                current = current.getPrevious()
            paths[vertex_id] = path[::-1]
    
    return distances, paths

def visualize_dijkstra_graph():
    """Crear visualización del grafo de Dijkstra"""
    # Crear el grafo
    graph, weighted_edges = create_weighted_graph()
    
    # Ejecutar Dijkstra desde 'a'
    distances, paths = dijkstra_with_visualization(graph, 'a')
    
    # Crear grafo dirigido de NetworkX para visualización
    G = nx.DiGraph()
    
    # Agregar nodos
    for vertex_id in ['a', 'b', 'c', 'd', 'e']:
        G.add_node(vertex_id)
    
    # Agregar aristas con pesos
    for v1, v2, weight in weighted_edges:
        G.add_edge(v1, v2, weight=weight)
    
    # Configurar la visualización
    plt.figure(figsize=(14, 10))
    
    # Posiciones de los nodos
    pos = nx.spring_layout(G, seed=42)
    
    # Colores basados en la distancia desde 'a'
    colors = []
    max_distance = max([d for d in distances.values() if d != float('inf')]) if distances else 1
    
    for node in G.nodes():
        if node in distances and distances[node] != float('inf'):
            # Color más intenso para nodos más cercanos
            intensity = 1 - (distances[node] / max_distance)
            colors.append(plt.cm.Greens(0.3 + 0.7 * intensity))
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
    
    # Agregar etiquetas de peso en las aristas
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels, font_size=12, 
                                bbox=dict(boxstyle='round,pad=0.2', facecolor='yellow', alpha=0.7))
    
    # Agregar etiquetas de distancia
    distance_labels = {}
    for node in G.nodes():
        if node in distances:
            if distances[node] == float('inf'):
                distance_labels[node] = "d=∞"
            else:
                distance_labels[node] = f"d={distances[node]}"
        else:
            distance_labels[node] = "d=∞"
    
    pos_labels = {node: (pos[node][0], pos[node][1] - 0.15) for node in pos}
    
    for node, label in distance_labels.items():
        plt.text(pos_labels[node][0], pos_labels[node][1], label, 
                horizontalalignment='center', fontsize=10, 
                bbox=dict(boxstyle='round,pad=0.2', facecolor='white', alpha=0.8))
    
    plt.title("Algoritmo de Dijkstra - Camino Más Corto Con Pesos\n" +
              "Desde vértice 'a' - Grafo Dirigido Ponderado", 
              fontsize=14, fontweight='bold')
    
    # Agregar leyenda
    legend_elements = [
        plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=plt.cm.Greens(0.9), 
                  markersize=10, label='Distancia mínima'),
        plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=plt.cm.Greens(0.6), 
                  markersize=10, label='Distancia media'),
        plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=plt.cm.Greens(0.3), 
                  markersize=10, label='Distancia máxima'),
        plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='lightgray', 
                  markersize=10, label='No alcanzable')
    ]
    plt.legend(handles=legend_elements, loc='upper right')
    
    plt.tight_layout()
    plt.savefig('c:\\Users\\Usuario\\lab04\\creacion_grafos\\dijkstra_graph.png', 
                dpi=300, bbox_inches='tight')
    plt.show()
    
    print("=== Distancias mínimas desde 'a' (Dijkstra) ===")
    for vertex, distance in sorted(distances.items()):
        if distance == float('inf'):
            print(f"Vértice {vertex}: No alcanzable")
        else:
            print(f"Vértice {vertex}: distancia {distance}")
    
    print("\n=== Caminos más cortos ===")
    for vertex, path in sorted(paths.items()):
        if len(path) > 1:
            print(f"Camino a {vertex}: {' → '.join(path)} (costo: {distances[vertex]})")

if __name__ == "__main__":
    print("=== Visualización del Algoritmo de Dijkstra ===")
    visualize_dijkstra_graph()