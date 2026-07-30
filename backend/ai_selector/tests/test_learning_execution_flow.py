from core.intelligence.decision_types import AIDecision
from core.execution.executor import Executor


def test_learning_decision_to_execution():


    decision = AIDecision(

        code="000001",

        action="BUY",

        confidence=0.8,

        score=0.9,

        reason="learning",

        weight=0.6
    )


    order = Executor().execute(
        decision
    )


    assert order.code == "000001"

    assert order.action == "BUY"

    assert order.confidence == 0.8