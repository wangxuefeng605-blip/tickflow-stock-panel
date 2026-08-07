from core.decision.decision_context import DecisionContext


def test_decision_context():

    ctx = DecisionContext(
        {
            "market":"BULL",
            "confidence":0.8
        }
    )


    assert ctx.market == "BULL"

    assert ctx.confidence == 0.8