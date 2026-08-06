"""
AI Selector v17.2
Alpha Score Engine

负责:
- 因子综合评分
- 输出股票Alpha分
"""


from __future__ import annotations
from core.ai_weight_provider import get_ai_weights


DEFAULT_WEIGHTS = {

    "momentum":0.25,

    "trend":0.25,

    "quality":0.20,

    "liquidity":0.15,

    "risk":0.15
}



def alpha_score(
    factors,
    context=None
):

    if isinstance(context, dict):

        weights = context


    elif context:

        weights = context.weights


    else:

        weights = get_ai_weights()


    score = 0


    for key, weight in weights.items():

        score += (
            factors.get(
                key,
                0
            )
            *
            weight
        )


    return round(
        score,
        6
    )



if __name__=="__main__":


    test={

        "momentum":0.0314,

        "trend":1,

        "volume_factor":1.126,

        "volatility":0.0127

    }


    print(
        {
            "alpha_score":
            alpha_score(test)
        }
    )