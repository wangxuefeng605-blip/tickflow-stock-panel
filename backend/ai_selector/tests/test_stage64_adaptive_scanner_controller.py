from core.adaptive_scanner_controller import AdaptiveScannerController


def test_adaptive_scanner_controller():

    controller = AdaptiveScannerController()


    result = controller.decide(
        {
            "runtime_status": "READY"
        }
    )


    assert result["scanner_mode"] == "NORMAL"

    assert result["workers"] == 8