from core.scanner.runtime_integration import ScannerRuntimeIntegration


def test_scanner_production_release():

    runtime = ScannerRuntimeIntegration()


    result = runtime.run(
        {
            "code": "000001",
            "momentum": 0.8,
            "trend": 0.7
        }
    )


    assert result["runtime_ready"] is True

    assert result["worker_execution_completed"] is True

    assert result["input"]["code"] == "000001"