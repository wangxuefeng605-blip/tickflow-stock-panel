class PortfolioRuntimeState:

    def __init__(self):
        self.last_strategy = None
        self.last_allocation = None
        self.last_decision = None
        self.feedback = None
        self.learning_updated = False


    def update(self, data):

        for k, v in data.items():
            setattr(self, k, v)


    def snapshot(self):

        return {
            "strategy": self.last_strategy,
            "allocation": self.last_allocation,
            "decision": self.last_decision,
            "learning_updated": self.learning_updated
        }