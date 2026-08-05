from core.runtime_strategy_recovery_intelligence_autonomous_evolution_adaptive_evolutionary_autonomous_evolution_strategy_evolution_self_optimization_engine import (
    RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryAutonomousEvolutionStrategyEvolutionSelfOptimizationEngine
)



def test_register():

    engine = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryAutonomousEvolutionStrategyEvolutionSelfOptimizationEngine()
    )


    result = engine.register_strategy(
        "momentum",
        {
            "weight":0.5
        }
    )


    assert result["registered"] is True



def test_update():

    engine = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryAutonomousEvolutionStrategyEvolutionSelfOptimizationEngine()
    )


    engine.register_strategy(
        "trend",
        {
            "risk":0.5
        }
    )


    result = engine.update_parameter(
        "trend",
        "risk",
        0.3
    )


    assert result["value"] == 0.3



def test_optimize_positive():

    engine = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryAutonomousEvolutionStrategyEvolutionSelfOptimizationEngine()
    )


    engine.register_strategy(
        "alpha",
        {
            "weight":1
        }
    )


    result = engine.optimize(
        "alpha",
        1
    )


    assert result["factor"] == 1.1



def test_optimize_negative():

    engine = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryAutonomousEvolutionStrategyEvolutionSelfOptimizationEngine()
    )


    engine.register_strategy(
        "beta",
        {
            "weight":1
        }
    )


    result = engine.optimize(
        "beta",
        -1
    )


    assert result["factor"] == 0.9