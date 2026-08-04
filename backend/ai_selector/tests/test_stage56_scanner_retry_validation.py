from core.scanner.runtime_integration import ScannerRuntimeIntegration


def test_scanner_retry_validation():

    runtime = ScannerRuntimeIntegration()

    result = runtime.execute(
        {
            "code": "000001",
            "simulate_failure": True
        }
    )

    assert result is not None
    assert result["worker_execution_completed"] is True