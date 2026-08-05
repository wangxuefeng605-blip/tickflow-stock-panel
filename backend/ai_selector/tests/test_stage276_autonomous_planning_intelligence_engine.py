from core.runtime_strategy_recovery_intelligence_autonomous_evolution_adaptive_evolutionary_autonomous_evolution_strategy_evolution_autonomous_planning_intelligence_engine import (
    RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryAutonomousEvolutionStrategyEvolutionAutonomousPlanningIntelligenceEngine
)



def test_goal():

    engine = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryAutonomousEvolutionStrategyEvolutionAutonomousPlanningIntelligenceEngine()
    )


    result = engine.create_goal(
        "maximize_alpha",
        10
    )


    assert result["name"] == "maximize_alpha"



def test_plan():

    engine = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryAutonomousEvolutionStrategyEvolutionAutonomousPlanningIntelligenceEngine()
    )


    goal = engine.create_goal(
        "optimize_strategy"
    )


    engine.add_action(
        "increase_weight",
        "momentum"
    )


    result = engine.generate_plan(
        goal
    )


    assert len(result["steps"]) == 1



def test_optimize():

    engine = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryAutonomousEvolutionStrategyEvolutionAutonomousPlanningIntelligenceEngine()
    )


    engine.plans.append(
        {
            "steps":[1,2]
        }
    )


    result = engine.optimize_plan()


    assert len(result["steps"]) == 2