from core.runtime_strategy_state_storage import (
    RuntimeStrategyStateStorage
)


def test_runtime_strategy_state_save_load(tmp_path):

    file_path = (
        tmp_path /
        "strategy_state.json"
    )


    storage = RuntimeStrategyStateStorage(
        file_path
    )


    state = {
        "momentum_weight": 0.35,
        "trend_weight": 0.30,
        "risk_weight": 0.10
    }


    result = storage.save(state)


    assert result["saved"] is True


    loaded = storage.load()


    assert loaded["loaded"] is True

    assert loaded["state"]["momentum_weight"] == 0.35

    assert loaded["state"]["risk_weight"] == 0.10