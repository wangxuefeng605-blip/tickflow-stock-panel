class RuntimeStrategyExecutionHook:


    def __init__(self):

        self.context = None


    def prepare(self, strategy):

        self.context = {
            "strategy": strategy["strategy"],
            "weight": strategy.get(
                "weight",
                1.0
            ),
            "active": True
        }

        return self.context


    def current(self):

        return self.context