from core.optimization.strategy_optimizer import (
    StrategyOptimizer
)


def test_strategy_optimizer():

    optimizer = StrategyOptimizer()


    result = optimizer.optimize(
        {
            "strategy": "momentum",
            "score": 0.85
        }
    )


    assert result["status"] == "optimized"

    assert result["strategy"] == "momentum"

    assert result["score"] == 0.85