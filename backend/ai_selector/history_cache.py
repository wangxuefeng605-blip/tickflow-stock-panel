import os
import pandas as pd

from kline_cache import load_kline

CACHE_DIR = "history_cache"
os.makedirs(CACHE_DIR, exist_ok=True)


def cache_file(code):
    return os.path.join(CACHE_DIR, f"{code}.csv")


def load_history(code):
    file = cache_file(code)

    if os.path.exists(file):
        try:
            return pd.read_csv(file)
        except Exception:
            pass

    # history_cache 没有，则读取 kline_cache
    data = load_kline(code)

    if data is not None and len(data) > 0:
        data.to_csv(file, index=False)
        return data

    return None


def save_history(code, df):
    df.to_csv(cache_file(code), index=False)


def get_history(code):
    return load_history(code)