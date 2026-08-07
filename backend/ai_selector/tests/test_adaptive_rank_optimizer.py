from core.learning import AdaptiveRankOptimizer


def test_adaptive_rank_optimizer():


    optimizer = AdaptiveRankOptimizer()


    weights = {

        "momentum":0.3,

        "risk":0.2

    }


    result = optimizer.optimize(
        weights,
        [
            {
                "reward":1
            }
        ]
    )


    assert result["momentum"] > 0.3