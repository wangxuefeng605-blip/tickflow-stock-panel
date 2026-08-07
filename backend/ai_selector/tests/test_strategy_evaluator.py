from core.strategy.strategy_evaluator import StrategyEvaluator


def test_strategy_evaluator():

    evaluator = StrategyEvaluator()


    result = evaluator.evaluate(
        {
            "return":0.15,
            "risk":0.2,
            "win_rate":0.65
        }
    )


    assert result["score"] > 0

    assert result["level"] == "GOOD"