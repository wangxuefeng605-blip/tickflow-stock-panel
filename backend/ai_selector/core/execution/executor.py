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



        if hasattr(
            decision,
            "code"
        ):

            code = decision.code

            action = decision.action

            confidence = decision.confidence


        else:

            code = decision["code"]

            action = decision.get(
                "decision",
                decision.get(
                    "action"
                )
            )

            confidence = decision.get(
                "confidence",
                0
            )


        return ExecutionOrder(

            code=code,

            action=action,

            quantity=100,

            confidence=confidence,

            reason="AI execution approved"

        )