from core.runtime_strategy_recovery_intelligence_autonomous_evolution_feedback_analyzer import (
    RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionFeedbackAnalyzer
)



def test_feedback_success():

    analyzer = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionFeedbackAnalyzer()
    )


    result = analyzer.analyze(
        {
            "strategy": "restore",
            "status": "executed"
        }
    )


    assert result["reward"] == 1.0
    assert result["success"] is True



def test_feedback_monitor():

    analyzer = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionFeedbackAnalyzer()
    )


    result = analyzer.analyze(
        {
            "strategy": "restore",
            "status": "monitoring"
        }
    )


    assert result["reward"] == 0.5



def test_feedback_failure():

    analyzer = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionFeedbackAnalyzer()
    )


    result = analyzer.analyze(
        {
            "strategy": "rollback",
            "status": "held"
        }
    )


    assert result["reward"] == 0.0
    assert result["success"] is False



def test_feedback_history():

    analyzer = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionFeedbackAnalyzer()
    )


    analyzer.analyze(
        {
            "strategy": "test",
            "status": "executed"
        }
    )


    assert len(
        analyzer.get_history()
    ) == 1