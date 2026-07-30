from core.intelligence.decision_types import AIDecision


def test_learning_execution_integration():

    decision = AIDecision(
        code="000001",
        action="BUY",
        confidence=0.8,
        score=0.8,
        reason="test",
        weight=0.6
    )

    ...