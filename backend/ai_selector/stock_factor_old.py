import os

os.environ.pop("HTTP_PROXY", None)
os.environ.pop("HTTPS_PROXY", None)
os.environ.pop("ALL_PROXY", None)


import akshare as ak



def get_stock_factor(code):

    try:

        # 深圳股票
        if code.startswith("000") or code.startswith("001") or code.startswith("002"):
            symbol = "sz" + code

        # 上海股票
        else:
            symbol = "sh" + code



        df = ak.stock_zh_a_daily(
            symbol=symbol,
            adjust="qfq"
        )


        if len(df) < 25:

            return None



        close = df["close"]

        volume = df["volume"]



        close_price = close.iloc[-1]

        close_price_20 = close.iloc[-20]



        # 动量

        momentum = (
            close_price /
            close_price_20
        )



        # 成交量因子

        volume_today = volume.iloc[-1]


        volume_avg20 = (
            volume.tail(20)
            .mean()
        )


        volume_factor = (

            volume_today /
            volume_avg20

        )



        # 趋势

        MA5 = (
            close.tail(5)
            .mean()
        )


        MA20 = (
            close.tail(20)
            .mean()
        )


        trend = 1 if MA5 > MA20 else 0



        return {


            "code": code,


            "momentum":

            round(momentum,4),


            "volume_factor":

            round(volume_factor,4),


            "trend":

            trend

        }



    except Exception as e:

        print(
            code,
            "错误:",
            e
        )

        return None





if __name__ == "__main__":


    result = get_stock_factor(
        "000001"
    )


    print(result)