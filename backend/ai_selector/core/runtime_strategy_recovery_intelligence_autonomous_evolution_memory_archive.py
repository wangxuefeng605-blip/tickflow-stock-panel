class RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionMemoryArchive:
    """
    Stores long-term autonomous evolution memories.
    """

    def __init__(self):

        self.generations = []
        self.lineage = []
        self.history = []


    def archive_generation(self, generation):

        self.generations.append(
            generation
        )


        self.history.append(
            {
                "action": "archive_generation",
                "generation": generation
            }
        )


        return generation



    def archive_strategy_lineage(
        self,
        parent,
        child
    ):

        record = {

            "parent": parent,

            "child": child

        }


        self.lineage.append(
            record
        )


        self.history.append(
            {
                "action": "archive_lineage",
                "record": record
            }
        )


        return record



    def get_best_generation(self):

        if not self.generations:

            return None


        return max(
            self.generations,
            key=lambda x: x.get(
                "fitness",
                0
            )
        )



    def get_generations(self):

        return self.generations



    def get_lineage(self):

        return self.lineage



    def get_history(self):

        return self.history