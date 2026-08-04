import time

from core.scanner.runtime_integration import ScannerRuntimeIntegration


def test_runtime_benchmark():

    runtime = ScannerRuntimeIntegration()

    start = time.time()

    result = runtime.run(
        {
            "code": "000001",
            "momentum": 0.8
        }
    )

    elapsed = time.time() - start

    assert result["runtime_ready"] is True
    assert result["worker_execution_completed"] is True

    assert elapsed < 1.0