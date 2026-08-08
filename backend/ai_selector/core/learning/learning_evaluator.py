"""
Learning Evaluator

Stage35 Autonomous Learning
"""


class LearningEvaluator:


    def evaluate(
        self,
        experience
    ):

        reward = experience.get(
            "reward",
            0
        )


        if reward > 0:

            level = "POSITIVE"

        elif reward < 0:

            level = "NEGATIVE"

        else:

            level = "NEUTRAL"


        return {
            "score": reward,
            "reward": reward,
            "level": level
        }