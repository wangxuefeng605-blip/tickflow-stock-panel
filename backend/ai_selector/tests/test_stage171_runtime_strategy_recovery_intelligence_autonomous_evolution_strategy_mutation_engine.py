from core.runtime_strategy_recovery_intelligence_autonomous_evolution_strategy_mutation_engine import (
    RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionStrategyMutationEngine
)



def test_strategy_mutation():

    engine = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionStrategyMutationEngine()
    )


    result = engine.mutate(
        "adaptive_restore"
    )


    assert result["child"] == "adaptive_restore_mutated"
    assert result["mutation"] is True



def test_elite_preservation():

    engine = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionStrategyMutationEngine()
    )


    result = engine.preserve_elite(
        [
            {
                "strategy": "a",
                "fitness": 0.5
            },
            {
                "strategy": "b",
                "fitness": 0.9
            }
        ]
    )


    assert result["strategy"] == "b"



def test_lineage_tracking():

    engine = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionStrategyMutationEngine()
    )


    engine.mutate(
        "restore"
    )


    lineage = engine.get_lineage()


    assert lineage[0]["from"] == "restore"
    assert lineage[0]["to"] == "restore_mutated"



def test_mutation_history():

    engine = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionStrategyMutationEngine()
    )


    engine.mutate(
        "test"
    )


    assert len(
        engine.get_history()
    ) == 1