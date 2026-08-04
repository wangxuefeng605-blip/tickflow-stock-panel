from core.runtime_strategy_recovery_decision_execution_feedback_collector import (
    RuntimeStrategyRecoveryDecisionExecutionFeedbackCollector
)


def test_runtime_strategy_positive_feedback():

    collector = (
        RuntimeStrategyRecoveryDecisionExecutionFeedbackCollector()
    )


    result = collector.collect(
        {
            "policy": "restore",
            "status": "SUCCESS"
        }
    )


    assert result["feedback"] == "POSITIVE"



def test_runtime_strategy_negative_feedback():

    collector = (
        RuntimeStrategyRecoveryDecisionExecutionFeedbackCollector()
    )


    result = collector.collect(
        {
            "policy": "rollback",
            "status": "FAILED"
        }
    )


    assert result["feedback"] == "NEGATIVE"



def test_runtime_strategy_feedback_history():

    collector = (
        RuntimeStrategyRecoveryDecisionExecutionFeedbackCollector()
    )


    collector.collect(
        {
            "policy": "fallback",
            "status": "SUCCESS"
        }
    )


    assert len(
        collector.get_history()
    ) == 1