from .rules import (
    momentum_entry,
    trend_exit
)


class StrategyEngine:


    def evaluate(
        self,
        factors,
        context=None
    ):


        if momentum_entry(
            factors
        ):

            return {
                "action":"BUY",
                "confidence":0.8
            }


        if trend_exit(
            factors
        ):

            return {
                "action":"SELL",
                "confidence":0.7
            }


        return {
            "action":"HOLD",
            "confidence":0.5
        }