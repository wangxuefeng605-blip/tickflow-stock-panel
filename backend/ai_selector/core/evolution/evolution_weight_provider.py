"""
Evolution Weight Provider

Stage55
"""

from core.evolution.evolution_persistence import (
    EvolutionPersistence
)


DEFAULT_WEIGHTS = {
    "momentum": 0.35,
    "trend": 0.30,
    "quality": 0.15,
    "liquidity": 0.10,
    "risk": 0.10
}


class EvolutionWeightProvider:


    def __init__(self):

        self.store = EvolutionPersistence()



    def get_weights(self):

        strategy = (
            self.store.load_strategy()
        )


        if not strategy:

            return DEFAULT_WEIGHTS


        weights = {}

        for key in DEFAULT_WEIGHTS:

            weights[key] = round(
                strategy.get(
                    key,
                    DEFAULT_WEIGHTS[key]
                ),
                4
            )


        total = sum(
            weights.values()
        )


        if total <= 0:

            return DEFAULT_WEIGHTS


        # normalize
        for key in weights:

            weights[key] = round(
                weights[key] / total,
                4
            )


        return weights