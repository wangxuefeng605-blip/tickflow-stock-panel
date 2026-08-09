from core.decision.realtime_decision import (
    RealtimeDecisionEngine
)


def test_realtime_decision():

    engine = RealtimeDecisionEngine()


    result = engine.decide(
        {
            "code":"000001",
            "score":85
        }
    )


    assert result["action"]=="BUY"