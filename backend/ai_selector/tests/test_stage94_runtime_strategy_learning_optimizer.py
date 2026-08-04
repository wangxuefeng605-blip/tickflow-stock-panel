from core.runtime_strategy_learning_optimizer import (
    RuntimeStrategyLearningOptimizer
)


def test_runtime_strategy_learning_optimizer():

    optimizer = RuntimeStrategyLearningOptimizer()


    result = optimizer.optimize(
        {
            "reward":0.8
        }
    )


    assert result["optimized"] is True
    assert result["adjustments"] == {}