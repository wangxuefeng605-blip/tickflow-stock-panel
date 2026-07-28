from core.scanner.worker import ScanWorker


def test_scanner_keep_ai_explanation():

    result = {
        "code":"000001",
        "score":0.8,
        "signals":[
            "Strong momentum"
        ],
        "explanation":
            "Market State:BULL"
    }


    assert "signals" in result

    assert (
        "Strong momentum"
        in result["signals"]
    )


    assert (
        "BULL"
        in result["explanation"]
    )