from core.adaptive.adaptive_state import AdaptiveState
from core.adaptive.strategy_adapter import StrategyAdapter



def test_strategy_adapter():


    state = AdaptiveState()

    state.adjust_strategy()


    adapter = StrategyAdapter(
        state
    )


    result = adapter.apply(
        "momentum"
    )


    assert result["strategy"] == "momentum"

    assert result["version"] == 2

    assert result["adaptive"] is True