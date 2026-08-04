from core.runtime_strategy_recovery_learning_weight_adjuster import (
    RuntimeStrategyRecoveryLearningWeightAdjuster
)


def test_runtime_strategy_weight_positive():

    adjuster = (
        RuntimeStrategyRecoveryLearningWeightAdjuster()
    )


    result = adjuster.adjust(
        {
            "policy": "restore",
            "learning_score": 1.0
        }
    )


    assert result["weight"] == 1.1



def test_runtime_strategy_weight_negative():

    adjuster = (
        RuntimeStrategyRecoveryLearningWeightAdjuster()
    )


    result = adjuster.adjust(
        {
            "policy": "rollback",
            "learning_score": -1.0
        }
    )


    assert result["weight"] == 0.9



def test_runtime_strategy_weight_history():

    adjuster = (
        RuntimeStrategyRecoveryLearningWeightAdjuster()
    )


    adjuster.adjust(
        {
            "policy": "fallback",
            "learning_score": 1.0
        }
    )


    assert len(
        adjuster.get_history()
    ) == 1