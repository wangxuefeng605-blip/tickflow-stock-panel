"""
Decision Feedback Loop

Stage30 Autonomous Decision Intelligence
"""


class DecisionFeedbackLoop:


    def __init__(self):

        self.history = []


    def record(
        self,
        feedback
    ):

        self.history.append(
            feedback
        )


        return {
            "stored": True,
            "reward": feedback.get(
                "reward",
                0
            )
        }


    def recent(self):

        return self.history