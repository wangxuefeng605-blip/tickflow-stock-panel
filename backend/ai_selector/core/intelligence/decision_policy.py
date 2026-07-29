def decide_action(
    score,
    confidence,
    market_state
):

    if confidence < 0.3:
        return "AVOID"


    if market_state == "BEAR":

        if score > 0.7:
            return "BUY"

        if score > 0.4:
            return "HOLD"

        return "REDUCE"


    else:

        if score > 0.6:
            return "BUY"

        if score > 0.35:
            return "HOLD"

        return "REDUCE"