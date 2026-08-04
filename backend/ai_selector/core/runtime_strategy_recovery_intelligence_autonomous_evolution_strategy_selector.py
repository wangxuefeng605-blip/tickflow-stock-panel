class RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionStrategySelector:
    """
    Selects best strategy from evolution candidates.
    """

    def __init__(self):

        self.history = []


    def select(self, strategies):

        if not strategies:

            return None


        selected = max(
            strategies,
            key=lambda x: x.get(
                "fitness",
                0
            )
        )


        result = {

            "strategy": selected.get(
                "strategy"
            ),

            "fitness": selected.get(
                "fitness"
            ),

            "status": "selected"

        }


        self.history.append(
            result
        )


        return result



    def rank(self, strategies):

        return sorted(
            strategies,
            key=lambda x: x.get(
                "fitness",
                0
            ),
            reverse=True
        )



    def get_history(self):

        return self.history