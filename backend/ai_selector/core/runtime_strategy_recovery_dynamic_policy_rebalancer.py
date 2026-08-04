class RuntimeStrategyRecoveryDynamicPolicyRebalancer:
    """
    Dynamically rebalance recovery strategy weights.
    """

    def __init__(self):
        self.history = []


    def rebalance(self, strategy_weights):

        total = sum(
            strategy_weights.values()
        )

        if total == 0:
            result = {
                key: 0
                for key in strategy_weights
            }
        else:
            result = {
                key: value / total
                for key, value in strategy_weights.items()
            }


        self.history.append(
            result
        )

        return result


    def get_history(self):

        return self.history