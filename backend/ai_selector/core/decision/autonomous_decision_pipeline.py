"""
Autonomous Decision Pipeline

Stage30 Autonomous Decision Intelligence
"""


from .autonomous_decision_controller import (
    AutonomousDecisionController
)

from .decision_feedback_loop import (
    DecisionFeedbackLoop
)


class AutonomousDecisionPipeline:


    def __init__(self):

        self.controller = (
            AutonomousDecisionController()
        )

        self.feedback = (
            DecisionFeedbackLoop()
        )


    def run(
        self,
        data
    ):

        decision = (
            self.controller.decide(
                data
            )
        )


        self.feedback.record(
            {
                "action": decision["action"]
            }
        )


        return {
            "decision":
                decision["action"],

            "level":
                decision["level"]
        }