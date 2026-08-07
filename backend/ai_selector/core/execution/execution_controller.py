"""
Execution Controller

Stage31 Autonomous Execution Intelligence
"""

from .execution_guard import ExecutionGuard
from .execution_simulator import ExecutionSimulator
from .execution_feedback import ExecutionFeedback


class ExecutionController:


    def __init__(self):

        self.guard = ExecutionGuard()

        self.simulator = ExecutionSimulator()

        self.feedback = ExecutionFeedback()



    def run(
        self,
        plan
    ):

        guard_result = self.guard.check(
            plan
        )


        if not guard_result["allowed"]:

            return {
                "status": "REJECTED",
                "reason": guard_result["reason"]
            }



        execution = self.simulator.execute(
            plan
        )


        execution.update(
            {
                "exit_price":
                    plan.get(
                        "exit_price",
                        execution["price"]
                    )
            }
        )


        return self.feedback.collect(
            execution
        )