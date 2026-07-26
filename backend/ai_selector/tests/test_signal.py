def test_signal_detection():

    factors = {

        "momentum":0.1,

        "trend":1,

        "volume_factor":1.5
    }


    signals = detect_signals(
        factors
    )


    assert "strong_momentum" in signals
    assert "trend_up" in signals
    assert "volume_breakout" in signals