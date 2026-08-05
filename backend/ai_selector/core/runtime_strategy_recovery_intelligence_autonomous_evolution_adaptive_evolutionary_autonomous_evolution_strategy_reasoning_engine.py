class RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryAutonomousEvolutionStrategyReasoningEngine:
    """
    Performs reasoning over strategy knowledge.
    """

    def __init__(self):

        self.knowledge = {}

        self.reasoning_history = []



    def register_fact(
        self,
        subject,
        relation,
        object_value
    ):

        if subject not in self.knowledge:

            self.knowledge[subject] = []


        fact = {

            "relation": relation,

            "object": object_value

        }


        self.knowledge[subject].append(
            fact
        )


        result = {

            "stored": True,

            "fact": {

                "subject": subject,

                "relation": relation,

                "object": object_value

            }

        }


        self.reasoning_history.append(
            {
                "action": "fact",
                "result": result
            }
        )


        return result



    def reason(
        self,
        subject,
        relation
    ):

        facts = self.knowledge.get(
            subject,
            []
        )


        conclusions = []


        for fact in facts:

            if fact["relation"] == relation:

                conclusions.append(
                    fact["object"]
                )


        result = {

            "subject": subject,

            "relation": relation,

            "conclusions": conclusions

        }


        self.reasoning_history.append(
            {
                "action": "reason",
                "result": result
            }
        )


        return result



    def explain(
        self,
        strategy
    ):

        facts = self.knowledge.get(
            strategy,
            []
        )


        explanation = []


        for fact in facts:

            explanation.append(
                f"{strategy} {fact['relation']} {fact['object']}"
            )


        result = {

            "strategy": strategy,

            "explanation": explanation

        }


        self.reasoning_history.append(
            {
                "action": "explain",
                "result": result
            }
        )


        return result



    def get_history(self):

        return self.reasoning_history