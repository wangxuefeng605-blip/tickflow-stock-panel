from core.runtime_strategy_recovery_execution_feedback_analyzer import (
    RuntimeStrategyRecoveryExecutionFeedbackAnalyzer
)


def test_runtime_strategy_execution_success_feedback():

    analyzer = (
        RuntimeStrategyRecoveryExecutionFeedbackAnalyzer()
    )


    result = analyzer.analyze(
        {
            "status": "executed",
            "action": "restore"
        }
    )


    assert result["success_score"] == 1.0
    assert result["learning_signal"] == 1



def test_runtime_strategy_execution_block_feedback():

    analyzer = (
        RuntimeStrategyRecoveryExecutionFeedbackAnalyzer()
    )


    result = analyzer.analyze(
        {
            "status": "blocked",
            "action": "rollback"
        }
    )


    assert result["recovery_quality"] == "blocked"



def test_runtime_strategy_feedback_history():

    analyzer = (
        RuntimeStrategyRecoveryExecutionFeedbackAnalyzer()
    )


    analyzer.analyze(
        {
            "status": "executed",
            "action": "fallback"
        }
    )


    assert len(
        analyzer.get_history()
    ) == 1