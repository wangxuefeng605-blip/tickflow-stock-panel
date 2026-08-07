"""
Self Healing Controller

Stage26 Self-Healing Intelligence
"""

from core.healing.failure_analyzer import (
    FailureAnalyzer
)

from core.healing.recovery_strategy import (
    AdaptiveRecoveryStrategy
)



class SelfHealingController:


    def __init__(self):

        self.analyzer = (
            FailureAnalyzer()
        )

        self.strategy = (
            AdaptiveRecoveryStrategy()
        )



    def heal(
        self,
        errors,
        executor=None
    ):

        analysis = (
            self.analyzer
            .analyze(errors)
        )


        results = []


        for failure in analysis:


            decision = (
                self.strategy
                .decide(failure)
            )


            success = False


            if executor:

                try:

                    executor(
                        decision
                    )

                    success = True


                except Exception:

                    success = False


            self.strategy.record_result(
                failure["type"],
                success
            )


            results.append(
                {
                    "failure":
                        failure,

                    "decision":
                        decision,

                    "success":
                        success
                }
            )


        return results