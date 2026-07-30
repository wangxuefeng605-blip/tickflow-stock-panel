from core.scanner.runtime_executor import RuntimeExecutor


def test_runtime_executor():

    executor = RuntimeExecutor()

    result = executor.execute(
        {
            "code": "000001",
            "momentum": 0.8
        }
    )

    assert result["runtime_completed"]