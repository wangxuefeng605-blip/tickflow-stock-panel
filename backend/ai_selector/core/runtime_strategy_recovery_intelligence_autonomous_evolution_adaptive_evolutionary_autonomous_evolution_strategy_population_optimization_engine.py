class RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryAutonomousEvolutionStrategyPopulationOptimizationEngine:
    """
    Optimizes strategy population.
    """

    def __init__(self):

        self.population = {}

        self.history = []



    def add_strategy(
        self,
        name,
        fitness
    ):

        self.population[name] = {

            "fitness": fitness,

            "active": True

        }


        result = {

            "strategy": name,

            "added": True

        }


        self.history.append(
            {
                "action": "add",
                "result": result
            }
        )


        return result



    def evaluate_population(self):

        if not self.population:

            return None


        total = sum(
            item["fitness"]
            for item in self.population.values()
        )


        average = round(
            total /
            len(self.population),
            3
        )


        result = {

            "size":
                len(self.population),

            "average_fitness":
                average

        }


        self.history.append(
            {
                "action": "evaluate",
                "result": result
            }
        )


        return result



    def remove_low_quality(
        self,
        threshold=0.3
    ):

        removed = []


        for name in list(
            self.population.keys()
        ):

            if (
                self.population[name]["fitness"]
                <
                threshold
            ):

                removed.append(
                    name
                )

                del self.population[name]


        result = {

            "removed": removed

        }


        self.history.append(
            {
                "action": "remove",
                "result": result
            }
        )


        return result



    def best_strategy(self):

        if not self.population:

            return None


        return max(
            self.population,
            key=lambda x:
            self.population[x]["fitness"]
        )



    def get_population(self):

        return self.population



    def get_history(self):

        return self.history