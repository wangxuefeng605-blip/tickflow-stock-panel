"""
AI Confidence Calculator
v18.9
"""


def calculate_confidence(market):

    if not market:

        return 0.0


    confidence = 0


    momentum = market.get(
        "momentum",
        0
    )


    trend = market.get(
        "trend",
        0
    )


    if isinstance(trend, str):

        trend_map = {

            "UP": 1,

            "DOWN": 0,

            "SIDEWAY": 0.5

        }

        trend = trend_map.get(
            trend.upper(),
            0.5
        )

    else:

        trend = float(trend)



    volume = market.get(
        "volume_factor",
        0
    )


    volatility = market.get(
        "volatility",
        0
    )


    if isinstance(volatility, str):

        volatility_map = {

            "HIGH": 1,

            "MEDIUM": 0.5,

            "LOW": 0

        }

        volatility = volatility_map.get(
            volatility.upper(),
            0.5
        )

    else:

        volatility = float(volatility)



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
        confidence,
        1.0
    )