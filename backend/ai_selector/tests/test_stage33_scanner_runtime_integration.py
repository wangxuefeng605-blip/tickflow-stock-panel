from core.scanner.runtime_integration import ScannerRuntimeIntegration


def test_scanner_runtime_integration():

    runtime = ScannerRuntimeIntegration()

    result = runtime.execute(
        {
            "code": "000001",
            "momentum":0.8
        }
    )

    assert result["scanner_runtime_completed"]