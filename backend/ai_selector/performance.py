import sqlite3
import pandas as pd



conn=sqlite3.connect(
    "stock_ai.db"
)


df=pd.read_sql(
"""
SELECT return_rate
FROM backtest_result

""",
conn
)


# 胜率

win_rate=(
    len(
        df[df.return_rate>0]
    )
    /
    len(df)
)



# 平均收益

avg_return=df.return_rate.mean()



# 最大回撤

equity=(1+df.return_rate).cumprod()


max_drawdown=(
    equity /
    equity.cummax()
    -1
).min()



print(
"====== AI策略表现 ======"
)


print(
"胜率:",
round(win_rate*100,2),
"%"
)


print(
"平均收益:",
round(avg_return*100,2),
"%"
)


print(
"最大回撤:",
round(max_drawdown*100,2),
"%"
)


conn.close()