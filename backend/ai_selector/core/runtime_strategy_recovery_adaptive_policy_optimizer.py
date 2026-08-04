class RuntimeStrategyRecoveryAdaptivePolicyOptimizer:
    """
    Select best recovery policy based on learned weights.
    """

    def __init__(self):
        self.weights = {
            "restore": 1.0,
            "rollback": 1.0,
            "fallback": 1.0,
        }

        self.history = []


    def update_weights(self, weights):

        self.weights.update(
            weights
        )


    def optimize(self):

        policy = max(
            self.weights,
            key=self.weights.get
        )

        result = {
            "selected_policy": policy,
            "weight": self.weights[policy]
        }


        self.history.append(
            result
        )


        return result


    def get_history(self):

        return self.history