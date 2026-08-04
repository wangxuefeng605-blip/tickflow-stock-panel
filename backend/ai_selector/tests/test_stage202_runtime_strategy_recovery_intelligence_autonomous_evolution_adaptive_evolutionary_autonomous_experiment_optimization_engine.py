from core.runtime_strategy_recovery_intelligence_autonomous_evolution_adaptive_evolutionary_autonomous_experiment_optimization_engine import (
    RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryAutonomousExperimentOptimizationEngine
)



def test_register_experiment():

    engine = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryAutonomousExperimentOptimizationEngine()
    )


    result = engine.register_experiment(
        "factor_test",
        10,
        50
    )


    assert result["name"] == "factor_test"



def test_select_best_experiment():

    engine = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryAutonomousExperimentOptimizationEngine()
    )


    engine.register_experiment(
        "slow",
        20,
        40
    )


    engine.register_experiment(
        "fast",
        5,
        30
    )


    result = engine.select_best_experiment()


    assert result["name"] == "fast"



def test_parameter_optimization():

    engine = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryAutonomousExperimentOptimizationEngine()
    )


    result = engine.optimize_parameters(
        {
            "window": 5
        }
    )


    assert result["optimized_parameters"]["window"] == 6



def test_experiment_history():

    engine = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryAutonomousExperimentOptimizationEngine()
    )


    engine.register_experiment(
        "test",
        1,
        1
    )


    assert len(
        engine.get_history()
    ) == 1