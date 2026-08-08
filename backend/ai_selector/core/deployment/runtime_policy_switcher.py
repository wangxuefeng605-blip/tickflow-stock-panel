class RuntimePolicySwitcher:

    def __init__(
        self,
        registry
    ):
        self.registry = registry


    def switch(
        self,
        policy
    ):

        self.registry.activate(
            policy
        )

        return self.registry.get_active()


    def current(self):

        return self.registry.get_active()