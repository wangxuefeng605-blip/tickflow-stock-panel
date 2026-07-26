def detect_signals(factors):

    signals = []

    momentum = factors.get(
        "momentum",
        0
    )

    trend = factors.get(
        "trend",
        0
    )

    volume = factors.get(
        "volume_factor",
        0
    )


    if momentum > 0.05:

        signals.append(
            "strong_momentum"
        )


    if trend > 0:

        signals.append(
            "trend_up"
        )


    if volume > 1.2:

        signals.append(
            "volume_breakout"
        )


    return signals