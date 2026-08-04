class RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionMetaStrategyController:
    """
    Controls high level autonomous evolution strategies.
    """

    def __init__(self):

        self.strategies = {}

        self.active_strategy = None

        self.history = []


    def register_strategy(
        self,
        name,
        config
    ):

        self.strategies[name] = config


        self.history.append(
            {
                "action": "register",
                "strategy": name
            }
        )


        return config



    def select_strategy(
        self,
        name
    ):

        if name not in self.strategies:

            return None


        self.active_strategy = name


        result = {

            "selected": name,

            "config": self.strategies[name]

        }


        self.history.append(
            {
                "action": "select",
                "strategy": name
            }
        )


        return result



    def get_active_strategy(self):

        return self.active_strategy



    def get_strategies(self):

        return self.strategies



    def get_history(self):

        return self.history