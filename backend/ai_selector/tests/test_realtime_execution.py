from core.execution.realtime_executor import (
    RealtimeExecutor
)


def test_realtime_execution():

    executor = RealtimeExecutor()

    result = executor.execute(
        {
            "action":"BUY",
            "code":"000001"
        }
    )

    assert result["status"] == "EXECUTED"