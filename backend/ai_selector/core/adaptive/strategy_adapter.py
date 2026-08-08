"""
Strategy Adapter

Stage36 Adaptive Intelligence
"""


class StrategyAdapter:


    def __init__(
        self,
        state
    ):

        self.state = state



    def apply(
        self,
        strategy
    ):


        version = self.state.strategy_version


        return {

            "strategy":
                strategy,

            "version":
                version,

            "adaptive":
                True
        }