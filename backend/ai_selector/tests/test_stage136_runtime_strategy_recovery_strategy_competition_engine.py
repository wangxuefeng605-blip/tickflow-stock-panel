from core.runtime_strategy_recovery_strategy_competition_engine import (
    RuntimeStrategyRecoveryStrategyCompetitionEngine
)



def test_strategy_competition():

    engine = (
        RuntimeStrategyRecoveryStrategyCompetitionEngine()
    )


    result = engine.compete(
        {
            "restore":0.9,
            "fallback":0.5
        }
    )


    assert result["restore"] == 0.9



def test_strategy_champion():

    engine = (
        RuntimeStrategyRecoveryStrategyCompetitionEngine()
    )


    engine.compete(
        {
            "restore":0.9,
            "fallback":0.5
        }
    )


    engine.compete(
        {
            "restore":0.8,
            "fallback":0.6
        }
    )


    assert (
        engine.champion()
        ==
        "restore"
    )



def test_strategy_competition_history():

    engine = (
        RuntimeStrategyRecoveryStrategyCompetitionEngine()
    )


    engine.compete(
        {
            "restore":1.0
        }
    )


    assert len(
        engine.history()
    ) == 1