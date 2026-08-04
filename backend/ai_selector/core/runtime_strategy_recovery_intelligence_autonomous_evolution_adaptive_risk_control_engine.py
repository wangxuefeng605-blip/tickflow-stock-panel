class RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveRiskControlEngine:
    """
    Controls risks during autonomous evolution.
    """

    def __init__(self):

        self.risk_level = 0
        self.history = []


    def assess(self, state):

        fitness_drop = state.get(
            "fitness_drop",
            0
        )

        mutation_rate = state.get(
            "mutation_rate",
            0
        )


        risk = (
            fitness_drop
            +
            mutation_rate
        )


        if risk >= 0.8:

            level = "high"

            action = "safe_mode"


        elif risk >= 0.4:

            level = "medium"

            action = "reduce_exploration"


        else:

            level = "low"

            action = "normal"



        result = {

            "risk_score": risk,

            "level": level,

            "action": action

        }


        self.risk_level = risk


        self.history.append(
            result
        )


        return result



    def get_risk_level(self):

        return self.risk_level



    def get_history(self):

        return self.history