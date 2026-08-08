from core.learning.strategy_adjuster import StrategyAdjuster


def test_strategy_adjuster():

    adjuster = StrategyAdjuster()

    result = adjuster.adjust(
        {
            "feedback": "positive"
        }
    )

    assert result["momentum"] > 0.35
    assert result["trend"] > 0.30