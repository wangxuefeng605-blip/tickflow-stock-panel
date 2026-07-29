"""
AI Confidence Calculator
v18.9
"""


def calculate_confidence(factors):

    if not factors:
        return 0.0


    confidence = 0


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

    volatility = factors.get(
        "volatility",
        0
    )


    if momentum > 1:
        confidence += 0.35


    elif momentum > 0.7:
        confidence += 0.2


    if trend >= 1:
        confidence += 0.3


    if volume > 1:
        confidence += 0.2


    if volatility < 0.1:
        confidence += 0.15


    return min(
        round(
            confidence,
            2
        ),
        1.0
    )