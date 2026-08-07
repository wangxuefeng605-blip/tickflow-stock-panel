from core.learning import RuntimeWeightProvider

def test_ranking_uses_runtime_weights():

    provider = RuntimeWeightProvider()

    provider.update(
        {
            "momentum":0.8
        }
    )

    weights = provider.get_weights()

    assert weights["momentum"] == 0.8