from core.adaptive.adaptive_evaluator import AdaptiveEvaluator



def test_adaptive_evaluator():


    evaluator = AdaptiveEvaluator()


    result = evaluator.evaluate(
        0.9
    )


    assert result["level"] == "EXCELLENT"

    assert result["should_adjust"] is False