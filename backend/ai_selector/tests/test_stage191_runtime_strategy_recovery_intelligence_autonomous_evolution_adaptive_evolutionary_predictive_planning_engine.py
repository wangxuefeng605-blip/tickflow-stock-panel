from core.runtime_strategy_recovery_intelligence_autonomous_evolution_adaptive_evolutionary_predictive_planning_engine import (
    RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryPredictivePlanningEngine
)



def test_high_fitness_plan():

    engine = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryPredictivePlanningEngine()
    )


    result = engine.create_plan(
        {
            "fitness": 0.9
        }
    )


    assert result["direction"] == "optimize_existing"



def test_low_fitness_plan():

    engine = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryPredictivePlanningEngine()
    )


    result = engine.create_plan(
        {
            "fitness": 0.2
        }
    )


    assert result["direction"] == "explore_new"



def test_middle_plan():

    engine = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryPredictivePlanningEngine()
    )


    result = engine.create_plan(
        {
            "fitness": 0.5
        }
    )


    assert result["direction"] == "balanced_evolution"



def test_plan_history():

    engine = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryPredictivePlanningEngine()
    )


    engine.create_plan(
        {
            "fitness": 1
        }
    )


    assert len(
        engine.get_history()
    ) == 1