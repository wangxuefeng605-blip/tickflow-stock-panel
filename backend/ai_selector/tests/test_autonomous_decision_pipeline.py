from core.decision.autonomous_decision_pipeline import (
    AutonomousDecisionPipeline
)


def test_autonomous_decision_pipeline():

    pipeline = AutonomousDecisionPipeline()


    result = pipeline.run(
        {
            "market":"BULL",
            "confidence":0.85,
            "market_score":0.8,
            "risk":0.1
        }
    )


    assert result["decision"] == "SELECT"

    assert result["level"] == "HIGH"