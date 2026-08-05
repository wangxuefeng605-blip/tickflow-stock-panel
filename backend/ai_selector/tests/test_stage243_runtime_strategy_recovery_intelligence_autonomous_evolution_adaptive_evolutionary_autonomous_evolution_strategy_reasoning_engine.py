from core.runtime_strategy_recovery_intelligence_autonomous_evolution_adaptive_evolutionary_autonomous_evolution_strategy_reasoning_engine import (
    RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryAutonomousEvolutionStrategyReasoningEngine
)



def test_register_fact():

    engine = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryAutonomousEvolutionStrategyReasoningEngine()
    )


    result = engine.register_fact(
        "momentum",
        "works_in",
        "bull_market"
    )


    assert result["stored"] is True



def test_reason():

    engine = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryAutonomousEvolutionStrategyReasoningEngine()
    )


    engine.register_fact(
        "momentum",
        "works_in",
        "bull_market"
    )


    result = engine.reason(
        "momentum",
        "works_in"
    )


    assert "bull_market" in result["conclusions"]



def test_explain():

    engine = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryAutonomousEvolutionStrategyReasoningEngine()
    )


    engine.register_fact(
        "trend",
        "requires",
        "volume"
    )


    result = engine.explain(
        "trend"
    )


    assert len(result["explanation"]) == 1



def test_empty_reason():

    engine = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryAutonomousEvolutionStrategyReasoningEngine()
    )


    result = engine.reason(
        "unknown",
        "works_in"
    )


    assert result["conclusions"] == []