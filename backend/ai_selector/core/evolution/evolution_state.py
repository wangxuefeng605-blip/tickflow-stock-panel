"""
Evolution State

Track strategy evolution progress.
"""


class EvolutionState:


    def __init__(self):

        self.generation = 0

        self.strategies = []

        self.best_strategy = None



    def add_strategy(
        self,
        strategy
    ):

        self.strategies.append(strategy)



    def evolve_generation(self):

        self.generation += 1



    def set_best(
        self,
        strategy
    ):

        self.best_strategy = strategy



    def snapshot(self):

        return {

            "generation":
                self.generation,

            "strategy_count":
                len(self.strategies),

            "best_strategy":
                self.best_strategy

        }