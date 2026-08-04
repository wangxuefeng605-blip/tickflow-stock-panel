class RuntimeStrategyRecoveryLearningOptimizer:
    """
    Learn recovery strategy performance
    and optimize future recovery preference.
    """

    def __init__(self):
        self.weights = {
            "fallback": 1.0,
            "rollback": 1.0,
            "parameter_restore": 1.0
        }

        self.history = []


    def optimize(self, outcome):

        action = outcome.get(
            "action"
        )

        success = outcome.get(
            "success"
        )


        if action not in self.weights:
            return None


        if success:

            self.weights[action] += 0.1

        else:

            self.weights[action] -= 0.1


        result = {
            "action": action,
            "success": success,
            "weight": self.weights[action]
        }


        self.history.append(
            result
        )


        return result



    def get_weights(self):

        return self.weights



    def optimization_history(self):

        return self.history