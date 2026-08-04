class RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvaluationEngine:
    """
    Evaluates evolution improvement quality.
    """

    def __init__(self):

        self.history = []


    def evaluate(self, previous, current):

        previous_fitness = previous.get(
            "fitness",
            0
        )

        current_fitness = current.get(
            "fitness",
            0
        )


        improvement = round(
            current_fitness - previous_fitness,
            2
        )


        if improvement > 0:

            decision = "accept"

        elif improvement == 0:

            decision = "continue"

        else:

            decision = "rollback"


        result = {

            "previous_fitness": previous_fitness,

            "current_fitness": current_fitness,

            "improvement": improvement,

            "decision": decision

        }


        self.history.append(
            result
        )


        return result



    def get_history(self):

        return self.history