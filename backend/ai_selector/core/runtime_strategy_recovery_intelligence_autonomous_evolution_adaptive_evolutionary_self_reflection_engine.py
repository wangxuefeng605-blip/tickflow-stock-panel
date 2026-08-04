class RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionarySelfReflectionEngine:
    """
    Reflects on previous autonomous evolution decisions.
    """

    def __init__(self):

        self.reflections = []

        self.history = []



    def reflect(
        self,
        decision,
        outcome
    ):

        if outcome >= 0.8:

            evaluation = "successful"

            suggestion = "reinforce_strategy"


        elif outcome <= 0.3:

            evaluation = "failed"

            suggestion = "change_strategy"


        else:

            evaluation = "neutral"

            suggestion = "continue_observation"



        result = {

            "decision": decision,

            "outcome": outcome,

            "evaluation": evaluation,

            "suggestion": suggestion

        }


        self.reflections.append(
            result
        )


        self.history.append(
            {
                "action": "reflect",
                "result": result
            }
        )


        return result



    def get_reflections(self):

        return self.reflections



    def get_history(self):

        return self.history