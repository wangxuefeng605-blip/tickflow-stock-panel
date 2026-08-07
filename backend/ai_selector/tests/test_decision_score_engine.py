from core.decision.decision_score_engine import DecisionScoreEngine


def test_decision_score_engine():

    engine = DecisionScoreEngine()


    result = engine.score(
        {
            "market_score":0.8,
            "confidence":0.9,
            "risk":0.2
        }
    )


    assert result["score"] > 0

    assert result["level"] == "HIGH"