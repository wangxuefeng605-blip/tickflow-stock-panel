from core.runtime_strategy_recovery_continuous_learning_coordinator import (
    RuntimeStrategyRecoveryContinuousLearningCoordinator
)


def test_runtime_strategy_learning_reinforce():

    coordinator = (
        RuntimeStrategyRecoveryContinuousLearningCoordinator()
    )


    result = coordinator.coordinate(
        {
            "learning_signal": 1,
            "recovery_quality": "positive"
        }
    )


    assert result["learning_action"] == "reinforce"



def test_runtime_strategy_learning_adjust():

    coordinator = (
        RuntimeStrategyRecoveryContinuousLearningCoordinator()
    )


    result = coordinator.coordinate(
        {
            "learning_signal": -1,
            "recovery_quality": "blocked"
        }
    )


    assert result["learning_action"] == "adjust"



def test_runtime_strategy_learning_history():

    coordinator = (
        RuntimeStrategyRecoveryContinuousLearningCoordinator()
    )


    coordinator.coordinate(
        {
            "learning_signal": 1
        }
    )


    assert len(
        coordinator.get_history()
    ) == 1