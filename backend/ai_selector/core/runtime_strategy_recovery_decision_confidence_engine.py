class RuntimeStrategyRecoveryDecisionConfidenceEngine:
    """
    Calculate confidence of recovery policy decision.
    """

    def __init__(self):
        self.history = []


    def evaluate(self, policies):

        scores = {}

        for name, data in policies.items():

            scores[name] = data.get(
                "score",
                0
            )


        if not scores:

            result = {
                "selected_policy": None,
                "confidence": 0
            }

            self.history.append(result)

            return result


        ranked = sorted(
            scores.items(),
            key=lambda x: x[1],
            reverse=True
        )


        selected = ranked[0][0]

        top_score = ranked[0][1]


        if len(ranked) > 1:

            second_score = ranked[1][1]

        else:

            second_score = 0


        confidence = (
            top_score - second_score
        )


        result = {
            "selected_policy": selected,
            "confidence": confidence
        }


        self.history.append(result)

        return result


    def get_history(self):

        return self.history