import os
import pandas as pd
import akshare as ak


CACHE_DIR = "kline_cache"


os.makedirs(
    CACHE_DIR,
    exist_ok=True
)


pool = pd.read_csv(
    "stock_pool.csv",
    dtype={"code": str}
)


print("股票数量:", len(pool))


for i, code in enumerate(pool["code"]):

    file = os.path.join(
        CACHE_DIR,
        f"{code}.csv"
    )


    if os.path.exists(file):
        continue


    try:

        if code.startswith("6"):
            symbol = "sh" + code
        else:
            symbol = "sz" + code


        df = ak.stock_zh_a_hist_tx(
            symbol=symbol,
            start_date="20250101",
            end_date="20260731"
        )


        if df.empty:
            print(code, "empty")
            continue


        df.to_csv(
            file,
            index=False,
            encoding="utf-8-sig"
        )


        print(
            f"[{i+1}] saved {code}"
        )


    except Exception as e:

        print(
            code,
            e
        )