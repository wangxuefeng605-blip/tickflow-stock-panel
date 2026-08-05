from core.runtime_strategy_recovery_intelligence_autonomous_evolution_adaptive_evolutionary_autonomous_evolution_trade_feedback_learning_engine import (
    RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryAutonomousEvolutionTradeFeedbackLearningEngine
)



def test_record_trade():

    engine = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryAutonomousEvolutionTradeFeedbackLearningEngine()
    )


    result = engine.record_trade(
        "000001",
        "BUY",
        100
    )


    assert result["profit"] == 100



def test_success_learning():

    engine = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryAutonomousEvolutionTradeFeedbackLearningEngine()
    )


    trade = engine.record_trade(
        "000001",
        "BUY",
        100
    )


    result = engine.analyze_trade(
        trade
    )


    assert result["result"] == "SUCCESS"



def test_failure_learning():

    engine = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryAutonomousEvolutionTradeFeedbackLearningEngine()
    )


    trade = engine.record_trade(
        "000001",
        "BUY",
        -50
    )


    result = engine.analyze_trade(
        trade
    )


    assert result["result"] == "FAILURE"



def test_weight_update():

    engine = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryAutonomousEvolutionTradeFeedbackLearningEngine()
    )


    trade = engine.record_trade(
        "A",
        "BUY",
        20
    )


    engine.analyze_trade(
        trade
    )


    result = engine.update_strategy_weight(
        0.5
    )


    assert result["new"] == 0.55