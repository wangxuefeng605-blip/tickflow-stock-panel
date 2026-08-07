class StrategyState:

    def __init__(self):
        self.strategy = None
        self.market = None
        self.performance = 0


    def update(self, data):
        self.strategy = data["strategy"]
        self.market = data["market"]
        self.performance = data["performance"]


    def snapshot(self):
        return {
            "strategy": self.strategy,
            "market": self.market,
            "performance": self.performance
        }