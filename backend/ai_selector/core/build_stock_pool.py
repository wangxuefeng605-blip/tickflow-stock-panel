"""
Build Stock Pool
v17.2 Stable

生成:
data/cache/stock_pool.csv

"""

import os
import pandas as pd


POOL_FILE = "data/cache/stock_pool.csv"


def build_pool():

    os.makedirs(
        "data/cache",
        exist_ok=True
    )


    #
    # A股市场代码
    #

    codes = []


    # 深圳主板
    for i in range(1, 10000):
        codes.append(
            f"{i:06d}"
        )


    # 沪市
    for i in range(600000, 700000):
        codes.append(
            str(i)
        )


    #
    # 过滤
    #

    result = []


    for code in codes:


        if code.startswith(
            (
                "000",
                "001",
                "002",
                "003",
                "300",
                "600",
                "601",
                "603",
                "605"
            )
        ):
            result.append(code)



    df = pd.DataFrame(
        {
            "code": result
        }
    )


    df.to_csv(
        POOL_FILE,
        index=False,
        encoding="utf-8-sig"
    )


    print(
        "股票池生成:",
        len(result)
    )


if __name__ == "__main__":

    build_pool()