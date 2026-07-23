import pandas as pd



def momentum_factor(df):

    close = df["close"]

    return (
        close.iloc[-1]
        /
        close.iloc[-20]
        - 1
    )



def volume_factor(df):

    volume = df["volume"]

    return (
        volume.tail(5).mean()
        /
        volume.tail(20).mean()
    )



def trend_factor(df):

    close = df["close"]


    ma5 = (
        close
        .rolling(5)
        .mean()
        .iloc[-1]
    )


    ma20 = (
        close
        .rolling(20)
        .mean()
        .iloc[-1]
    )


    if ma5 > ma20:
        return 1

    else:
        return 0



def alpha_score(df):


    momentum = momentum_factor(df)

    volume = volume_factor(df)

    trend = trend_factor(df)


    score = (

        momentum * 0.5

        +

        volume * 0.3

        +

        trend * 0.2

    )


    return round(score,4)