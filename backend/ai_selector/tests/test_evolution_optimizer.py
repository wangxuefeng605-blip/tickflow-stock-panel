from core.evolution.evolution_optimizer import EvolutionOptimizer


def test_optimizer():

    optimizer = EvolutionOptimizer()


    result = optimizer.optimize(
        {
            "momentum":0.35,
            "trend":0.30,
            "quality":0.15,
            "liquidity":0.10,
            "risk":0.10
        },
        {
            "average_reward":1
        }
    )


    assert result["momentum"] > 0.35

    assert round(
        sum(result.values()),
        4
    ) == 1