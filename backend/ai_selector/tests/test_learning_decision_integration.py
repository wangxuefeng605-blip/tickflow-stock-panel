from core.intelligence.decision_engine import AIDecisionEngine
from core.intelligence.context import AIContext


engine = AIDecisionEngine()


def test_decision_uses_learning_weight():

    ranking = {
        "code":"000001",
        "score":0.8,
        "weight":0.6,
        "confidence":0.8
    }


    context = AIContext(
        market_state="BULL"
    )


    decision = engine.decide(
        ranking,
        context
    )


    assert decision.weight == 0.6