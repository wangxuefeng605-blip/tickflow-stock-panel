class RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryAutonomousEvolutionKnowledgeRetrievalEngine:
    """
    Retrieves useful knowledge from historical experiences.
    """

    def __init__(self):

        self.knowledge = []

        self.history = []



    def add_knowledge(
        self,
        knowledge
    ):

        self.knowledge.append(
            knowledge
        )


        result = {

            "stored": True,

            "count": len(self.knowledge)

        }


        self.history.append(
            {
                "action": "add",
                "result": result
            }
        )


        return result



    def retrieve(
        self,
        market_state,
        min_quality=0
    ):

        results = []


        for item in self.knowledge:

            if (
                item.get("market_state")
                ==
                market_state
                and
                item.get("quality", 0)
                >=
                min_quality
            ):

                results.append(
                    item
                )


        result = {

            "market_state": market_state,

            "matches": results,

            "count": len(results)

        }


        self.history.append(
            {
                "action": "retrieve",
                "result": result
            }
        )


        return result



    def best_knowledge(
        self
    ):

        if not self.knowledge:

            return None


        return max(
            self.knowledge,
            key=lambda x:
            x.get(
                "quality",
                0
            )
        )



    def get_history(self):

        return self.history