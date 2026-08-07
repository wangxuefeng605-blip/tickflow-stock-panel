from core.strategy.strategy_state import StrategyState


def test_strategy_state():

    state = StrategyState()

    state.update(
        {
            "strategy":"trend_follow",
            "market":"bull",
            "performance":0.15
        }
    )


    result = state.snapshot()


    assert result["strategy"]=="trend_follow"

    assert result["performance"]==0.15