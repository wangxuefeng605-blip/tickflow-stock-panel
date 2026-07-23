import os
import pandas as pd
import akshare as ak
from tqdm import tqdm
import time


CACHE_DIR="kline_cache"


if not os.path.exists(CACHE_DIR):
    os.makedirs(CACHE_DIR)



def cache_path(code):

    return os.path.join(
        CACHE_DIR,
        f"{code}.csv"
    )



def download_one(code):

    try:


        if code.startswith("6"):

            symbol="sh"+code

        else:

            symbol="sz"+code



        df=ak.stock_zh_a_hist_tx(
            symbol=symbol,
            start_date="20250101",
            end_date="20260715"
        )



        if df.empty:

            return False



        df.to_csv(
            cache_path(code),
            index=False,
            encoding="utf-8-sig"
        )


        return True



    except Exception as e:


        print(
            code,
            "失败",
            e
        )


        return False





def batch_download(stocks):


    print("================")
    print("行情批量缓存 v16.5.1")
    print("================")


    success=0
    fail=0



    for code in tqdm(stocks):


        file=cache_path(code)



        # 已存在跳过

        if os.path.exists(file):

            success+=1

            continue



        if download_one(code):

            success+=1

        else:

            fail+=1



        time.sleep(0.3)



    print("================")
    print(
        "完成:",
        success
    )

    print(
        "失败:",
        fail
    )