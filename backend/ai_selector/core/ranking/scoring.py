"""
AI Ranking Scoring Engine
v18.7

Responsible for:
- weighted score
- AI confidence boost
- market adjustment
- risk penalty
"""


def clamp(
    value,
    low=0,
    high=1
):
    return max(
        low,
        min(
            high,
            value
        )
    )



def factor_quality(
    factors
):

    if not factors:
        return 0


    values = []


    for key in [
        "momentum",
        "trend",
        "quality",
        "growth",
        "volume_factor"
    ]:

        if key in factors:

            values.append(
                factors[key]
            )


    if not values:
        return 0


    return sum(values) / len(values)



def market_bonus(
    market_state
):

    mapping = {

        "BULL": 1.10,

        "SIDEWAYS": 1.00,

        "BEAR": 0.90,

        "UNKNOWN": 1.00

    }


    return mapping.get(
        market_state,
        1.0
    )



def confidence_bonus(
    confidence
):

    return (
        1
        +
        confidence * 0.1
    )



def risk_penalty(
    risks
):

    if not risks:
        return 1


    return max(
        0.8,
        1 - len(risks)*0.05
    )



def calculate_rank_score(
    item
):

    """
    item:

    {
        score,
        factors,
        market_state,
        confidence,
        risks
    }

    """


    base_score = item.get(
        "score",
        0
    )


    factors = item.get(
        "factors",
        {}
    )


    ai_score = factor_quality(
        factors
    )


    market = market_bonus(
        item.get(
            "market_state",
            "UNKNOWN"
        )
    )


    confidence = confidence_bonus(
        item.get(
            "confidence",
            0
        )
    )


    penalty = risk_penalty(
        item.get(
            "risks",
            []
        )
    )


    final = (

        base_score * 0.65

        +

        ai_score * 0.35

    )


    final *= market

    final *= confidence

    final *= penalty


    return round(
        clamp(final),
        6
    )