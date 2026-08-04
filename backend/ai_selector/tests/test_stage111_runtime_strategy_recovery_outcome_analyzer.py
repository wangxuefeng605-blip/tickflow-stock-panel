from core.runtime_strategy_recovery_outcome_analyzer import (
    RuntimeStrategyRecoveryOutcomeAnalyzer
)



def test_runtime_strategy_recovery_success_analysis():

    analyzer = RuntimeStrategyRecoveryOutcomeAnalyzer()


    result = analyzer.analyze(
        {
            "action": "fallback",
            "status": "success"
        }
    )


    assert result["success"] is True
    assert result["score"] == 1.0
    assert result["recommendation"] == "keep"



def test_runtime_strategy_recovery_failure_analysis():

    analyzer = RuntimeStrategyRecoveryOutcomeAnalyzer()


    result = analyzer.analyze(
        {
            "action": "rollback",
            "status": "failed"
        }
    )


    assert result["success"] is False
    assert result["recommendation"] == "retry"



def test_runtime_strategy_recovery_analysis_history():

    analyzer = RuntimeStrategyRecoveryOutcomeAnalyzer()


    analyzer.analyze(
        {
            "action": "fallback",
            "status": "success"
        }
    )


    assert len(
        analyzer.analysis_history()
    ) == 1