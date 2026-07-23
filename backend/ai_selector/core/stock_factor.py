"""
AI Selector v17.2
Stock Factor Engine

只负责:
- 技术因子计算
- 基础Alpha因子

不负责:
- cache
- scanner
- ranking
"""

from __future__ import annotations

import pandas as pd
import numpy as np


def safe_value(x, default=0):

    if x is None:
        return default

    try:
        if np.isnan(x):
            return default
    except:
        pass

    return float(x)



def momentum_factor(df):

    if len(df) < 20:
        return 0

    close=df["close"]

    return safe_value(
        close.iloc[-1] /
        close.iloc[-20]-1
    )



def trend_factor(df):

    if len(df)<20:
        return 0

    close=df["close"]

    ma5=close.tail(5).mean()
    ma20=close.tail(20).mean()

    return 1 if ma5>ma20 else 0



def volatility_factor(df):

    if len(df)<20:
        return 0

    close=df["close"]

    return safe_value(
        close.pct_change()
        .rolling(20)
        .std()
        .iloc[-1]
    )



def volume_factor(df):

    # 兼容腾讯行情 amount
    if "volume" not in df.columns:

        if "amount" in df.columns:
            df["volume"] = (
                df["amount"]
                /
                df["close"]
            )

        else:
            return 0

    if len(df)<20:
        return 0

    v=df["volume"]

    return safe_value(
        v.iloc[-5:].mean()
        /
        v.iloc[-20:].mean()
    )



def calculate_factors(df):

    return {

        "momentum":
            round(momentum_factor(df),4),

        "trend":
            trend_factor(df),

        "volume_factor":
            round(volume_factor(df),4),

        "volatility":
            round(volatility_factor(df),4),

        "quality":
            0.5,

        "growth":
            0.5,

    }



if __name__=="__main__":

    import akshare as ak

    df=ak.stock_zh_a_hist_tx(
        symbol="000001",
        start_date="20250101",
        end_date="20260721"
    )

    print(
        calculate_factors(df)
    )