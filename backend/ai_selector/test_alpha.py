import akshare as ak
import pandas as pd

from alpha_factor import alpha_score


print("====================")
print("测试股票: 平安银行 000001")
print("====================")


# 获取平安银行日线

df = ak.stock_zh_a_hist_tx(
    symbol="sz000001",
    start_date="20250101",
    end_date="20260712"
)


print("\n原始数据:")
print(df.head())


# 字段统一

df = df.rename(
    columns={
        "日期": "date",
        "开盘": "open",
        "收盘": "close",
        "最高": "high",
        "最低": "low",
        "成交量": "volume",
        "成交额": "amount"
    }
)


# 检查成交量

if "volume" not in df.columns:

    print("没有volume，使用amount替代")

    df["volume"] = df["amount"]



print("\n标准化字段:")
print(df.columns)


print("\n最后数据:")
print(df.tail())


# Alpha评分

score = alpha_score(df)


print("\n====================")
print("平安银行 Alpha评分:")
print(score)
print("====================")