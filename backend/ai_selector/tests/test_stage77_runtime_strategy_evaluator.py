from core.runtime_strategy_evaluator import RuntimeStrategyEvaluator


def test_runtime_strategy_evaluator():

    evaluator = RuntimeStrategyEvaluator()


    result = evaluator.evaluate(
        {
            "version":1
        }
    )


    assert result["accepted"] is True

    assert result["strategy_score"] == 1