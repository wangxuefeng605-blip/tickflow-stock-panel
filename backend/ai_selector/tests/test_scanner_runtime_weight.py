from core.learning.runtime_weight_provider import (
    RuntimeWeightProvider
)


def test_scanner_runtime_weight():

    provider = RuntimeWeightProvider()


    weights = provider.get_weights()


    assert "momentum" in weights
    assert "trend" in weights