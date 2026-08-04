from core.runtime_strategy_recovery_intelligence_autonomous_feedback_loop_controller import (
    RuntimeStrategyRecoveryIntelligenceAutonomousFeedbackLoopController
)



def test_feedback_loop_success():

    controller = (
        RuntimeStrategyRecoveryIntelligenceAutonomousFeedbackLoopController()
    )


    result = controller.process(
        {
            "executed": True
        }
    )


    assert result["status"] == "success"
    assert result["learning_signal"] == "reward"
    assert result["score_delta"] == 0.1



def test_feedback_loop_failure():

    controller = (
        RuntimeStrategyRecoveryIntelligenceAutonomousFeedbackLoopController()
    )


    result = controller.process(
        {
            "executed": False
        }
    )


    assert result["status"] == "failure"
    assert result["learning_signal"] == "penalty"



def test_feedback_loop_history():

    controller = (
        RuntimeStrategyRecoveryIntelligenceAutonomousFeedbackLoopController()
    )


    controller.process(
        {
            "executed": True
        }
    )


    assert len(
        controller.get_history()
    ) == 1


    assert len(
        controller.get_memory()
    ) == 1