import akshare as ak
import pandas as pd
import numpy as np

def get_stock_list():
    df = ak.stock_info_a_code_name()
    return df["code"].tolist()[:30]


def get_data(symbol):
    try:
        df = ak.stock_zh_a_hist(symbol=symbol, period="daily", adjust="qfq")
        df = df.rename(columns={"收盘": "close"})
        return df
    except:
        return None


def score(df):
    try:
        df = df.copy()
        df["ma5"] = df["close"].rolling(5).mean()
        df["ma10"] = df["close"].rolling(10).mean()

        momentum = df["close"].iloc[-1] / df["close"].iloc[-10] - 1

        ma_score = 1 if df["ma5"].iloc[-1] > df["ma10"].iloc[-1] else 0

        return ma_score * 10 + momentum * 100
    except:
        return -999


def get_top10():
    stocks = get_stock_list()
    results = []

    print("📡 正在获取A股数据...")

    for i, s in enumerate(stocks):
        df = get_data(s)

        if df is None or len(df) < 20:
            continue

        sc = score(df)
        results.append((s, sc))

        print(f"{i+1}/30 {s} score={sc:.2f}")

    results.sort(key=lambda x: x[1], reverse=True)

    return results[:10]