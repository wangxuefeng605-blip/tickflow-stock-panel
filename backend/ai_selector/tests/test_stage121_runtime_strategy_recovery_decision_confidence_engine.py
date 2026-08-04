from core.runtime_strategy_recovery_decision_confidence_engine import (
    RuntimeStrategyRecoveryDecisionConfidenceEngine
)


def test_runtime_strategy_confidence_calculation():

    engine = (
        RuntimeStrategyRecoveryDecisionConfidenceEngine()
    )


    result = engine.evaluate(
        {
            "restore": {
                "score": 0.9
            },
            "fallback": {
                "score": 0.5
            }
        }
    )


    assert result["selected_policy"] == "restore"
    assert result["confidence"] == 0.4



def test_runtime_strategy_high_confidence():

    engine = (
        RuntimeStrategyRecoveryDecisionConfidenceEngine()
    )


    result = engine.evaluate(
        {
            "rollback": {
                "score": 1
            }
        }
    )


    assert result["confidence"] == 1



def test_runtime_strategy_confidence_history():

    engine = (
        RuntimeStrategyRecoveryDecisionConfidenceEngine()
    )


    engine.evaluate(
        {
            "restore": {
                "score": 0.8
            }
        }
    )


    assert len(
        engine.get_history()
    ) == 1