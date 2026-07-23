"""
AI_Top10 v17.0

History Cache Module

功能:

1. 历史行情缓存
2. Parquet存储
3. 自动更新
4. Tencent行情接口
5. 自动重试
6. 提供统一行情接口

"""
class HistoryError(Exception):
    pass
import os
import time
import pandas as pd
from datetime import datetime

import akshare as ak



# =========================
# 缓存目录
# =========================

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)


CACHE_DIR = os.path.join(
    BASE_DIR,
    "data",
    "cache",
    "history"
)


os.makedirs(
    CACHE_DIR,
    exist_ok=True
)



MAX_RETRY = 3



# =========================
# 股票代码
# =========================

def normalize_code(code):

    return str(code).zfill(6)




# =========================
# 缓存文件
# =========================

def get_cache_file(code):

    return os.path.join(
        CACHE_DIR,
        f"{normalize_code(code)}.parquet"
    )




# =========================
# 腾讯行情获取
# =========================

def fetch_history(code):


    code = normalize_code(code)


    try:

        if code.startswith(("6","68")):
            symbol="sh"+code
        else:
            symbol="sz"+code


        df = ak.stock_zh_a_hist_tx(
            symbol=symbol,
            start_date="20200101",
            end_date=datetime.now().strftime("%Y%m%d")

             )
        print(code, list(df.columns))

        if df is None:
            raise HistoryError(
                "empty response"
            )


        if not isinstance(df, pd.DataFrame):
            raise HistoryError(
                f"invalid type {type(df)}"
            )


        if df.empty:
            raise HistoryError(
                "empty dataframe"
            )


        df=df.rename(
            columns={
                "日期":"date",
                "开盘":"open",
                "收盘":"close",
                "最高":"high",
                "最低":"low",
                "成交量":"volume",
                "成交额":"amount"
            }
        )
        # =========================
        # volume字段兼容
        # Tencent接口没有volume
        # 使用 amount / close 估算
        # =========================

        if "volume" not in df.columns:

            if "amount" in df.columns:

                df["volume"] = (
                    df["amount"]
                    /
                    df["close"]
                )

                print(
                    f"{code} volume generated"
                )

            else:

                raise HistoryError(
                    "missing volume and amount"
                )

        required = [
            "date",
            "close",
            "volume"
        ]


        missing = [
            c for c in required
            if c not in df.columns
        ]


        if missing:

            raise HistoryError(
                f"missing columns {missing}"
            )


        df["date"] = pd.to_datetime(
            df["date"],
            errors="coerce"
        )


        df = df.dropna(
            subset=["date"]
        )


        df=df.sort_values(
            "date"
        )


        if len(df)<30:

            raise HistoryError(
                f"history too short {len(df)}"
            )


        return df



    except Exception as e:


        print(
            f"[HistoryError] {code}: {e}"
        )


        return None




# =========================
# 下载重试
# =========================

def download_history(code):


    for i in range(
        MAX_RETRY
    ):


        df=fetch_history(
            code
        )


        if df is not None:

            return df



        print(
            f"{code} 重试 {i+1}/{MAX_RETRY}"
        )


        time.sleep(2)



    return None




# =========================
# 保存
# =========================

def save_history(code,df):


    file=get_cache_file(code)


    df.to_parquet(
        file,
        engine="pyarrow",
        index=False
    )




# =========================
# 读取
# =========================

def load_history(code):


    file=get_cache_file(code)


    if not os.path.exists(file):

        return None



    try:

        df=pd.read_parquet(
            file
        )


        df["date"]=pd.to_datetime(
            df["date"]
        )


        return df


    except Exception as e:

     print(
        f"{code} cache load failed:",
        e
    )

    return None




# =========================
# 是否更新
# =========================

def need_update(df):


    if df is None:

        return True



    last=df["date"].max()


    today=pd.Timestamp.today()


    return (
        today-last
    ).days >= 3




# =========================
# 核心接口
# =========================

def get_history(
        code,
        refresh=False
):


    code=normalize_code(code)


    df=load_history(code)


    if df is not None and not need_update(df):

        return df



    if refresh or need_update(df):

        print(
            f"更新行情 {code}"
        )


        new_df=download_history(code)


        if new_df is not None:

            save_history(
                code,
                new_df
            )

            df=new_df



    return df




# =========================
# 测试
# =========================

if __name__=="__main__":


    df=get_history(
        "000001"
    )


    if df is not None:

        print(
            df.tail()
        )


        print(
            "行情数量:",
            len(df)
        )

    else:

        print(
            "获取失败"
        )