class RuntimeStrategyRecoveryIntelligentPolicySelector:
    """
    Intelligent recovery policy selector.
    """

    def __init__(self):
        self.history = []


    def select(self, policies):

        best_policy = None
        best_score = -1


        for name, data in policies.items():

            weight = data.get(
                "weight",
                0
            )

            performance = data.get(
                "score",
                0
            )

            final_score = (
                weight * performance
            )


            if final_score > best_score:

                best_score = final_score
                best_policy = name


        result = {
            "selected_policy": best_policy,
            "score": best_score
        }


        self.history.append(result)

        return result


    def get_history(self):

        return self.history