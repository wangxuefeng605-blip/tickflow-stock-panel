from core.runtime_strategy_recovery_intelligence_autonomous_evolution_adaptive_feedback_analyzer import (
    RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveFeedbackAnalyzer
)



def test_feedback_success():

    analyzer = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveFeedbackAnalyzer()
    )


    result = analyzer.analyze(
        {
            "status": "executed",
            "strategy": "adaptive_restore"
        }
    )


    assert result["success"] is True
    assert result["performance"] == 1.0
    assert result["improvement_signal"] == "increase"



def test_feedback_failure():

    analyzer = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveFeedbackAnalyzer()
    )


    result = analyzer.analyze(
        {
            "status": "blocked",
            "strategy": "unsafe"
        }
    )


    assert result["success"] is False
    assert result["improvement_signal"] == "adjust"



def test_feedback_history():

    analyzer = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveFeedbackAnalyzer()
    )


    analyzer.analyze(
        {
            "status": "executed",
            "strategy": "test"
        }
    )


    assert len(
        analyzer.get_history()
    ) == 1