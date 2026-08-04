class RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveExplorationController:
    """
    Controls exploration and exploitation balance.
    """

    def __init__(self):

        self.exploration_rate = 0.5
        self.history = []


    def adjust(self, fitness):

        if fitness >= 0.8:

            self.exploration_rate = 0.2

            mode = "exploit"


        elif fitness <= 0.3:

            self.exploration_rate = 0.8

            mode = "explore"


        else:

            self.exploration_rate = 0.5

            mode = "balanced"


        result = {

            "mode": mode,

            "exploration_rate": self.exploration_rate

        }


        self.history.append(
            result
        )


        return result



    def get_rate(self):

        return self.exploration_rate



    def get_history(self):

        return self.history