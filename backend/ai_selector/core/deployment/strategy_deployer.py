class StrategyDeployer:

    def __init__(
        self,
        registry
    ):

        self.registry = registry


    def deploy(
        self,
        policy
    ):

        self.registry.activate(
            policy
        )

        return self.registry.get_active()