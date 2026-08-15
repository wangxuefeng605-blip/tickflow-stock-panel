"""
Evolution Weight Provider

Stage55
"""

from core.evolution.evolution_persistence import (
    EvolutionPersistence
)


DEFAULT_WEIGHTS = {
    "momentum": 0.30,
    "trend": 0.25,
    "volume_factor": 0.15,
    "volatility": 0.10,
    "quality": 0.10,
    "growth": 0.10,
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
        keys = list(weights.keys())

        for key in keys:

            weights[key] = round(
                weights[key] / total,
                4
            )

        # Correct rounding drift so the final weights
        # always sum to exactly 1.0000.
        rounded_total = round(
            sum(weights.values()),
            4
        )

        drift = round(
            1.0 - rounded_total,
            4
        )

        if drift != 0:

            last_key = keys[-1]

            weights[last_key] = round(
                weights[last_key] + drift,
                4
            )

        return weights