from core.runtime_strategy_recovery_feedback_loop_manager import (
    RuntimeStrategyRecoveryFeedbackLoopManager
)



def test_runtime_strategy_recovery_feedback_success():

    manager = RuntimeStrategyRecoveryFeedbackLoopManager()


    result = manager.collect_feedback(
        {
            "policy": "fallback",
            "status": "executed"
        }
    )


    assert result["success"] is True
    assert result["feedback_score"] == 1.0



def test_runtime_strategy_recovery_feedback_failed():

    manager = RuntimeStrategyRecoveryFeedbackLoopManager()


    result = manager.collect_feedback(
        {
            "policy": "rollback",
            "status": "failed"
        }
    )


    assert result["success"] is False
    assert result["feedback_score"] == 0.0



def test_runtime_strategy_recovery_feedback_history():

    manager = RuntimeStrategyRecoveryFeedbackLoopManager()


    manager.collect_feedback(
        {
            "policy": "parameter_restore",
            "status": "executed"
        }
    )


    assert len(
        manager.feedback_history()
    ) == 1