"""
AI Ranking Score Engine
v18.6
"""


def ranking_score(item):

    score = item.score


    # AI confidence boost

    confidence = getattr(
        item,
        "confidence",
        0
    )


    score += confidence * 0.05



    # signal bonus

    signals = getattr(
        item,
        "signals",
        []
    )


    score += len(signals) * 0.01



    # market adjustment

    explanation = getattr(
        item,
        "explanation",
        {}
    )


    if isinstance(explanation, dict):

        state = explanation.get(
            "market_state",
            ""
        )


        if state == "BULL":
            score += 0.03


        elif state == "BEAR":
            score -= 0.03



    return round(
        score,
        6
    )