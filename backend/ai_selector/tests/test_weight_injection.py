from core.learning.weight_provider import (
    WeightProvider
)


def test_weight_provider():


    provider = WeightProvider()


    weights = provider.get_weights()


    assert weights["momentum"] == 0.2



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