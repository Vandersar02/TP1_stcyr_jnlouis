import heapq

class Dijkstra:
    def __init__(self, graph):
        self.graph = graph
        self.nodes = graph.nodes
        self.edges = graph.edges

    def add_node(self, value):
        self.nodes.add(value)
        self.edges[value] = {}

    def add_edge(self, from_node, to_node, weight):
        self.edges[from_node][to_node] = weight
        self.edges[to_node][from_node] = weight  # Si le graphe est non orienté
        
    # @staticmethod
    def dijkstra(self, start, end):
        distances = {node: float('infinity') for node in self.nodes}
        distances[start] = 0
        previous_nodes = {node: None for node in self.nodes}

        priority_queue = [(0, start)]

        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)

            if current_distance > distances[current_node]:
                continue

            for neighbor, weight in self.edges[current_node].items():
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous_nodes[neighbor] = current_node
                    heapq.heappush(priority_queue, (distance, neighbor))
        path = []
        current_node = end
        while previous_nodes[current_node] is not None:
            path.insert(0, current_node)
            current_node = previous_nodes[current_node]
        path.insert(0, start)

        return path, distances[end]