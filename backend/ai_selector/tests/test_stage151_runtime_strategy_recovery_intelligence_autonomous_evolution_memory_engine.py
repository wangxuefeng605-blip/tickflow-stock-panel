from core.runtime_strategy_recovery_intelligence_autonomous_evolution_memory_engine import (
    RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionMemoryEngine
)



def test_memory_success_record():

    engine = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionMemoryEngine()
    )


    result = engine.record(
        {
            "version": 1,
            "fitness": 0.8
        }
    )


    assert result["fitness"] == 0.8
    assert len(
        engine.get_success_history()
    ) == 1



def test_memory_failure_record():

    engine = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionMemoryEngine()
    )


    engine.record(
        {
            "version": 2,
            "fitness": 0.2
        }
    )


    assert len(
        engine.get_failure_history()
    ) == 1



def test_best_memory():

    engine = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionMemoryEngine()
    )


    engine.record(
        {
            "version": 1,
            "fitness": 0.6
        }
    )


    engine.record(
        {
            "version": 2,
            "fitness": 0.9
        }
    )


    result = engine.get_best_memory()


    assert result["version"] == 2
    assert result["fitness"] == 0.9



def test_memory_history():

    engine = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionMemoryEngine()
    )


    engine.record(
        {
            "version": 1,
            "fitness": 0.7
        }
    )


    assert len(
        engine.get_history()
    ) == 1