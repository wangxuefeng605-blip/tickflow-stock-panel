from core.scanner.runtime_integration import ScannerRuntimeIntegration


def test_production_runtime_full_loop():

    runtime = ScannerRuntimeIntegration()


    result = runtime.run(
        {
            "code": "000001",
            "momentum": 0.8,
            "trend": 0.7
        }
    )


    assert result["runtime_ready"]

    assert result["worker_execution_completed"]

    assert result["scanner_runtime_completed"]

    assert result["input"]["code"] == "000001"