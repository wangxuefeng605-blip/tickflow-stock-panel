def allow_execution(
    decision
):

    confidence = decision.get(
        "confidence",
        0
    )


    action = decision.get(
        "decision",
        "HOLD"
    )


    if confidence < 0.5:
        return False


    if action not in [
        "BUY",
        "SELL"
    ]:
        return False


    return True