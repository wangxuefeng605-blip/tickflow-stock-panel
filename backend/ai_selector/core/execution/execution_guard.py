"""
Execution Guard

Stage31 Autonomous Execution Intelligence
"""


class ExecutionGuard:


    def check(
        self,
        execution
    ):

        if not execution.get("action"):

            return {
                "allowed": False,
                "reason": "MISSING_ACTION"
            }


        if not execution.get("symbol"):

            return {
                "allowed": False,
                "reason": "MISSING_SYMBOL"
            }


        confidence = execution.get(
            "confidence",
            0
        )

        if confidence < 0.7:

            return {
                "allowed": False,
                "reason": "LOW_CONFIDENCE"
            }


        risk = execution.get(
            "risk",
            1
        )

        if risk > 0.3:

            return {
                "allowed": False,
                "reason": "RISK_LIMIT"
            }


        return {
            "allowed": True,
            "reason": "PASS"
        }