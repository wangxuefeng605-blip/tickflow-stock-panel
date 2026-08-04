from core.runtime_strategy_recovery_learning_weight_optimizer import (
    RuntimeStrategyRecoveryLearningWeightOptimizer
)



def test_runtime_strategy_learning_weight_increase():

    optimizer = RuntimeStrategyRecoveryLearningWeightOptimizer()


    result = optimizer.optimize(
        {
            "policy": "fallback",
            "learning_weight": 1.1
        }
    )


    assert result["new_weight"] == 1.1



def test_runtime_strategy_learning_weight_decrease():

    optimizer = RuntimeStrategyRecoveryLearningWeightOptimizer()


    result = optimizer.optimize(
        {
            "policy": "rollback",
            "learning_weight": 0.9
        }
    )


    assert result["new_weight"] == 0.9



def test_runtime_strategy_learning_weight_history():

    optimizer = RuntimeStrategyRecoveryLearningWeightOptimizer()


    optimizer.optimize(
        {
            "policy": "restore",
            "learning_weight": 1.1
        }
    )


    assert len(
        optimizer.get_history()
    ) == 1