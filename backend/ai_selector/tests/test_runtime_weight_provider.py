from core.learning.runtime_weight_provider import (
    RuntimeWeightProvider
)


def test_runtime_weight_provider():


    provider = RuntimeWeightProvider()


    old = provider.get_weights()


    assert old["momentum"] == 0.35



    result = provider.update(
        {
            "momentum":0.5
        }
    )


    assert result["momentum"] == 0.5