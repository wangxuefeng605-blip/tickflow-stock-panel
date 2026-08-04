from core.runtime_strategy_recovery_intelligence_experience_replay_engine import (
    RuntimeStrategyRecoveryIntelligenceExperienceReplayEngine
)



def test_experience_replay_store():

    engine = (
        RuntimeStrategyRecoveryIntelligenceExperienceReplayEngine()
    )


    result = engine.store(
        {
            "policy": "restore",
            "success": True
        }
    )


    assert result["stored"] is True



def test_experience_replay_match():

    engine = (
        RuntimeStrategyRecoveryIntelligenceExperienceReplayEngine()
    )


    engine.store(
        {
            "policy": "restore",
            "success": True,
            "score": 0.9
        }
    )


    result = engine.replay(
        "restore"
    )


    assert result["success"] is True



def test_experience_replay_history():

    engine = (
        RuntimeStrategyRecoveryIntelligenceExperienceReplayEngine()
    )


    engine.store(
        {
            "policy": "fallback"
        }
    )


    assert len(
        engine.get_history()
    ) == 1