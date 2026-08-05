from core.runtime_strategy_recovery_intelligence_autonomous_evolution_adaptive_evolutionary_autonomous_evolution_contextual_strategy_adaptation_engine import (
    RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryAutonomousEvolutionContextualStrategyAdaptationEngine
)



def test_register_strategy():

    engine = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryAutonomousEvolutionContextualStrategyAdaptationEngine()
    )


    result = engine.register_strategy(
        "BULL",
        {
            "aggressiveness": 0.6
        }
    )


    assert result["registered"] is True



def test_select_strategy():

    engine = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryAutonomousEvolutionContextualStrategyAdaptationEngine()
    )


    engine.register_strategy(
        "BULL",
        {
            "mode": "growth"
        }
    )


    result = engine.select_strategy(
        "BULL"
    )


    assert result["strategy"]["mode"] == "growth"



def test_adapt_positive():

    engine = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryAutonomousEvolutionContextualStrategyAdaptationEngine()
    )


    result = engine.adapt_parameters(
        {
            "aggressiveness": 0.5
        },
        1
    )


    assert result["strategy"]["aggressiveness"] == 0.6



def test_adapt_negative():

    engine = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryAutonomousEvolutionContextualStrategyAdaptationEngine()
    )


    result = engine.adapt_parameters(
        {
            "aggressiveness": 0.5
        },
        -1
    )


    assert result["strategy"]["aggressiveness"] == 0.4