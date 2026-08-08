from core.evolution.strategy_mutation import StrategyMutation


def test_strategy_mutation():

    engine = StrategyMutation()

    result = engine.mutate(
        {
            "strategy": "trend",
            "score": 0.91
        }
    )

    assert result["strategy"] == "trend"
    assert result["mutation"] == "increase_weight"