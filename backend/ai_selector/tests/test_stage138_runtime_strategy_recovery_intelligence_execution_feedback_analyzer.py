from core.runtime_strategy_recovery_intelligence_execution_feedback_analyzer import (
    RuntimeStrategyRecoveryIntelligenceExecutionFeedbackAnalyzer
)



def test_feedback_analyzer_success():

    analyzer = (
        RuntimeStrategyRecoveryIntelligenceExecutionFeedbackAnalyzer()
    )


    result = analyzer.analyze(
        {
            "health": True
        }
    )


    assert result["success_rate"] == 1.0
    assert result["learning_feedback"] == "positive"



def test_feedback_analyzer_failure():

    analyzer = (
        RuntimeStrategyRecoveryIntelligenceExecutionFeedbackAnalyzer()
    )


    result = analyzer.analyze(
        {
            "health": False,
            "alerts": [
                "timeout"
            ]
        }
    )


    assert result["failure_reason"] == "timeout"
    assert result["learning_feedback"] == "negative"



def test_feedback_history():

    analyzer = (
        RuntimeStrategyRecoveryIntelligenceExecutionFeedbackAnalyzer()
    )


    analyzer.analyze(
        {
            "health": True
        }
    )


    assert len(
        analyzer.get_history()
    ) == 1