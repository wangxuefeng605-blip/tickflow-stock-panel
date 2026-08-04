class RuntimeStrategyDeployer:


    def __init__(self):

        self.active_strategy = None


    def deploy(self, strategy):

        self.active_strategy = strategy


        return {

            "deployed": True,

            "strategy":
                strategy

        }


    def current(self):

        return self.active_strategy