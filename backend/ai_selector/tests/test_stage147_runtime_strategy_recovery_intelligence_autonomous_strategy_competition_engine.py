from core.runtime_strategy_recovery_intelligence_autonomous_strategy_competition_engine import (
    RuntimeStrategyRecoveryIntelligenceAutonomousStrategyCompetitionEngine
)



def test_strategy_competition_winner():

    engine = (
        RuntimeStrategyRecoveryIntelligenceAutonomousStrategyCompetitionEngine()
    )


    engine.register(
        {
            "version": 1,
            "fitness": 0.5
        }
    )


    engine.register(
        {
            "version": 2,
            "fitness": 0.9
        }
    )


    result = engine.compete()


    assert result["winner"] == 2
    assert result["score"] == 0.9



def test_strategy_competition_empty():

    engine = (
        RuntimeStrategyRecoveryIntelligenceAutonomousStrategyCompetitionEngine()
    )


    result = engine.compete()


    assert result["winner"] is None
    assert result["score"] == 0



def test_strategy_competition_history():

    engine = (
        RuntimeStrategyRecoveryIntelligenceAutonomousStrategyCompetitionEngine()
    )


    engine.compete()


    assert len(
        engine.get_history()
    ) == 1