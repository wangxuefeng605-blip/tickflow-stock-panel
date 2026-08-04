class RuntimeStrategyRecoveryIntelligenceAutonomousStrategyGenomeManager:
    """
    Stores and manages strategy genomes.
    """

    def __init__(self):

        self.genomes = []
        self.history = []


    def register(self, strategy):

        genome = {

            "version": strategy.get(
                "version"
            ),

            "parent": strategy.get(
                "parent"
            ),

            "fitness": strategy.get(
                "fitness",
                0
            )

        }


        self.genomes.append(genome)

        self.history.append(genome)

        return genome



    def get_best_genome(self):

        if not self.genomes:

            return None


        return max(
            self.genomes,
            key=lambda x: x["fitness"]
        )



    def get_lineage(self):

        return self.genomes



    def get_history(self):

        return self.history