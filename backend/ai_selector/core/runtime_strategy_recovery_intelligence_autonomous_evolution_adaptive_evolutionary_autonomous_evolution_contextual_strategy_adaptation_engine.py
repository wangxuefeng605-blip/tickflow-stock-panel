class RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryAutonomousEvolutionContextualStrategyAdaptationEngine:
    """
    Adapts strategy according to market context.
    """

    def __init__(self):

        self.strategies = {}

        self.history = []



    def register_strategy(
        self,
        name,
        parameters
    ):

        self.strategies[name] = parameters


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



    def select_strategy(
        self,
        market_state
    ):

        if market_state in self.strategies:

            selected = self.strategies[market_state]


        elif "DEFAULT" in self.strategies:

            selected = self.strategies["DEFAULT"]


        else:

            selected = None


        result = {

            "market_state": market_state,

            "strategy": selected

        }


        self.history.append(
            {
                "action": "select",
                "result": result
            }
        )


        return result



    def adapt_parameters(
        self,
        strategy,
        performance
    ):

        updated = strategy.copy()


        if performance > 0:

            updated["aggressiveness"] = round(
                min(
                    updated.get(
                        "aggressiveness",
                        0.5
                    )
                    + 0.1,
                    1
                ),
                3
            )


        else:

            updated["aggressiveness"] = round(
                max(
                    updated.get(
                        "aggressiveness",
                        0.5
                    )
                    - 0.1,
                    0
                ),
                3
            )


        result = {

            "strategy": updated

        }


        self.history.append(
            {
                "action": "adapt",
                "result": result
            }
        )


        return result



    def get_history(self):

        return self.history