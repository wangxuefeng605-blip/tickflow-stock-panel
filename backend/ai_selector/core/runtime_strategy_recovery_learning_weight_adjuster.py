class RuntimeStrategyRecoveryLearningWeightAdjuster:
    """
    Adjust recovery strategy weights based on learning signals.
    """

    def __init__(self):
        self.weights = {
            "restore": 1.0,
            "rollback": 1.0,
            "fallback": 1.0,
        }

        self.history = []


    def adjust(self, signal):

        policy = signal.get(
            "policy"
        )

        score = signal.get(
            "learning_score",
            0.0
        )


        if policy not in self.weights:
            self.weights[policy] = 1.0


        if score > 0:

            self.weights[policy] += 0.1

        elif score < 0:

            self.weights[policy] -= 0.1


        record = {
            "policy": policy,
            "weight": round(
                self.weights[policy],
                2
            )
        }


        self.history.append(
            record
        )


        return record


    def get_weights(self):

        return self.weights


    def get_history(self):

        return self.history