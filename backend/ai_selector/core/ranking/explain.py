from .types import RankingResult


def explain(item):


    reasons=[]

    risks=[]


    factors=item.factors


    momentum = factors.get(
        "momentum",
        0
    )

    volume_factor = factors.get(
        "volume_factor",
        0
    )

    volatility = factors.get(
        "volatility",
        0
    )