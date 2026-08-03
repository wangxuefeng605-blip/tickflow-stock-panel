from .execution_plan import ExecutionPlan


class ExecutionEngine:


    def __init__(self):
        pass



    def create_plan(
        self,
        decision
    ):

        return ExecutionPlan(

            code=decision["code"],

            action=decision.get(
                "action",
                decision.get(
                    "side",
                    "HOLD"
                )
            ),

            confidence=decision.get(
                "confidence",
                0
            ),

            status="CREATED"

        )