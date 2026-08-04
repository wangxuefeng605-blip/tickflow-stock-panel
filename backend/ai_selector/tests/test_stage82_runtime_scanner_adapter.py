from core.runtime_scanner_adapter import RuntimeScannerAdapter


def test_runtime_scanner_adapter():

    adapter = RuntimeScannerAdapter()


    result = adapter.bind(
        {
            "strategy":"momentum_v2",
            "weight":0.8
        }
    )


    assert result["bound"] is True

    assert adapter.get_strategy()["strategy"] == "momentum_v2"