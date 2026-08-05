class RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryAutonomousEvolutionMultiStrategyCoordinationEngine:
    """
    Coordinates multiple trading strategies.
    """

    def __init__(self):

        self.strategies = {}

        self.performance = {}

        self.history = []



    def register_strategy(
        self,
        name,
        weight=0.5
    ):

        self.strategies[name] = {

            "weight": weight,

            "active": True

        }


        self.performance[name] = []


        result = {

            "strategy": name,

            "registered": True

        }


        self.history.append(
            {
                "action": "register",
                "result": result
            }
        )


        return result



    def update_performance(
        self,
        name,
        score
    ):

        if name not in self.performance:

            return None


        self.performance[name].append(
            score
        )


        result = {

            "strategy": name,

            "score": score

        }


        self.history.append(
            {
                "action": "performance",
                "result": result
            }
        )


        return result



    def select_best_strategy(self):

        ranking = {}


        for name, values in self.performance.items():

            if values:

                ranking[name] = sum(values) / len(values)


        if not ranking:

            return None


        best = max(
            ranking,
            key=ranking.get
        )


        result = {

            "strategy": best,

            "score": ranking[best]

        }


        self.history.append(
            {
                "action": "select",
                "result": result
            }
        )


        return result



    def get_active_strategies(self):

        return [

            name
            for name, item
            in self.strategies.items()
            if item["active"]

        ]



    def get_history(self):

        return self.history