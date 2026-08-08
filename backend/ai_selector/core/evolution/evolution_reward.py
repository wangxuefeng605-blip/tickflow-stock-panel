"""
Evolution Reward Aggregator

Stage53.2
Aggregate multiple feedback rewards
"""


from core.evolution.evolution_feedback import (
    EvolutionFeedback
)


class EvolutionReward:

    def __init__(self):

        self.feedback = EvolutionFeedback()


    def calculate(self, performances):

        if not performances:

            return {
                "average_reward": 0,
                "success_rate": 0,
                "samples": 0
            }


        rewards = []

        success = 0


        for item in performances:

            result = self.feedback.evaluate(
                item
            )

            rewards.append(
                result["reward"]
            )

            if result["success"]:
                success += 1


        total = len(rewards)


        return {

            "average_reward":
                sum(rewards) / total,

            "success_rate":
                success / total,

            "samples":
                total
        }