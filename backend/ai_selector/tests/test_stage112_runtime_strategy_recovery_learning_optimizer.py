from core.runtime_strategy_recovery_learning_optimizer import (
    RuntimeStrategyRecoveryLearningOptimizer
)



def test_runtime_strategy_recovery_learning_success():

    optimizer = RuntimeStrategyRecoveryLearningOptimizer()


    result = optimizer.optimize(
        {
            "action": "fallback",
            "success": True
        }
    )


    assert result["weight"] == 1.1



def test_runtime_strategy_recovery_learning_failure():

    optimizer = RuntimeStrategyRecoveryLearningOptimizer()


    result = optimizer.optimize(
        {
            "action": "rollback",
            "success": False
        }
    )


    assert result["weight"] == 0.9



def test_runtime_strategy_recovery_learning_history():

    optimizer = RuntimeStrategyRecoveryLearningOptimizer()


    optimizer.optimize(
        {
            "action": "fallback",
            "success": True
        }
    )


    assert len(
        optimizer.optimization_history()
    ) == 1