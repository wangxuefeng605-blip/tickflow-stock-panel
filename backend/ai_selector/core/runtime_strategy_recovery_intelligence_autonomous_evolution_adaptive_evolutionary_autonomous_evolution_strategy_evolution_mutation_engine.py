class RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryAutonomousEvolutionStrategyEvolutionMutationEngine:
    """
    Generates strategy mutations and new strategy variants.
    """

    def __init__(self):

        self.strategies = {}

        self.mutations = []

        self.history = []



    def register_strategy(
        self,
        name,
        parameters=None
    ):

        self.strategies[name] = parameters or {}


        result = {

            "strategy": name,

            "registered": True

        }


        self.history.append(
            {
                "action": "register",
                "result": result
            }
        )


        return result



    def mutate_parameter(
        self,
        name,
        key,
        delta
    ):

        if name not in self.strategies:

            return None


        value = self.strategies[name].get(
            key,
            0
        )


        new_value = round(
            value + delta,
            3
        )


        mutation = {

            "strategy": name,

            "parameter": key,

            "old": value,

            "new": new_value

        }


        self.strategies[name][key] = new_value


        self.mutations.append(
            mutation
        )


        self.history.append(
            {
                "action": "mutation",
                "result": mutation
            }
        )


        return mutation



    def create_variant(
        self,
        source,
        variant
    ):

        if source not in self.strategies:

            return None


        self.strategies[variant] = (
            self.strategies[source].copy()
        )


        result = {

            "source": source,

            "variant": variant,

            "created": True

        }


        self.history.append(
            {
                "action": "variant",
                "result": result
            }
        )


        return result



    def compare(
        self,
        first,
        second
    ):

        if first not in self.strategies:
            return None

        if second not in self.strategies:
            return None


        return {

            "first": self.strategies[first],

            "second": self.strategies[second]

        }



    def get_history(self):

        return self.history