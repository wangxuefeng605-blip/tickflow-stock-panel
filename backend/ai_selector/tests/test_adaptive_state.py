from core.adaptive.adaptive_state import AdaptiveState



def test_adaptive_state():


    state = AdaptiveState()


    state.update_performance(
        0.85
    )


    state.adjust_strategy()


    result = state.snapshot()


    assert result["strategy_version"] == 2

    assert result["performance"] == 0.85

    assert result["adjustments"] == 1