"""
Evolution Optimizer

Stage53.3
Adjust AI factor weights from reward
"""


class EvolutionOptimizer:


    def optimize(
        self,
        weights,
        reward
    ):

        new_weights = weights.copy()


        avg = reward.get(
            "average_reward",
            0
        )


        if avg > 0:

            new_weights["momentum"] += 0.05

            new_weights["trend"] += 0.03

            new_weights["risk"] -= 0.02


        elif avg < 0:

            new_weights["risk"] += 0.05

            new_weights["momentum"] -= 0.03


        return self.normalize(
            new_weights
        )


    def normalize(
        self,
        weights
    ):

        total = sum(
            weights.values()
        )


        return {
            k:round(v/total,4)
            for k,v in weights.items()
        }