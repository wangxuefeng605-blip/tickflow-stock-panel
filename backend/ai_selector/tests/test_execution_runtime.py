from core.execution.runtime import ExecutionRuntime


def test_execution_runtime():

    runtime = ExecutionRuntime()


    result = runtime.execute(
        {
            "code":"000533",
            "action":"BUY",
            "confidence":0.8
        }
    )


    assert result.code=="000533"
    assert result.action=="BUY"