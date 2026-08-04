class RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionPopulationManager:
    """
    Manages autonomous evolution strategy population.
    """

    def __init__(self, max_size=5):

        self.population = []
        self.history = []
        self.max_size = max_size


    def add_strategy(self, strategy):

        self.population.append(
            strategy
        )


        self.history.append(
            {
                "action": "add",
                "strategy": strategy
            }
        )


    def evolve(self):

        self.population.sort(
            key=lambda x: x.get(
                "fitness",
                0
            ),
            reverse=True
        )


        if len(self.population) > self.max_size:

            removed = self.population[
                self.max_size:
            ]

            self.population = self.population[
                :self.max_size
            ]

        else:

            removed = []


        result = {

            "population": self.population,

            "removed": removed

        }


        self.history.append(
            {
                "action": "evolve",
                "result": result
            }
        )


        return result



    def get_elite(self):

        if not self.population:

            return None


        return max(
            self.population,
            key=lambda x: x.get(
                "fitness",
                0
            )
        )



    def get_population(self):

        return self.population



    def get_history(self):

        return self.history