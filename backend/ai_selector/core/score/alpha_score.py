def alpha_score(
    factors,
    weights=None,
    context=None
):
    """
    Backward compatible alpha scoring engine.

    Supports:
    alpha_score(factors)

    alpha_score(factors, weights)

    alpha_score(
        factors,
        context=context
    )
    """

    if not factors:
        return 0.0


    if weights is None:

        if context and hasattr(context, "weights"):
            weights = context.weights

        else:
            weights = {
                "momentum": 0.35,
                "trend": 0.30,
                "quality": 0.15,
                "liquidity": 0.10,
                "risk": 0.10,
            }


    score = 0.0


    for key, weight in weights.items():

        value = factors.get(
            key,
            0
        )

        score += value * weight


    return score