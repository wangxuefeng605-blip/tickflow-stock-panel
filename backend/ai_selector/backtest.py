import os

os.environ.pop("HTTP_PROXY", None)
os.environ.pop("HTTPS_PROXY", None)
os.environ.pop("ALL_PROXY", None)
import akshare as ak
import sqlite3
from datetime import datetime


DB_NAME = "stock_history.db"



# 回测单只股票

def calc_return(code):

    try:

        df = ak.stock_zh_a_hist_tx(
            symbol=code,
            start_date="20250101",
            end_date="20260712"
        )


        if len(df) < 20:

            return None


        buy_price = float(
            df.iloc[-15]["close"]
        )


        sell_price = float(
            df.iloc[-1]["close"]
        )


        ret = (
            sell_price -
            buy_price
        ) / buy_price * 100


        return round(ret,2)


    except Exception as e:

        print(
            code,
            "错误:",
            e
        )

        return None



# AI Top10

top10 = [

    {
        "code":"000078",
        "name":"ST海王"
    },

    {
        "code":"000021",
        "name":"深科技"
    },

    {
        "code":"000017",
        "name":"深中华A"
    },

    {
        "code":"000034",
        "name":"神州数码"
    },

    {
        "code":"000153",
        "name":"丰原药业"
    },

    {
        "code":"000063",
        "name":"中兴通讯"
    },

    {
        "code":"000066",
        "name":"中国长城"
    },

    {
        "code":"000516",
        "name":"国际医学"
    },

    {
        "code":"000088",
        "name":"盐田港"
    },

    {
        "code":"000301",
        "name":"东方盛虹"
    }

]



results=[]


print(
    "====== AI回测 ======"
)



for stock in top10:


    code = stock["code"]


    r = calc_return(code)


    print(
        code,
        stock["name"],
        "10日收益:",
        r,
        "%"
    )


    if r is not None:

        results.append(r)



if len(results)>0:


    avg_return = sum(results)/len(results)


    win_rate = (
        len(
            [
                x for x in results
                if x>0
            ]
        )
        /
        len(results)
    )*100



    print()

    print(
        "====== 回测统计 ======"
    )


    print(
        "平均收益:",
        round(avg_return,2),
        "%"
    )


    print(
        "胜率:",
        round(win_rate,2),
        "%"
    )



    conn = sqlite3.connect(
        DB_NAME
    )


    cursor = conn.cursor()


    cursor.execute(
        """
        INSERT INTO backtest_result
        (
        date,
        period,
        avg_return,
        win_rate,
        max_drawdown
        )

        VALUES
        (?,?,?,?,?)
        """,
        (
        datetime.now().strftime("%Y-%m-%d"),
        "10日",
        avg_return,
        win_rate,
        0
        )
    )


    conn.commit()

    conn.close()


    print(
        "回测结果保存成功"
    )