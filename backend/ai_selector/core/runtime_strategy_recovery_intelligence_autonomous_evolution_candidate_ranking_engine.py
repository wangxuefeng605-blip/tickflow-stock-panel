class RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionCandidateRankingEngine:
    """
    Ranks candidate strategies for autonomous evolution.
    """

    def __init__(self):

        self.history = []


    def rank(self, candidates):

        ranked = sorted(
            candidates,
            key=lambda x: self._score(x),
            reverse=True
        )


        result = {

            "ranking": ranked,

            "best": ranked[0] if ranked else None

        }


        self.history.append(
            result
        )


        return result



    def _score(self, candidate):

        fitness = candidate.get(
            "fitness",
            0
        )

        confidence = candidate.get(
            "confidence",
            0
        )

        risk = candidate.get(
            "risk",
            0
        )


        return round(
            fitness * 0.6
            +
            confidence * 0.3
            -
            risk * 0.1,
            4
        )



    def get_history(self):

        return self.history