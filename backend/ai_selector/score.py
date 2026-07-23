import pandas as pd



# =================================
# AI综合评分
# =================================


def calculate_score(factors):


    score = (

        factors["momentum"] * 20

        +

        factors["volume_factor"] * 15

        +

        factors["trend"] * 15

        +

        factors["value"] * 15

        +

        factors["quality"] * 15

        +

        factors["growth"] * 10

        +

        factors["volatility"] * 5

        +

        factors["liquidity"] * 5

    )


    return round(score,2)





def add_score(df):


    df["score"] = df.apply(
        lambda x:
        calculate_score(x),
        axis=1
    )


    return df
# ==================================
# 兼容旧版本 daily_selector.py
# ==================================

def stock_score(factors):

    return calculate_score(factors)