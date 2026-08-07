"""
Evolution Controller

Stage28 Self Evolution Layer
"""

from core.evolution.evolution_memory import EvolutionMemory
from core.evolution.strategy_mutation_engine import (
    StrategyMutationEngine
)
from core.evolution.evolution_evaluator import (
    EvolutionEvaluator
)


class EvolutionController:


    def __init__(self):

        self.memory = EvolutionMemory()

        self.mutation = StrategyMutationEngine()

        self.evaluator = EvolutionEvaluator()



    def evolve(self, strategy):

        candidates = (
            self.mutation
            .generate_candidates(
                strategy
            )
        )


        evaluated = []

        for item in candidates:

         evaluation = (
             self.evaluator
             .evaluate(
                 strategy,
                 item
             )
         )

         evaluated.append(
            {
                 "strategy": item,
                 "score": evaluation["improvement"],
                 "evaluation": evaluation
            }
        ) 
            
        best = max(
            evaluated,
            key=lambda x:x["score"]
        )


        self.memory.save_strategy(
            best["strategy"],
            best["score"]
        )


        return best