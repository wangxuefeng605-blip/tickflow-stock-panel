from core.runtime_strategy_recovery_intelligence_prediction_engine import (
    RuntimeStrategyRecoveryIntelligencePredictionEngine
)



def test_prediction_update():

    engine = (
        RuntimeStrategyRecoveryIntelligencePredictionEngine()
    )


    result = engine.update(
        {
            "restore": {
                "success_rate": 0.9
            }
        }
    )


    assert result["updated"] is True



def test_prediction_best_policy():

    engine = (
        RuntimeStrategyRecoveryIntelligencePredictionEngine()
    )


    engine.update(
        {
            "restore": {
                "success_rate": 0.9
            },
            "fallback": {
                "success_rate": 0.5
            }
        }
    )


    result = engine.predict()


    assert result["policy"] == "restore"
    assert result["probability"] == 0.9



def test_prediction_empty():

    engine = (
        RuntimeStrategyRecoveryIntelligencePredictionEngine()
    )


    result = engine.predict()


    assert result["policy"] is None