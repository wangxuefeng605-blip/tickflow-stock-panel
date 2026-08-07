from core.runtime.decision_engine import (
    RuntimeDecisionEngine
)


def test_runtime_continue():

    engine = RuntimeDecisionEngine()

    result = engine.decide(
        {
            "components": {
                "scanner": "OK",
                "ranking": "OK"
            },
            "errors": []
        }
    )

    assert result["action"] == "CONTINUE"



def test_runtime_recovery():

    engine = RuntimeDecisionEngine()

    result = engine.decide(
        {
            "components": {
                "learning": "ERROR"
            },
            "errors": [
                "learning failed"
            ]
        }
    )

    assert (
        result["action"]
        ==
        "RECOVER_LEARNING"
    )