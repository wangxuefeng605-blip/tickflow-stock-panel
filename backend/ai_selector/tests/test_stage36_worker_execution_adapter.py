from core.scanner.worker_execution_adapter import WorkerExecutionAdapter


def test_worker_execution_adapter():

    adapter = WorkerExecutionAdapter()

    result = adapter.execute(
        {
            "code": "000001",
            "momentum": 0.8
        }
    )

    assert result["worker_execution_completed"]