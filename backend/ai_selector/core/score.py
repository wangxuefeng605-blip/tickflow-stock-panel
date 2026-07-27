"""
AI Selector v17.2
Alpha Score Engine

负责:
- 因子综合评分
- 输出股票Alpha分
"""


from __future__ import annotations


DEFAULT_WEIGHTS = {

    "momentum":0.25,

    "trend":0.25,

    "quality":0.20,

    "liquidity":0.15,

    "risk":0.15
}



def alpha_score(
    factors,
    weights=None
):

    if weights is None:

        weights = DEFAULT_WEIGHTS


    score = 0


    for name, weight in weights.items():

        value = factors.get(
            name,
            0
        )


        score += (
            value
            *
            weight
        )


    return score



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