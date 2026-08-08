from core.meta.meta_state import MetaState



def test_meta_state():


    state = MetaState()


    state.record_cycle(
        True
    )


    state.record_cycle(
        False
    )


    state.update_best_strategy(
        "momentum_v2"
    )


    result = state.snapshot()


    assert result["cycles"] == 2

    assert result["optimizations"] == 1

    assert result["best_strategy"] == "momentum_v2"

    assert result["success_rate"] == 0.5