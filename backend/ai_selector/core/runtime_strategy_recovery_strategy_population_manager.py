class RuntimeStrategyRecoveryStrategyPopulationManager:
    """
    Manage recovery strategy population.
    """

    def __init__(self):

        self.population = {}
        self.history = []


    def register_strategy(
        self,
        strategy,
        score=0
    ):

        self.population[strategy] = {
            "score": score,
            "active": True
        }


    def evaluate(
        self,
        strategy_scores
    ):

        result = {}

        for strategy, score in strategy_scores.items():

            if strategy in self.population:

                self.population[strategy]["score"] = score


                result[strategy] = score


        self.history.append(result)

        return result


    def select_best(self):

        active = {
            k:v
            for k,v in self.population.items()
            if v["active"]
        }


        if not active:

            return None


        return max(
            active,
            key=lambda x:
            active[x]["score"]
        )


    def remove_strategy(
        self,
        strategy
    ):

        if strategy in self.population:

            self.population[strategy]["active"] = False


    def get_history(self):

        return self.history