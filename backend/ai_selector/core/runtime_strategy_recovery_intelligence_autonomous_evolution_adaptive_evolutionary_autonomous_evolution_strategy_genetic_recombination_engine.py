class RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryAutonomousEvolutionStrategyGeneticRecombinationEngine:
    """
    Combines strategy genomes to create hybrid strategies.
    """

    def __init__(self):

        self.genomes = {}

        self.children = []

        self.history = []



    def add_genome(
        self,
        name,
        parameters,
        fitness
    ):

        genome = {

            "name": name,

            "parameters": parameters,

            "fitness": fitness

        }


        self.genomes[name] = genome


        result = {

            "stored": True,

            "name": name

        }


        self.history.append(
            {
                "action": "add",
                "result": result
            }
        )


        return result



    def recombine(
        self,
        parent_a,
        parent_b
    ):

        if (
            parent_a not in self.genomes
            or
            parent_b not in self.genomes
        ):

            return None


        a = self.genomes[parent_a]

        b = self.genomes[parent_b]


        child_parameters = {}


        keys = set(
            a["parameters"].keys()
        ).union(
            b["parameters"].keys()
        )


        for key in keys:

            if key in a["parameters"]:

                child_parameters[key] = a["parameters"][key]

            else:

                child_parameters[key] = b["parameters"][key]


        child = {

            "name":
                parent_a
                +
                "_x_"
                +
                parent_b,

            "parameters":
                child_parameters,

            "fitness":
                (
                    a["fitness"]
                    +
                    b["fitness"]
                )
                /
                2

        }


        self.children.append(
            child
        )


        result = {

            "child": child

        }


        self.history.append(
            {
                "action": "recombine",
                "result": result
            }
        )


        return result



    def best_child(self):

        if not self.children:

            return None


        return max(
            self.children,
            key=lambda x:
            x["fitness"]
        )



    def get_history(self):

        return self.history