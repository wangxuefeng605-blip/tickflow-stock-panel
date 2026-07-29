from core.ranking.signal import detect_signals


def test_signal_detection():

    factors = {

        "momentum":0.1,

        "trend":1,

        "volume_factor":1.5
    }


    signals = detect_signals(
        factors
    )


    assert len(signals) > 0