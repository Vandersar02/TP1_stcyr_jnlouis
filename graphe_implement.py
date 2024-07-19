class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = {}

    def add_node(self, value):
        self.nodes.add(value)
        self.edges[value] = {}

    def add_edge(self, from_node, to_node, weight):
        self.edges[from_node][to_node] = weight
        self.edges[to_node][from_node] = weight  

    def display(self):
        print("Nodes:")
        for node in self.nodes:
            print(node)

        print("\nEdges:")
        for from_node, to_nodes in self.edges.items():
            for to_node, weight in to_nodes.items():
                print(f"{from_node} --({weight})--> {to_node}")