class RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryAutonomousEvolutionStrategyEvolutionAutonomousSelfAdaptiveRecoveryIntelligenceEngine:
    """
    Selects recovery strategies adaptively based on context.
    """

    def __init__(self):

        self.context = {}

        self.strategies = {}

        self.history = []



    def update_context(
        self,
        key,
        value
    ):

        self.context[key] = value


        result = {

            "key": key,

            "value": value

        }


        self.history.append(
            {
                "action": "context",
                "result": result
            }
        )


        return result



    def register_strategy(
        self,
        problem,
        strategy,
        priority=0
    ):

        if problem not in self.strategies:

            self.strategies[problem] = []


        item = {

            "strategy": strategy,

            "priority": priority

        }


        self.strategies[problem].append(
            item
        )


        self.history.append(
            {
                "action": "register",
                "result": item
            }
        )


        return item



    def select_recovery(
        self,
        problem
    ):

        candidates = self.strategies.get(
            problem,
            []
        )


        if not candidates:

            return None


        selected = max(
            candidates,
            key=lambda x:
            x["priority"]
        )


        result = {

            "problem": problem,

            "selected":
                selected["strategy"]

        }


        self.history.append(
            {
                "action": "select",
                "result": result
            }
        )


        return result



    def get_history(
        self
    ):

        return self.history