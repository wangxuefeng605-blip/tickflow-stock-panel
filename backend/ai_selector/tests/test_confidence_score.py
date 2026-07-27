from core.intelligence.ai_score import calculate_ai_score


def test_confidence_changes_score():

    factors = {
        "momentum": 1.0,
        "trend": 1.0
    }


    weights = {
        "momentum": 0.5,
        "trend": 0.5
    }


    high_confidence = calculate_ai_score(
        factors,
        weights,
        confidence=1.0
    )


    low_confidence = calculate_ai_score(
        factors,
        weights,
        confidence=0.5
    )


    assert low_confidence < high_confidence