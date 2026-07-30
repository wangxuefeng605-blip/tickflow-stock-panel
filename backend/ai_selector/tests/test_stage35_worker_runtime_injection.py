from core.scanner.worker_runtime import WorkerRuntimeInjection


def test_worker_runtime_injection():

    runtime = WorkerRuntimeInjection()

    result = runtime.execute(
        {
            "code": "000001",
            "momentum": 0.8
        }
    )

    assert result["worker_runtime_completed"]