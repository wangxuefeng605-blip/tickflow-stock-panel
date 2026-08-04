class RuntimeStrategyRecoveryLearningWeightOptimizer:
    """
    Optimize runtime strategy weights based on recovery learning feedback.
    """

    def __init__(self):
        self.strategy_weights = {}
        self.history = []


    def optimize(self, learning_signal):

        policy = learning_signal.get(
            "policy"
        )

        weight = learning_signal.get(
            "learning_weight",
            1.0
        )

        old_weight = self.strategy_weights.get(
            policy,
            1.0
        )

        new_weight = old_weight * weight


        self.strategy_weights[
            policy
        ] = new_weight


        result = {
            "policy": policy,
            "old_weight": old_weight,
            "new_weight": new_weight,
            "updated": True
        }


        self.history.append(
            result
        )


        return result


    def get_weight(self, policy):

        return self.strategy_weights.get(
            policy,
            1.0
        )


    def get_history(self):

        return self.history