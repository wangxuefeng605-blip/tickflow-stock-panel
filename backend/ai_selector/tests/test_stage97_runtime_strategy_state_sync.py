from core.runtime_strategy_state_sync import (
    RuntimeStrategyStateSynchronizer
)


def test_runtime_strategy_state_sync():

    sync = RuntimeStrategyStateSynchronizer()

    result = sync.sync(
        {
            "momentum_weight": 0.35,
            "trend_weight": 0.30
        }
    )

    assert result["synced"] is True

    assert result["state"]["momentum_weight"] == 0.35
    assert result["state"]["trend_weight"] == 0.30


def test_runtime_strategy_state_persist():

    sync = RuntimeStrategyStateSynchronizer()

    sync.sync(
        {
            "risk_weight": 0.1
        }
    )

    state = sync.get_state()

    assert state["risk_weight"] == 0.1