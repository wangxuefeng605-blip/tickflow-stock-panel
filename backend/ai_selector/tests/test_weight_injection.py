from core.learning.weight_provider import (
    WeightProvider
)


def test_weight_provider():

    provider = WeightProvider()

    weights = provider.get_weights()

    assert weights["momentum"] == 0.3
    assert weights["trend"] == 0.25
    assert weights["volume_factor"] == 0.15
    assert weights["volatility"] == 0.1
    assert weights["quality"] == 0.1
    assert weights["growth"] == 0.1



    provider.update(
        {
            "momentum":0.5
        }
    )


    assert (
        provider.get_weights()["momentum"]
        ==
        0.5
    )