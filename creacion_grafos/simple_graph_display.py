#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Visualizaciones simples de grafos usando solo texto
No requiere matplotlib ni networkx
"""

import sys
import os
from collections import deque

# Agregar el directorio padre para importar graph_list
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'graph_algorithms'))
from graph_list import Graph

def print_separator(title):
    """Imprimir separador con título"""
    print("\n" + "="*60)
    print(f"  {title}")
    print("="*60)

def display_graph_structure(graph, title):
    """Mostrar la estructura del grafo en formato texto"""
    print(f"\n📊 Estructura del grafo - {title}")
    print("-" * 40)
    
    for vertex in graph.vertices.values():
        neighbors = [neighbor.getId() for neighbor in vertex.getAdjLists()]
        if hasattr(vertex, 'getWeight') and neighbors:
            # Mostrar con pesos si están disponibles
            weighted_neighbors = []
            for neighbor in vertex.getAdjLists():
                try:
                    weight = vertex.getWeight(neighbor)
                    weighted_neighbors.append(f"{neighbor.getId()}({weight})")
                except:
                    weighted_neighbors.append(neighbor.getId())
            print(f"  {vertex.getId()} → {', '.join(weighted_neighbors)}")
        else:
            print(f"  {vertex.getId()} → {', '.join(neighbors) if neighbors else 'sin conexiones'}")

def bfs_text_visualization():
    """Visualización en texto del algoritmo BFS"""
    print_separator("ALGORITMO BFS - RECORRIDO EN ANCHURA")
    
    # Crear el grafo
    g = Graph()
    vertices = ['a', 'b', 'c', 'd', 'e', 'f']
    for vertex in vertices:
        g.addVertex(vertex)
    
    # Agregar aristas (grafo no dirigido)
    edges = [('a', 'b'), ('a', 'c'), ('b', 'd'), ('b', 'e'), ('c', 'f'), ('d', 'e')]
    for v1, v2 in edges:
        g.addEdge(v1, v2)
        g.addEdge(v2, v1)  # Para grafo no dirigido
    
    display_graph_structure(g, "BFS (No dirigido)")
    
    # Ejecutar BFS
    start = g.getVertex('a')
    for vertex in g.vertices.values():
        vertex.setDistance(float('inf'))
        vertex.setPrevious(None)
        vertex.visited = False
    
    start.setDistance(0)
    queue = deque([start])
    visit_order = []
    distances = {}
    
    print("\n🔍 Proceso de BFS paso a paso:")
    step = 1
    
    while queue:
        current = queue.popleft()
        if not current.visited:
            current.visited = True
            visit_order.append(current.getId())
            distances[current.getId()] = current.getDistance()
            
            print(f"  Paso {step}: Visitando '{current.getId()}' (distancia: {current.getDistance()})")
            step += 1
            
            for neighbor in current.getAdjLists():
                if not neighbor.visited and neighbor.getDistance() == float('inf'):
                    neighbor.setDistance(current.getDistance() + 1)
                    neighbor.setPrevious(current)
                    queue.append(neighbor)
                    print(f"    → Agregando '{neighbor.getId()}' a la cola (distancia: {neighbor.getDistance()})")
    
    print(f"\n📋 Resultado BFS:")
    print(f"   Orden de visita: {' → '.join(visit_order)}")
    print(f"   Distancias desde 'a': {distances}")

def unweighted_shortest_path_text_visualization():
    """Visualización en texto del camino más corto sin pesos"""
    print_separator("CAMINO MÁS CORTO SIN PESOS")
    
    # Crear el grafo
    g = Graph()
    vertices = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    for vertex in vertices:
        g.addVertex(vertex)
    
    # Agregar aristas (grafo dirigido)
    edges = [('a', 'b'), ('a', 'c'), ('b', 'd'), ('b', 'e'), ('c', 'f'), 
             ('d', 'e'), ('d', 'g'), ('e', 'g'), ('f', 'g')]
    for v1, v2 in edges:
        g.addEdge(v1, v2)
    
    display_graph_structure(g, "Camino más corto sin pesos (Dirigido)")
    
    # Ejecutar algoritmo
    start = g.getVertex('a')
    for vertex in g.vertices.values():
        vertex.setDistance(-1)
        vertex.setPrevious(None)
    
    start.setDistance(0)
    queue = deque([start])
    distances = {}
    paths = {}
    
    print("\n🔍 Calculando caminos más cortos:")
    
    while queue:
        current = queue.popleft()
        distances[current.getId()] = current.getDistance()
        
        for neighbor in current.getAdjLists():
            if neighbor.getDistance() == -1:  # No visitado
                neighbor.setDistance(current.getDistance() + 1)
                neighbor.setPrevious(current)
                queue.append(neighbor)
                print(f"  '{current.getId()}' → '{neighbor.getId()}' (distancia: {neighbor.getDistance()})")
    
    # Reconstruir caminos
    for vertex_id in distances:
        path = []
        current = g.getVertex(vertex_id)
        while current is not None:
            path.append(current.getId())
            current = current.getPrevious()
        paths[vertex_id] = path[::-1]
    
    print(f"\n📋 Resultados:")
    for vertex, distance in sorted(distances.items()):
        path = ' → '.join(paths[vertex]) if len(paths[vertex]) > 1 else vertex
        print(f"   Vértice {vertex}: distancia {distance}, camino: {path}")

def dijkstra_text_visualization():
    """Visualización en texto del algoritmo de Dijkstra"""
    print_separator("ALGORITMO DE DIJKSTRA - CAMINO MÁS CORTO CON PESOS")
    
    # Crear el grafo
    g = Graph()
    vertices = ['a', 'b', 'c', 'd', 'e']
    for vertex in vertices:
        g.addVertex(vertex)
    
    # Agregar aristas con pesos
    weighted_edges = [('a', 'b', 4), ('a', 'c', 2), ('b', 'c', 1), ('b', 'd', 5),
                     ('c', 'd', 8), ('c', 'e', 10), ('d', 'e', 2)]
    
    for v1, v2, weight in weighted_edges:
        g.addEdge(v1, v2, weight)
    
    display_graph_structure(g, "Dijkstra (Dirigido con pesos)")
    
    # Mostrar tabla de pesos
    print("\n⚖️  Pesos de las aristas:")
    for v1, v2, weight in weighted_edges:
        print(f"   {v1} → {v2}: peso {weight}")
    
    print("\n🔍 Simulación simplificada de Dijkstra desde 'a':")
    print("   (Nota: Esta es una demostración conceptual)")
    
    # Resultados conocidos del algoritmo de Dijkstra
    dijkstra_results = {
        'a': (0, ['a']),
        'b': (3, ['a', 'c', 'b']),
        'c': (2, ['a', 'c']),
        'd': (8, ['a', 'c', 'b', 'd']),
        'e': (10, ['a', 'c', 'b', 'd', 'e'])
    }
    
    print(f"\n📋 Resultados de Dijkstra:")
    for vertex, (distance, path) in sorted(dijkstra_results.items()):
        path_str = ' → '.join(path)
        print(f"   Vértice {vertex}: distancia {distance}, camino: {path_str}")

def main():
    """Función principal"""
    print("🎯 VISUALIZACIONES DE ALGORITMOS DE GRAFOS")
    print("📝 Versión en texto (sin dependencias gráficas)")
    
    try:
        # Ejecutar todas las visualizaciones
        bfs_text_visualization()
        unweighted_shortest_path_text_visualization()
        dijkstra_text_visualization()
        
        print_separator("RESUMEN COMPLETADO")
        print("✅ Todas las visualizaciones en texto completadas")
        print("📁 Archivos creados en la carpeta 'creacion_grafos':")
        print("   - bfs_visualization.py (requiere matplotlib)")
        print("   - unweighted_shortest_path_visualization.py (requiere matplotlib)")
        print("   - dijkstra_visualization.py (requiere matplotlib)")
        print("   - simple_graph_display.py (este archivo, solo texto)")
        print("\n💡 Para visualizaciones gráficas, instale: pip install matplotlib networkx")
        
    except Exception as e:
        print(f"❌ Error durante la ejecución: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()