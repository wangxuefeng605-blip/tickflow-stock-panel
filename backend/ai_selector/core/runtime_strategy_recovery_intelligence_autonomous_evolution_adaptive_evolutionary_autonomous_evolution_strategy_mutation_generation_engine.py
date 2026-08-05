import random


class RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryAutonomousEvolutionStrategyMutationGenerationEngine:
    """
    Generates new strategies through mutation.
    """

    def __init__(self):

        self.strategies = {}

        self.generated = []

        self.history = []



    def add_strategy(
        self,
        name,
        parameters
    ):

        self.strategies[name] = parameters


        result = {

            "strategy": name,

            "added": True

        }


        self.history.append(
            {
                "action": "add",
                "result": result
            }
        )


        return result



    def mutate(
        self,
        name
    ):

        if name not in self.strategies:

            return None


        base = self.strategies[name].copy()


        for key in base:

            if isinstance(
                base[key],
                float
            ):

                change = random.choice(
                    [
                        -0.1,
                        0.1
                    ]
                )

                base[key] = round(
                    max(
                        min(
                            base[key] + change,
                            1
                        ),
                        0
                    ),
                    3
                )


        new_name = (
            name
            +
            "_mutation"
        )


        self.generated.append(
            new_name
        )


        self.strategies[new_name] = base


        result = {

            "parent": name,

            "child": new_name,

            "parameters": base

        }


        self.history.append(
            {
                "action": "mutation",
                "result": result
            }
        )


        return result



    def generate_population(
        self,
        count=1
    ):

        results = []


        names = list(
            self.strategies.keys()
        )


        for i in range(
            min(
                count,
                len(names)
            )
        ):

            results.append(
                self.mutate(
                    names[i]
                )
            )


        return results



    def get_generated(self):

        return self.generated



    def get_history(self):

        return self.history