from core.runtime_strategy_recovery_autonomous_learning_optimizer import (
    RuntimeStrategyRecoveryAutonomousLearningOptimizer
)


def test_runtime_strategy_optimizer_increase():

    optimizer = (
        RuntimeStrategyRecoveryAutonomousLearningOptimizer()
    )


    result = optimizer.optimize(
        {
            "learning_action": "reinforce",
            "signal": 1
        }
    )


    assert result["optimization_action"] == "increase"
    assert result["weight_adjustment"] == 0.1



def test_runtime_strategy_optimizer_decrease():

    optimizer = (
        RuntimeStrategyRecoveryAutonomousLearningOptimizer()
    )


    result = optimizer.optimize(
        {
            "learning_action": "adjust",
            "signal": -1
        }
    )


    assert result["optimization_action"] == "decrease"



def test_runtime_strategy_optimizer_history():

    optimizer = (
        RuntimeStrategyRecoveryAutonomousLearningOptimizer()
    )


    optimizer.optimize(
        {
            "learning_action": "reinforce"
        }
    )


    assert len(
        optimizer.get_history()
    ) == 1