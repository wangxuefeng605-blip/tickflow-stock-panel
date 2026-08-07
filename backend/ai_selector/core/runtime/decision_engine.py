"""
Runtime Decision Engine

Stage25 Autonomous Runtime Intelligence
"""


class RuntimeDecisionEngine:
    """
    Decide runtime actions based on system state
    """

    def decide(self, health):

        errors = health.get(
            "errors",
            []
        )

        components = health.get(
            "components",
            {}
        )

        if len(errors) >= 3:
            return {
                "action": "SAFE_MODE",
                "priority": "CRITICAL"
            }


        for name, state in components.items():

            if state == "ERROR":
                return {
                    "action": f"RECOVER_{name.upper()}",
                    "priority": "HIGH"
                }


        return {
            "action": "CONTINUE",
            "priority": "NORMAL"
        }