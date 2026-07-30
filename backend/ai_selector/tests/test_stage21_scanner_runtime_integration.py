def test_scanner_runtime_integration():

    adapter = ScannerLearningRuntimeAdapter()

    result = adapter.process(
        {
            "code":"000001",
            "momentum":0.8
        }
    )

    assert result["pipeline_completed"]