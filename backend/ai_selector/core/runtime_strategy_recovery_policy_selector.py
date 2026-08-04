class RuntimeStrategyRecoveryPolicySelector:
    """
    Select best recovery policy based on learned weights.
    """

    def __init__(self):
        self.history = []


    def select(self, weights):

        if not weights:
            return None


        policy = max(
            weights,
            key=weights.get
        )


        result = {
            "selected_policy": policy,
            "confidence": weights[policy]
        }


        self.history.append(
            result
        )


        return result



    def selection_history(self):

        return self.history