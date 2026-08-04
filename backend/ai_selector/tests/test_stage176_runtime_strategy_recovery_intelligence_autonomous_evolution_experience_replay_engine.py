from core.runtime_strategy_recovery_intelligence_autonomous_evolution_experience_replay_engine import (
    RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionExperienceReplayEngine
)



def test_store_experience():

    engine = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionExperienceReplayEngine()
    )


    result = engine.store(
        {
            "strategy": "adaptive_restore",
            "fitness": 0.8
        }
    )


    assert result["strategy"] == "adaptive_restore"
    assert len(
        engine.get_memory()
    ) == 1



def test_replay_best_experience():

    engine = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionExperienceReplayEngine()
    )


    engine.store(
        {
            "strategy": "a",
            "fitness": 0.5
        }
    )


    engine.store(
        {
            "strategy": "b",
            "fitness": 0.9
        }
    )


    result = engine.replay()


    assert result["replayed_strategy"] == "b"
    assert result["fitness"] == 0.9



def test_empty_replay():

    engine = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionExperienceReplayEngine()
    )


    assert engine.replay() is None



def test_replay_history():

    engine = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionExperienceReplayEngine()
    )


    engine.store(
        {
            "strategy": "test",
            "fitness": 1
        }
    )


    engine.replay()


    assert len(
        engine.get_history()
    ) == 2