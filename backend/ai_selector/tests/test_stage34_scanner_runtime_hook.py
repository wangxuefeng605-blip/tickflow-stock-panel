from core.scanner.runtime_hook import ScannerRuntimeHook


def test_scanner_runtime_hook():

    hook = ScannerRuntimeHook()

    result = hook.execute(
        {
            "code": "000001",
            "momentum": 0.8
        }
    )

    assert result["runtime_hook_completed"]