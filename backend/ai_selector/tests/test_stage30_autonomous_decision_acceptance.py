from core.decision.autonomous_decision_pipeline import (
    AutonomousDecisionPipeline
)


def test_stage30_full_autonomous_decision():

    pipeline = AutonomousDecisionPipeline()


    result = pipeline.run(
        {
            "market":"BULL",
            "confidence":0.9,
            "market_score":0.85,
            "risk":0.1
        }
    )


    assert result["decision"] == "SELECT"

    assert result["level"] == "HIGH"