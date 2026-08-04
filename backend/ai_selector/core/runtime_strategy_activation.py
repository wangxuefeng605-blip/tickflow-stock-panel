class RuntimeStrategyActivation:


    def __init__(self):

        self.strategy = None


    def activate(self, strategy):

        self.strategy = strategy

        return {
            "activated": True,
            "strategy": strategy
        }


    def current(self):

        return self.strategy