from core.runtime_strategy_recovery_intelligence_learning_feedback_integrator import (
    RuntimeStrategyRecoveryIntelligenceLearningFeedbackIntegrator
)



def test_learning_integrator_positive():

    integrator = (
        RuntimeStrategyRecoveryIntelligenceLearningFeedbackIntegrator()
    )


    result = integrator.integrate(
        {
            "learning_feedback": "positive"
        }
    )


    assert result["learning_signal"] == "reward"
    assert result["weight_delta"] == 0.1



def test_learning_integrator_negative():

    integrator = (
        RuntimeStrategyRecoveryIntelligenceLearningFeedbackIntegrator()
    )


    result = integrator.integrate(
        {
            "learning_feedback": "negative",
            "failure_reason": "timeout"
        }
    )


    assert result["learning_signal"] == "penalty"
    assert result["weight_delta"] == -0.1
    assert result["experience"] == "timeout"



def test_learning_history():

    integrator = (
        RuntimeStrategyRecoveryIntelligenceLearningFeedbackIntegrator()
    )


    integrator.integrate(
        {
            "learning_feedback": "positive"
        }
    )


    assert len(
        integrator.get_history()
    ) == 1


    assert len(
        integrator.get_memory()
    ) == 1