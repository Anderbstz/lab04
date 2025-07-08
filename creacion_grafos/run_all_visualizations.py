#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script principal para ejecutar todas las visualizaciones de algoritmos de grafos

Este script ejecuta las visualizaciones de:
1. BFS Traversal
2. Unweighted Shortest Path
3. Dijkstra Algorithm

Cada visualización genera un gráfico y guarda una imagen PNG.
"""

import sys
import os
import subprocess

def install_requirements():
    """Instalar las dependencias necesarias"""
    required_packages = ['matplotlib', 'networkx']
    
    for package in required_packages:
        try:
            __import__(package)
            print(f"✓ {package} ya está instalado")
        except ImportError:
            print(f"⚠ Instalando {package}...")
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])
            print(f"✓ {package} instalado correctamente")

def run_visualization(script_name, description):
    """Ejecutar un script de visualización específico"""
    print(f"\n{'='*60}")
    print(f"Ejecutando: {description}")
    print(f"{'='*60}")
    
    try:
        # Ejecutar el script
        result = subprocess.run([sys.executable, script_name], 
                              capture_output=True, text=True, cwd=os.path.dirname(__file__))
        
        if result.returncode == 0:
            print(f"✓ {description} ejecutado correctamente")
            if result.stdout:
                print("Salida:")
                print(result.stdout)
        else:
            print(f"✗ Error al ejecutar {description}")
            if result.stderr:
                print("Error:")
                print(result.stderr)
                
    except Exception as e:
        print(f"✗ Excepción al ejecutar {description}: {e}")

def main():
    """Función principal"""
    print("🎯 Iniciando visualizaciones de algoritmos de grafos")
    print("📁 Directorio de trabajo:", os.path.dirname(__file__))
    
    # Instalar dependencias
    print("\n📦 Verificando dependencias...")
    install_requirements()
    
    # Lista de visualizaciones a ejecutar
    visualizations = [
        ('bfs_visualization.py', 'BFS Traversal - Recorrido en Anchura'),
        ('unweighted_shortest_path_visualization.py', 'Camino Más Corto Sin Pesos'),
        ('dijkstra_visualization.py', 'Algoritmo de Dijkstra - Camino Más Corto Con Pesos')
    ]
    
    # Ejecutar cada visualización
    for script, description in visualizations:
        run_visualization(script, description)
    
    print(f"\n{'='*60}")
    print("🎉 Todas las visualizaciones completadas")
    print("📸 Las imágenes se han guardado en:")
    print("   - bfs_graph.png")
    print("   - unweighted_shortest_path_graph.png")
    print("   - dijkstra_graph.png")
    print(f"{'='*60}")

if __name__ == "__main__":
    main()