from core.runtime_strategy_recovery_intelligence_autonomous_evolution_adaptive_evolutionary_autonomous_evolution_strategy_autonomous_optimization_engine import (
    RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryAutonomousEvolutionStrategyAutonomousOptimizationEngine
)



def test_register():

    engine = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryAutonomousEvolutionStrategyAutonomousOptimizationEngine()
    )


    result = engine.register_strategy(
        "momentum",
        {
            "risk":0.5
        }
    )


    assert result["registered"] is True



def test_parameter_change():

    engine = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryAutonomousEvolutionStrategyAutonomousOptimizationEngine()
    )


    engine.register_strategy(
        "alpha",
        {
            "risk":0.5
        }
    )


    result = engine.optimize_parameter(
        "alpha",
        "risk",
        "increase"
    )


    assert result["value"] == 0.6



def test_weight_update():

    engine = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryAutonomousEvolutionStrategyAutonomousOptimizationEngine()
    )


    engine.register_strategy(
        "trend",
        {}
    )


    result = engine.optimize_weight(
        "trend",
        "momentum_weight",
        0.8
    )


    assert result["score"] == 0.8



def test_get_parameters():

    engine = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryAutonomousEvolutionStrategyAutonomousOptimizationEngine()
    )


    engine.register_strategy(
        "x",
        {
            "a":0.1
        }
    )


    result = engine.get_parameters(
        "x"
    )


    assert result["a"] == 0.1