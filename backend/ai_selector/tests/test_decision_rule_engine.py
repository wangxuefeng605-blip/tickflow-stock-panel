from core.decision.decision_context import DecisionContext
from core.decision.decision_rule_engine import DecisionRuleEngine


def test_decision_rule_engine():

    context = DecisionContext(
        {
            "market": "BULL",
            "confidence": 0.85
        }
    )


    engine = DecisionRuleEngine()


    result = engine.evaluate(
        context
    )


    assert result["action"] == "SELECT"

    assert result["confidence"] == 0.85