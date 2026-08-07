"""
Strategy Evaluator

Stage33 Strategy Intelligence Layer
"""


class StrategyEvaluator:


    def evaluate(
        self,
        performance
    ):

        ret = performance.get(
            "return",
            0
        )

        risk = performance.get(
            "risk",
            1
        )

        win_rate = performance.get(
            "win_rate",
            0
        )


        score = (
            ret * 0.5
            +
            win_rate * 0.5
            -
            risk * 0.2
        )


        level = "BAD"


        if score >= 0.35:

            level = "GOOD"

        elif score >= 0.15:

            level = "NORMAL"


        return {

            "score": round(score, 4),

            "level": level
        }