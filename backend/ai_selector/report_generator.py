import sqlite3
from datetime import datetime


DB_NAME="stock_history.db"



def get_backtest_report():

    conn=sqlite3.connect(DB_NAME)

    cursor=conn.cursor()


    rows=cursor.execute(
        """
        SELECT
        date,
        period,
        avg_return,
        win_rate,
        max_drawdown

        FROM backtest_result

        ORDER BY id DESC

        LIMIT 1
        """
    ).fetchone()


    conn.close()


    if rows:

        return {

            "date":rows[0],

            "period":rows[1],

            "avg_return":rows[2],

            "win_rate":rows[3],

            "max_drawdown":rows[4]

        }


    return None





def generate_report(top10):


    today=datetime.now().strftime(
        "%Y-%m-%d"
    )


    msg="""

📈 AI量化股票日报

日期: {}

================

🔥 AI Top10

""".format(today)



    for i,stock in enumerate(
        top10,
        1
    ):


        msg += (

            f"{i}. "
            f"{stock['code']} "
            f"{stock['name']} "

            f"评分:"
            f"{stock['score']}\n"

        )



    msg += """

================

📊 回测结果

"""



    report=get_backtest_report()


    if report:


        msg += (

            f"周期: {report['period']}\n"

            f"平均收益: "
            f"{round(report['avg_return'],2)}%\n"

            f"胜率: "
            f"{round(report['win_rate'],2)}%\n"

            f"最大回撤: "
            f"{round(report['max_drawdown'],2)}%\n"

        )


    else:

        msg+="暂无回测数据\n"



    msg += """

================

机器人状态:
✅ AI选股运行正常

"""


    return msg




if __name__=="__main__":


    test=[

        {
        "code":"000078",
        "name":"ST海王",
        "score":1.48
        },

        {
        "code":"000021",
        "name":"深科技",
        "score":1.46
        }

    ]


    print(
        generate_report(test)
    )