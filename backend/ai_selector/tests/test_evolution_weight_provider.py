from core.evolution.evolution_weight_provider import (
    EvolutionWeightProvider
)


def test_weight_provider():


    provider = EvolutionWeightProvider()


    weights = (
        provider.get_weights()
    )


    assert (
        "momentum"
        in weights
    )


    assert (
        round(
            sum(weights.values()),
            4
        )
        == 1
    )