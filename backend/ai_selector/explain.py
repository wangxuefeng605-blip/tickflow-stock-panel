def explain_score(df):


    result=[]


    close=df["close"]


    # 动量

    change20 = (
        close.iloc[-1]
        /
        close.iloc[-20]
        -1
    )


    if change20>0:

        result.append(
            "20日趋势上涨"
        )


    else:

        result.append(
            "20日趋势偏弱"
        )



    # 均线

    ma5=close.tail(5).mean()

    ma20=close.tail(20).mean()


    if ma5>ma20:

        result.append(
            "短期均线向上"
        )


    else:

        result.append(
            "短期调整"
        )



    # 成交

    volume=df["volume"]


    if (
        volume.tail(5).mean()
        >
        volume.tail(20).mean()
    ):

        result.append(
            "成交活跃"
        )

    else:

        result.append(
            "成交平稳"
        )


    return result