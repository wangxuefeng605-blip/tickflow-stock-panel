class RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveFitnessOptimizer:
    """
    Optimizes strategy fitness from calibrated rewards.
    """

    def __init__(self):

        self.history = []


    def optimize(self, reward_data):

        reward = reward_data.get(
            "reward",
            0
        )

        previous = reward_data.get(
            "previous_fitness",
            0
        )


        fitness = round(
            previous * 0.3
            +
            reward * 0.7,
            2
        )


        result = {

            "strategy": reward_data.get(
                "strategy"
            ),

            "fitness": fitness,

            "optimized": True

        }


        self.history.append(
            result
        )


        return result



    def compare(self, candidates):

        if not candidates:

            return None


        return max(
            candidates,
            key=lambda x: x.get(
                "fitness",
                0
            )
        )



    def get_history(self):

        return self.history