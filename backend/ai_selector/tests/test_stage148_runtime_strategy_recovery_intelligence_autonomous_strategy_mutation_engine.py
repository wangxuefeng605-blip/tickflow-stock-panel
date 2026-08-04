from core.runtime_strategy_recovery_intelligence_autonomous_strategy_mutation_engine import (
    RuntimeStrategyRecoveryIntelligenceAutonomousStrategyMutationEngine
)



def test_strategy_mutation():

    engine = (
        RuntimeStrategyRecoveryIntelligenceAutonomousStrategyMutationEngine()
    )


    result = engine.mutate(
        {
            "version": 1,
            "fitness": 0.8
        }
    )


    assert result["parent"] == 1
    assert result["fitness"] == 0.88
    assert result["mutation"] == 0.08



def test_strategy_mutation_version():

    engine = (
        RuntimeStrategyRecoveryIntelligenceAutonomousStrategyMutationEngine()
    )


    result = engine.mutate(
        {
            "version": 5,
            "fitness": 0.5
        }
    )


    assert result["version"] == 1



def test_strategy_mutation_history():

    engine = (
        RuntimeStrategyRecoveryIntelligenceAutonomousStrategyMutationEngine()
    )


    engine.mutate(
        {
            "version": 1,
            "fitness": 0.7
        }
    )


    assert len(
        engine.get_history()
    ) == 1