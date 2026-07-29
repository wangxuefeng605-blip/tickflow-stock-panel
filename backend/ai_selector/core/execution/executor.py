from .order_types import ExecutionOrder
from .execution_policy import allow_execution
from .risk_guard import risk_check


class Executor:


    def execute(
        self,
        decision
    ):


        if not allow_execution(decision):
            return None


        if not risk_check(decision):
            return None


        return ExecutionOrder(

            code=decision["code"],

            action=decision["decision"],

            quantity=100,

            confidence=decision.get(
                "confidence",
                0
            ),

            reason="AI execution approved"

        )