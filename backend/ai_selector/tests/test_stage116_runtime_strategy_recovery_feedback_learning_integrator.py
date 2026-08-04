from core.runtime_strategy_recovery_feedback_learning_integrator import (
    RuntimeStrategyRecoveryFeedbackLearningIntegrator
)



def test_runtime_strategy_feedback_learning_success():

    manager = RuntimeStrategyRecoveryFeedbackLearningIntegrator()


    result = manager.integrate_feedback(
        {
            "policy": "fallback",
            "success": True,
            "feedback_score": 1.0
        }
    )


    assert result["updated"] is True
    assert result["learning_weight"] == 1.1



def test_runtime_strategy_feedback_learning_failed():

    manager = RuntimeStrategyRecoveryFeedbackLearningIntegrator()


    result = manager.integrate_feedback(
        {
            "policy": "rollback",
            "success": False,
            "feedback_score": 0.0
        }
    )


    assert result["learning_weight"] == 0.9



def test_runtime_strategy_feedback_learning_history():

    manager = RuntimeStrategyRecoveryFeedbackLearningIntegrator()


    manager.integrate_feedback(
        {
            "policy": "restore",
            "success": True
        }
    )


    assert len(
        manager.history()
    ) == 1