from core.runtime_strategy_recovery_feedback_learning_adapter import (
    RuntimeStrategyRecoveryFeedbackLearningAdapter
)


def test_runtime_strategy_positive_learning():

    adapter = (
        RuntimeStrategyRecoveryFeedbackLearningAdapter()
    )


    result = adapter.adapt(
        {
            "policy": "restore",
            "feedback": "POSITIVE"
        }
    )


    assert result["learning_score"] == 1.0



def test_runtime_strategy_negative_learning():

    adapter = (
        RuntimeStrategyRecoveryFeedbackLearningAdapter()
    )


    result = adapter.adapt(
        {
            "policy": "rollback",
            "feedback": "NEGATIVE"
        }
    )


    assert result["learning_score"] == -1.0



def test_runtime_strategy_learning_history():

    adapter = (
        RuntimeStrategyRecoveryFeedbackLearningAdapter()
    )


    adapter.adapt(
        {
            "policy": "fallback",
            "feedback": "POSITIVE"
        }
    )


    assert len(
        adapter.get_history()
    ) == 1