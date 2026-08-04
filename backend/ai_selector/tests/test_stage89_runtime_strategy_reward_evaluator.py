from core.runtime_strategy_reward_evaluator import RuntimeStrategyRewardEvaluator


def test_runtime_strategy_reward_evaluator():

    evaluator = RuntimeStrategyRewardEvaluator()


    result = evaluator.evaluate(
        [
            1,
            1,
            0
        ]
    )


    assert result["keep"] is True