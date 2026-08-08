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

        candidates = self.generator.generate(strategy)

        best = candidates[-1]

        self.state.add_strategy(best)

        self.state.evolve_generation()

        self.state.set_best(best)

        return {
            "strategy": best.get(
                "strategy",
                strategy.get("strategy", "unknown")
                if isinstance(strategy, dict)
                else "unknown"
            ),
            "score": best.get(
                "score",
                strategy.get("score", 0)
                if isinstance(strategy, dict)
                else 0
            ),
            "mutation": "increase_weight",
            "best_strategy": best,
            "generation": self.state.generation
        }