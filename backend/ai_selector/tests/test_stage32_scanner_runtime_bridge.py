from core.scanner.runtime_bridge import RuntimeBridge


def test_scanner_runtime_bridge():

    bridge = RuntimeBridge()


    result = bridge.execute(
        {
            "code":"000001",
            "momentum":0.8
        }
    )


    assert result["runtime_completed"]
    assert result["bridge_completed"]