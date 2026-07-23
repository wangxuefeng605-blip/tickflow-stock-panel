import akshare as ak
import sqlite3
from datetime import datetime



DB="stock_history.db"



def get_top10():

    conn = sqlite3.connect(DB)

    cursor = conn.cursor()


    rows = cursor.execute(

    """
    SELECT code,name
    FROM daily_rank
    WHERE date =
    (
        SELECT MAX(date)
        FROM daily_rank
    )

    """

    ).fetchall()


    conn.close()


    return rows





def calc_stock_return(code, days=5):


    try:


        df = ak.stock_zh_a_hist(

            symbol=code,

            period="daily",

            adjust="qfq"

        )


        if len(df)<days+1:

            return None



        buy = df.iloc[-days-1]["收盘"]


        sell = df.iloc[-1]["收盘"]


        ret = (
            sell /
            buy
            -1
        )


        return ret*100



    except Exception as e:


        print(
            code,
            e
        )

        return None





def calculate_report():


    stocks=get_top10()


    returns=[]



    print(
        "回测股票数量:",
        len(stocks)
    )


    for code,name in stocks:


        r=calc_stock_return(
            code,
            5
        )


        if r is not None:


            print(

                code,

                name,

                "5日收益:",
                round(r,2),

                "%"

            )


            returns.append(r)




    if len(returns)==0:

        return



    avg_return = sum(returns)/len(returns)



    win_count = len(

        [
            x for x in returns
            if x>0
        ]

    )


    win_rate = (

        win_count /
        len(returns)

    )*100



    max_drawdown=min(
        returns
    )



    print("\n======策略报告======")

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


    print(
        "最大回撤:",
        round(max_drawdown,2),
        "%"
    )





    save_report(

        avg_return,

        win_rate,

        max_drawdown

    )





def save_report(
    avg,
    win,
    dd
):


    conn=sqlite3.connect(DB)

    cursor=conn.cursor()


    today=datetime.now().strftime(
        "%Y-%m-%d"
    )


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

    VALUES(?,?,?,?,?)

    """,

    (

    today,

    "5D",

    avg,

    win,

    dd

    )

    )


    conn.commit()

    conn.close()


    print(
        "回测报告保存成功"
    )





if __name__=="__main__":

    calculate_report()