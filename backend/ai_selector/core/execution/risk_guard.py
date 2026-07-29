def risk_check(
    decision
):

    confidence = decision.get(
        "confidence",
        0
    )


    if confidence < 0.4:
        return False


    return True