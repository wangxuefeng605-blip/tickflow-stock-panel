from core.runtime_strategy_recovery_feedback_learning_controller import (
    RuntimeStrategyRecoveryFeedbackLearningController
)


def test_runtime_strategy_feedback_learning_controller():

    controller = (
        RuntimeStrategyRecoveryFeedbackLearningController()
    )


    result = controller.process(
        {
            "policy": "restore",
            "success": True,
            "confidence": 0.85
        }
    )


    assert result["status"] == "learning"
    assert result["policy"] == "restore"



def test_runtime_strategy_feedback_learning_failure():

    controller = (
        RuntimeStrategyRecoveryFeedbackLearningController()
    )


    result = controller.process(
        {
            "policy": "fallback",
            "success": False,
            "confidence": 0.3
        }
    )


    assert result["status"] == "learning"



def test_runtime_strategy_feedback_learning_history():

    controller = (
        RuntimeStrategyRecoveryFeedbackLearningController()
    )


    controller.process(
        {
            "policy": "restore",
            "success": True,
            "confidence": 0.9
        }
    )


    assert len(
        controller.get_history()
    ) == 1