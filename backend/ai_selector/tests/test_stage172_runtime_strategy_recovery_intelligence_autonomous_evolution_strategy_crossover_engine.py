from core.runtime_strategy_recovery_intelligence_autonomous_evolution_strategy_crossover_engine import (
    RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionStrategyCrossoverEngine
)



def test_strategy_crossover():

    engine = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionStrategyCrossoverEngine()
    )


    result = engine.crossover(
        "adaptive_restore",
        "risk_control"
    )


    assert result["child"] == (
        "adaptive_restore_risk_control_hybrid"
    )

    assert result["crossover"] is True



def test_candidate_combination():

    engine = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionStrategyCrossoverEngine()
    )


    result = engine.combine_candidates(
        [
            "strategy_a",
            "strategy_b"
        ]
    )


    assert result["child"] == (
        "strategy_a_strategy_b_hybrid"
    )



def test_lineage_tracking():

    engine = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionStrategyCrossoverEngine()
    )


    engine.crossover(
        "a",
        "b"
    )


    lineage = engine.get_lineage()


    assert lineage[0]["from"] == [
        "a",
        "b"
    ]



def test_crossover_history():

    engine = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionStrategyCrossoverEngine()
    )


    engine.crossover(
        "a",
        "b"
    )


    assert len(
        engine.get_history()
    ) == 1