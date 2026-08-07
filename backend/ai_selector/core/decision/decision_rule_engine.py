"""
Decision Rule Engine

Stage30 Autonomous Decision Intelligence
"""


class DecisionRuleEngine:


    def evaluate(
        self,
        context
    ):

        if (
            context.market == "BULL"
            and context.confidence >= 0.7
        ):

            return {
                "action": "SELECT",
                "confidence": context.confidence
            }


        if context.market == "BEAR":

            return {
                "action": "HOLD",
                "confidence": context.confidence
            }


        return {
            "action": "WAIT",
            "confidence": context.confidence
        }