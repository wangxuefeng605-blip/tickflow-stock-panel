import sqlite3


conn=sqlite3.connect(
    "stock_ai.db"
)


rows=conn.execute(
"""
SELECT
code,
name,
return_rate

FROM backtest_result

ORDER BY return_rate DESC

"""
).fetchall()



print("====== AI回测报告 ======")


for r in rows:

    print(
        r[0],
        r[1],
        "收益:",
        round(r[2]*100,2),
        "%"
    )



conn.close()