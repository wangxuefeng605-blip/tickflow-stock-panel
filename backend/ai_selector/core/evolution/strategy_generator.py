from core.evolution.mutation_engine import MutationEngine


class StrategyGenerator:


    def __init__(self):

        self.mutation_engine = MutationEngine()



    def generate(
        self,
        strategy
    ):

        mutated = (
            self.mutation_engine
            .mutate(strategy)
        )


        return [
            strategy,
            mutated["strategy"]
        ]