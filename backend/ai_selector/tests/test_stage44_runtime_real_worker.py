from core.scanner.runtime_integration import ScannerRuntimeIntegration


def test_runtime_worker_execution():

    runtime = ScannerRuntimeIntegration()

    result = runtime.execute(
        {
            "code": "000001"
        }
    )

    assert result["worker_execution_completed"]