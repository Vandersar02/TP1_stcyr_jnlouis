import xml.etree.ElementTree as ET

from graphe_implement import Graph


class GraphUploader:
    def __init__(self):
        self.graph = Graph()

    def parse_graph_from_xml(self, xml_file):
        tree = ET.parse(xml_file)
        root = tree.getroot()

        for edge in root.findall('.//edge'):
            source = edge.find('source').text
            target = edge.find('target').text
            weight = float(edge.find('weight').text)

            if source not in self.graph.nodes:
                self.graph.add_node(source)
            if target not in self.graph.nodes:
                self.graph.add_node(target)

            self.graph.add_edge(source, target, weight)

    def get_graph(self):
        return self.graph




