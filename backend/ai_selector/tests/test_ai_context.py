from core.intelligence.context import AIContext


def test_ai_context():

    ctx = AIContext(
        market_state="BULL",
        weights={
            "momentum":0.35
        }
    )


    assert ctx.market_state=="BULL"

    assert (
        ctx.weights["momentum"]
        ==
        0.35
    )