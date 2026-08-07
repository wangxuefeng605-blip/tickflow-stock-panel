"""
Autonomous Optimization Controller

Stage27 Autonomous Optimization Intelligence
"""


class AutonomousOptimizationController:


    def __init__(
        self,
        feedback_loop,
        healer=None
    ):

        self.feedback_loop = feedback_loop
        self.healer = healer



    def run(
        self,
        metrics,
        feedback
    ):

        result = (
            self.feedback_loop
            .process(
                metrics,
                feedback
            )
        )


        if self.healer:

            result["healing"] = (
                self.healer
                .execute()
            )


        return result