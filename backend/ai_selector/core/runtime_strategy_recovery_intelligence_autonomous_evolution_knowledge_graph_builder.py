class RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionKnowledgeGraphBuilder:
    """
    Builds strategy evolution knowledge graph.
    """

    def __init__(self):

        self.nodes = []
        self.edges = []
        self.history = []


    def add_strategy(self, strategy):

        node = {

            "type": "strategy",

            "name": strategy

        }


        self.nodes.append(node)

        self.history.append(node)

        return node



    def add_relation(self, source, target, relation):

        edge = {

            "source": source,

            "target": target,

            "relation": relation

        }


        self.edges.append(edge)

        return edge



    def find_strategy(self, name):

        for node in self.nodes:

            if node["name"] == name:

                return node


        return None



    def get_graph(self):

        return {

            "nodes": self.nodes,

            "edges": self.edges

        }



    def get_history(self):

        return self.history