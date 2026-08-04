class RuntimeStrategyInjector:


    def __init__(self):

        self.config = None


    def inject(self, strategy):

        self.config = {
            "strategy": strategy["name"],
            "weight": strategy.get(
                "weight",
                1.0
            )
        }

        return self.config


    def current(self):

        return self.config