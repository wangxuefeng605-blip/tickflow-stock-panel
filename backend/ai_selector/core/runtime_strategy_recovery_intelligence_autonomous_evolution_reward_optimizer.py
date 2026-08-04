class RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionRewardOptimizer:
    """
    Optimizes evolution rewards.
    """

    def __init__(self):

        self.history = []


    def optimize(self, feedback):

        reward = feedback.get(
            "reward",
            0
        )

        success = feedback.get(
            "success",
            False
        )


        if success:

            optimized_reward = round(
                reward + 0.1,
                2
            )

        else:

            optimized_reward = round(
                reward - 0.1,
                2
            )


        result = {

            "strategy": feedback.get(
                "strategy"
            ),

            "original_reward": reward,

            "optimized_reward": optimized_reward

        }


        self.history.append(
            result
        )


        return result



    def get_history(self):

        return self.history