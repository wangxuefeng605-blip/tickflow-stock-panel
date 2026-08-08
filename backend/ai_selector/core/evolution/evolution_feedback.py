"""
Evolution Feedback

Stage53 Autonomous Feedback Loop
"""

from datetime import datetime


class EvolutionFeedback:

    def __init__(self):
        self.created_at = datetime.now()

    def evaluate(self, performance):
        """
        Evaluate recommendation performance.

        performance:
        {
            "return": 0.12
        }

        return:
        {
            "reward": 1,
            "success": True
        }
        """

        rate = performance.get(
            "return",
            0
        )

        if rate >= 0.1:
            reward = 1

        elif rate >= 0:
            reward = 0.5

        else:
            reward = -1


        return {
            "reward": reward,
            "success": reward > 0,
            "return": rate
        }