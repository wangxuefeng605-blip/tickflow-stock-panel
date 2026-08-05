from core.runtime_strategy_recovery_intelligence_autonomous_evolution_adaptive_evolutionary_autonomous_evolution_strategy_evolution_reasoning_engine import (
    RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryAutonomousEvolutionStrategyEvolutionReasoningEngine
)



def test_register():

    engine = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryAutonomousEvolutionStrategyEvolutionReasoningEngine()
    )


    result = engine.register_strategy(
        "momentum"
    )


    assert result["registered"] is True



def test_fact():

    engine = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryAutonomousEvolutionStrategyEvolutionReasoningEngine()
    )


    engine.register_strategy(
        "trend"
    )


    result = engine.add_fact(
        "trend",
        "volume_increase"
    )


    assert result["stored"] is True



def test_rule_reasoning():

    engine = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryAutonomousEvolutionStrategyEvolutionReasoningEngine()
    )


    engine.register_strategy(
        "alpha"
    )


    engine.add_rule(
        "alpha",
        "bull_market",
        "increase_position"
    )


    result = engine.reason(
        "alpha",
        "bull_market"
    )


    assert result["conclusions"][0] == "increase_position"



def test_causal():

    engine = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryAutonomousEvolutionStrategyEvolutionReasoningEngine()
    )


    result = engine.causal_analysis(
        "market_up",
        "momentum_strength"
    )


    assert result["relationship"] == "possible"