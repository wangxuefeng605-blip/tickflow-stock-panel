from core.meta.meta_evaluator import MetaEvaluator



def test_meta_evaluator():


    evaluator = MetaEvaluator()


    result = evaluator.evaluate(
        0.5,
        0.8
    )


    assert result["should_keep"] is True

    assert result["improvement"] == 0.3