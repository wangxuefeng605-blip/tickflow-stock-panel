from core.runtime_strategy_recovery_intelligence_autonomous_evolution_adaptive_evolutionary_autonomous_evolution_strategy_feedback_learning_engine import (
    RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryAutonomousEvolutionStrategyFeedbackLearningEngine
)



def test_register():

    engine = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryAutonomousEvolutionStrategyFeedbackLearningEngine()
    )


    result = engine.register_strategy(
        "trend"
    )


    assert result["registered"] is True



def test_collect_feedback():

    engine = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryAutonomousEvolutionStrategyFeedbackLearningEngine()
    )


    engine.register_strategy(
        "trend"
    )


    result = engine.collect_feedback(
        "trend",
        "buy",
        "success"
    )


    assert result["stored"] is True



def test_learning_score():

    engine = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryAutonomousEvolutionStrategyFeedbackLearningEngine()
    )


    engine.register_strategy(
        "alpha"
    )


    engine.collect_feedback(
        "alpha",
        "buy",
        "success"
    )


    engine.collect_feedback(
        "alpha",
        "sell",
        "failure"
    )


    result = engine.update_learning(
        "alpha"
    )


    assert result["learning_score"] == 0.5



def test_get_learning():

    engine = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryAutonomousEvolutionStrategyFeedbackLearningEngine()
    )


    engine.register_strategy(
        "momentum"
    )


    result = engine.get_learning(
        "momentum"
    )


    assert result["success"] == 0