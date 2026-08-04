class RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryAutonomousDiscoveryEngine:
    """
    Discovers new evolution strategies automatically.
    """

    def __init__(self):

        self.knowledge = []

        self.discoveries = []

        self.history = []



    def add_knowledge(
        self,
        item
    ):

        self.knowledge.append(
            item
        )


        self.history.append(
            {
                "action": "knowledge",
                "item": item
            }
        )


        return item



    def discover(
        self
    ):

        if len(self.knowledge) < 2:

            return None


        candidate = {

            "strategy":

                str(self.knowledge[0])
                +
                "_"
                +
                str(self.knowledge[1]),

            "novelty": True

        }


        self.discoveries.append(
            candidate
        )


        self.history.append(
            {
                "action": "discover",
                "candidate": candidate
            }
        )


        return candidate



    def score_discovery(
        self,
        candidate,
        score
    ):

        result = {

            "candidate": candidate,

            "score": score

        }


        self.history.append(
            {
                "action": "score",
                "result": result
            }
        )


        return result



    def get_history(self):

        return self.history