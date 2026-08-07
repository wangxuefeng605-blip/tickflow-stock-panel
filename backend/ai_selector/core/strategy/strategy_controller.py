"""
Strategy Controller

Stage33 Strategy Intelligence
"""


from .strategy_evaluator import StrategyEvaluator
from .strategy_evolution_engine import StrategyEvolutionEngine
from .strategy_mutation_engine import StrategyMutationEngine



class StrategyController:


    def __init__(self):

        self.evaluator = StrategyEvaluator()

        self.evolution = StrategyEvolutionEngine()

        self.mutation = StrategyMutationEngine()



    def process(
        self,
        strategy,
        performance
    ):

        evaluation = self.evaluator.evaluate(
            performance
        )


        evaluation["strategy"] = strategy


        decision = self.evolution.evolve(
            evaluation
        )


        if decision["action"] == "MODIFY":

            decision["candidates"] = (
                self.mutation.mutate(strategy)
            )


        return decision