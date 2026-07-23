"""
AI Selector v17.2
Alpha Score Engine

负责:
- 因子综合评分
- 输出股票Alpha分
"""


from __future__ import annotations


def alpha_score(factors):

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


    score = (

        0.4 * momentum

        +

        0.2 * trend

        +

        0.2 * volume

        -

        0.2 * volatility

    )


    return round(
        score,
        4
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