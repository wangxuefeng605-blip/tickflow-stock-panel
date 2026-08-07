"""
Runtime Decision Policy

Stage25 Autonomous Runtime Intelligence
"""


class RuntimeDecisionPolicy:
    """
    Runtime action policy controller
    """

    def __init__(
        self,
        max_retry=3
    ):
        self.max_retry = max_retry


    def apply(self, decision):

        action = decision.get(
            "action"
        )


        if action == "CONTINUE":

            return {
                "mode": "NORMAL",
                "retry": 0
            }


        if action.startswith(
            "RECOVER_"
        ):

            return {
                "mode": "RECOVERY",
                "retry": self.max_retry,
                "target": action.replace(
                    "RECOVER_",
                    ""
                ).lower()
            }


        if action == "SAFE_MODE":

            return {
                "mode": "SAFE",
                "retry": 0
            }


        return {
            "mode": "UNKNOWN",
            "retry": 0
        }