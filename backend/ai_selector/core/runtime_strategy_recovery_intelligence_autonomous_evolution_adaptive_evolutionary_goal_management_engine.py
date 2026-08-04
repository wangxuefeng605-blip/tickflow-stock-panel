class RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryGoalManagementEngine:
    """
    Manages autonomous evolution objectives.
    """

    def __init__(self):

        self.objectives = {}

        self.history = []



    def register_objective(
        self,
        name,
        weight
    ):

        self.objectives[name] = weight


        self.history.append(
            {
                "action": "register",
                "objective": name,
                "weight": weight
            }
        )


        return {
            "objective": name,
            "weight": weight
        }



    def optimize_goal(
        self,
        performance,
        risk
    ):

        score = round(
            performance * 0.7
            -
            risk * 0.3,
            2
        )


        result = {

            "goal_score": score,

            "performance": performance,

            "risk": risk

        }


        self.history.append(
            {
                "action": "optimize",
                "result": result
            }
        )


        return result



    def get_objectives(self):

        return self.objectives



    def get_history(self):

        return self.history