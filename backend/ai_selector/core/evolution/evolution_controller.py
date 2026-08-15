"""
Evolution Controller

Stage28 Self Evolution Layer
"""

from core.evolution.evolution_state import EvolutionState
from core.evolution.strategy_generator import StrategyGenerator


class EvolutionController:

    def __init__(self):

        self.state = EvolutionState()

        self.generator = StrategyGenerator()


    def evolve(self, strategy):

        candidates = self.generator.generate(
            strategy
        )


        if not candidates:
            candidates = [
                strategy
            ]


        best = candidates[-1]


        if best is None:
            best = strategy


        if not isinstance(best, dict):

            best = (
                strategy
                if isinstance(strategy, dict)
                else {
                    "strategy": "unknown",
                    "score": 0
                }
            )


        self.state.add_strategy(
            best
        )


        self.state.evolve_generation()


        self.state.set_best(
            best
        )


        fallback_strategy = (
            strategy.get(
                "strategy",
                "unknown"
            )
            if isinstance(strategy, dict)
            else "unknown"
        )


        fallback_score = (
            strategy.get(
                "score",
                0
            )
            if isinstance(strategy, dict)
            else 0
        )


        return {

            "strategy": best.get(
                "strategy",
                fallback_strategy
            ),


            "score": best.get(
                "score",
                fallback_score
            ),


            "mutation": "increase_weight",


            "best_strategy": best,


            "generation": self.state.generation
        }