def calculate_metrics(trades):

    if not trades:

        return {
            "total_return":0,
            "win_rate":0,
            "trades":0
        }


    returns=[
        x["return"]
        for x in trades
    ]


    wins=[
        x
        for x in returns
        if x>0
    ]


    return {

        "total_return":
            sum(returns),

        "win_rate":
            len(wins)
            /
            len(returns),

        "trades":
            len(trades)

    }