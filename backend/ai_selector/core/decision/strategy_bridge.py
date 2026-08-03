from core.strategy import StrategySelector



class DecisionStrategyBridge:


    def __init__(
        self,
        selector=None
    ):

        self.selector = (
            selector
            or StrategySelector()
        )


    def apply(
        self,
        decision
    ):


        strategy = self.selector.select(
            decision
        )


        decision["strategy"] = strategy


        return decision