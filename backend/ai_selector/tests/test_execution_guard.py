from core.execution.execution_guard import ExecutionGuard


def test_execution_guard():

    guard = ExecutionGuard()


    result = guard.check(
        {
            "action": "BUY",
            "symbol": "000001",
            "confidence": 0.9,
            "risk": 0.1
        }
    )


    assert result["allowed"] is True

    assert result["reason"] == "PASS"