from core.intelligence.ai_score import AIScoreEngine


def test_confidence_changes_score():

    engine = AIScoreEngine()


    factors = {
        "momentum": 1.0,
        "trend": 1.0
    }


    weights = {
        "momentum": 0.5,
        "trend": 0.5
    }


    class Context:

        confidence = 1.0


    high = engine.calculate(
        factors,
        weights,
        Context()
    )


    Context.confidence = 0.5


    low = engine.calculate(
        factors,
        weights,
        Context()
    )


    assert low < high