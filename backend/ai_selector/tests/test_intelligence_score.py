from core.ranking.intelligence_score import IntelligenceScorer


def test_bull_high_confidence():

    result = IntelligenceScorer().calculate(
        0.8,
        "BULL",
        1.0
    )

    assert result["intelligence_score"] > 0.8



def test_bear_penalty():

    result = IntelligenceScorer().calculate(
        0.8,
        "BEAR",
        1.0
    )

    assert result["intelligence_score"] < 0.8