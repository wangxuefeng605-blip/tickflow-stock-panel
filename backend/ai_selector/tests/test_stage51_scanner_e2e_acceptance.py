from core.scanner.runtime_integration import ScannerRuntimeIntegration


def test_scanner_e2e_acceptance():

    runtime = ScannerRuntimeIntegration()

    result = runtime.run(
        {
            "code": "000001",
            "momentum": 0.8
        }
    )

    assert result["runtime_ready"] is True
    assert result["worker_execution_completed"] is True