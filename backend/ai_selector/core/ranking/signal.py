def detect_signals(factors):

    signals = []


    if factors.get("momentum",0) > 0.7:
        signals.append(
            "strong_momentum"
        )


    if factors.get("trend",0) > 0.7:
        signals.append(
            "trend_up"
        )


    return signals