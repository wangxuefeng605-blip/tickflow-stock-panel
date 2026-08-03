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

            side=decision.get(
                "action",
                "HOLD"
            ),

            status="CREATED"

        )