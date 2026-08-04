class RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryPredictivePlanningEngine:
    """
    Predicts future evolution directions.
    """

    def __init__(self):

        self.plans = []

        self.history = []



    def create_plan(
        self,
        knowledge
    ):

        fitness = knowledge.get(
            "fitness",
            0
        )


        if fitness >= 0.8:

            direction = "optimize_existing"


        elif fitness <= 0.3:

            direction = "explore_new"


        else:

            direction = "balanced_evolution"



        plan = {

            "current_fitness": fitness,

            "direction": direction,

            "next_action": direction

        }


        self.plans.append(
            plan
        )


        self.history.append(
            {
                "action": "plan",
                "plan": plan
            }
        )


        return plan



    def get_latest_plan(self):

        if not self.plans:

            return None


        return self.plans[-1]



    def get_history(self):

        return self.history