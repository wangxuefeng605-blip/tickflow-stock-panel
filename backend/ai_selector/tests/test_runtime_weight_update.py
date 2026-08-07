from core.learning import (
    RuntimeWeightProvider,
    AdaptiveRankOptimizer
)



def test_runtime_weight_update():


    provider = RuntimeWeightProvider()


    optimizer = AdaptiveRankOptimizer()


    old = provider.get_weights()


    new = optimizer.optimize(
        old,
        [
            {
                "reward":1
            }
        ]
    )


    result = provider.update_weights(
        new
    )


    assert result["momentum"] > 0