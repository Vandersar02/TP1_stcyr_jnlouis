import xml.etree.ElementTree as ET
from graphe_implement import Graph
from Dijkstra import Dijkstra

# Charger le fichier XML
tree = ET.parse('graph.xml')
root = tree.getroot()

# Créer un graphe vide
g = Graph()

# Parcourir les éléments du fichier XML pour ajouter les nœuds et les arêtes au graphe
for vertex in root.findall('./Vertices/Vertex'):
    vertex_id = vertex.attrib['vertexId']
    g.add_node(vertex_id)

for edge in root.findall('./Edges/Edge'):
    head = edge.attrib['head']
    tail = edge.attrib['tail']
    weight = float(edge.attrib['weight'])
    g.add_edge(head, tail, weight)

# Utiliser l'algorithme de Dijkstra sur le graphe
dijkstra_algorithm = Dijkstra(g)
start_node = '9'

# Calcul du chemin le plus court pour visiter tous les autres sommets
shortest_paths = {}
for node in g.nodes:
    if node != start_node:
        shortest_path, total_distance = dijkstra_algorithm.dijkstra(start_node, node)
        shortest_paths[node] = (shortest_path, total_distance)

# Affichage des chemins les plus courts et de leurs coûts
for node, (shortest_path, total_distance) in shortest_paths.items():
    print(f"Le chemin le plus court de {start_node} à {node} est : {shortest_path}")
    print(f"Le coût minimum pour visiter {node} est : {total_distance}")
    print("\n")
