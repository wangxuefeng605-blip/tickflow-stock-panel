from core.scanner.runtime_integration import ScannerRuntimeIntegration


def test_production_runtime_acceptance():

    runtime = ScannerRuntimeIntegration()

    result = runtime.run(
        {
            "code": "000001"
        }
    )

    assert result["runtime_ready"]