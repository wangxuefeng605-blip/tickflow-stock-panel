"""
Decision Score Engine

Stage30 Autonomous Decision Intelligence
"""


class DecisionScoreEngine:


    def score(
        self,
        data
    ):

        score = (
            data.get("market_score", 0)
            * 0.4
            +
            data.get("confidence", 0)
            * 0.4
            -
            data.get("risk", 0)
            * 0.2
        )


        level = "LOW"


        if score >= 0.6:
            level = "HIGH"

        elif score >= 0.3:
            level = "MEDIUM"


        return {
            "score": score,
            "level": level
        }