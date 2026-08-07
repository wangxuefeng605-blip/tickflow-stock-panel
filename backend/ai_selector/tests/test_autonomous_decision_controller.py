from core.decision.autonomous_decision_controller import (
    AutonomousDecisionController
)


def test_autonomous_decision_controller():

    controller = AutonomousDecisionController()


    result = controller.decide(
        {
            "market":"BULL",
            "confidence":0.85,
            "market_score":0.8,
            "risk":0.1
        }
    )


    assert result["action"] == "SELECT"

    assert result["level"] == "HIGH"