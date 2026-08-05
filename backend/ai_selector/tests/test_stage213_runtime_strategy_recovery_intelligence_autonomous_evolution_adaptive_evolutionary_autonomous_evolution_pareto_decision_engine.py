from core.runtime_strategy_recovery_intelligence_autonomous_evolution_adaptive_evolutionary_autonomous_evolution_pareto_decision_engine import (
    RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryAutonomousEvolutionParetoDecisionEngine
)



def test_add_candidate():

    engine = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryAutonomousEvolutionParetoDecisionEngine()
    )


    result = engine.add_candidate(
        "strategy_a",
        0.9,
        0.1,
        0.8
    )


    assert result["name"] == "strategy_a"



def test_pareto_frontier():

    engine = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryAutonomousEvolutionParetoDecisionEngine()
    )


    engine.add_candidate(
        "weak",
        0.5,
        0.5,
        0.5
    )


    engine.add_candidate(
        "strong",
        0.9,
        0.1,
        0.9
    )


    result = engine.pareto_frontier()


    assert len(result) == 1

    assert result[0]["name"] == "strong"



def test_select_best():

    engine = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryAutonomousEvolutionParetoDecisionEngine()
    )


    engine.add_candidate(
        "a",
        0.8,
        0.2,
        0.7
    )


    engine.add_candidate(
        "b",
        0.9,
        0.1,
        0.9
    )


    result = engine.select_best()


    assert result["name"] == "b"



def test_history():

    engine = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryAutonomousEvolutionParetoDecisionEngine()
    )


    engine.add_candidate(
        "test",
        1,
        0,
        1
    )


    assert len(
        engine.get_history()
    ) == 1