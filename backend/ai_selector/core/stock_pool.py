"""
AI Selector V3
Stock Pool Manager

Responsibilities
----------------
- 获取真实 A 股股票池
- 本地缓存
- 股票代码校验
- 股票池过滤
"""

from __future__ import annotations

import time
from pathlib import Path

import akshare as ak
import pandas as pd


class StockPoolConfig:
    CACHE_FILE = Path("data/cache/stock_pool.csv")
    CACHE_EXPIRE = 24 * 3600

    VALID_PREFIXES = (
        "000",
        "001",
        "002",
        "003",
        "300",
        "600",
        "601",
        "603",
        "605",
        "688",
    )


# -------------------------
# Utilities
# -------------------------

def normalize_code(code: str) -> str:
    return str(code).zfill(6)


def validate_stock_code(code: str) -> bool:
    code = normalize_code(code)
    return code.startswith(
        StockPoolConfig.VALID_PREFIXES
    )


# -------------------------
# Cache
# -------------------------

def cache_valid() -> bool:

    file = StockPoolConfig.CACHE_FILE

    if not file.exists():
        return False

    age = time.time() - file.stat().st_mtime

    return age < StockPoolConfig.CACHE_EXPIRE


def load_cache():

    file = StockPoolConfig.CACHE_FILE

    if not file.exists():
        return []

    df = pd.read_csv(
        file,
        dtype=str,
    )

    return (
        df["code"]
        .astype(str)
        .tolist()
    )


def save_cache(codes):

    file = StockPoolConfig.CACHE_FILE

    file.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    pd.DataFrame(
        {
            "code": codes
        }
    ).to_csv(
        file,
        index=False,
        encoding="utf-8-sig",
    )


# -------------------------
# Fetch
# -------------------------

def fetch_stock_pool():

    cache_file = "data/cache/stock_pool.csv"


    # 1. 优先读取缓存
    if os.path.exists(cache_file):

        print("股票池缓存命中")

        df = pd.read_csv(cache_file)

        return df["code"].tolist()



    # 2. 尝试远程获取

    sources=[
        stock_info_a_code_name,
        stock_zh_a_spot_em
    ]


    for source in sources:

        try:

            print("Source:",source.__name__)

            df = source()

            codes = df["code"].astype(str).tolist()


            # 保存缓存

            os.makedirs(
                "data/cache",
                exist_ok=True
            )

            pd.DataFrame(
                {"code":codes}
            ).to_csv(
                cache_file,
                index=False
            )


            return codes


        except Exception as e:

            print(
              "[Warning]",
              source.__name__,
              e
            )


    # 3. 最后备用股票池

    print(
      "[Fallback] 使用内置A股列表"
    )

    return load_builtin_pool()


# -------------------------
# Filter
# -------------------------

def filter_stock_pool(codes):

    result = []

    for code in codes:

        code = normalize_code(code)

        if not validate_stock_code(code):
            continue

        result.append(code)

    return sorted(
        set(result)
    )


# -------------------------
# Build
# -------------------------

def build_pool():

    print("生成股票池...")

    codes = fetch_stock_pool()

    codes = filter_stock_pool(codes)

    save_cache(codes)

    print(
        f"股票池生成完成: {len(codes)}"
    )

    return codes


# -------------------------
# Public API
# -------------------------

def get_stock_pool(
    refresh=False
):

    if (
        not refresh
        and
        cache_valid()
    ):

        codes = load_cache()

        print(
            f"股票池缓存命中: {len(codes)}"
        )

        return codes

    return build_pool()


# -------------------------
# Debug
# -------------------------

if __name__ == "__main__":

    stocks = get_stock_pool(
        refresh=True
    )

    print(stocks[:20])

    print(len(stocks))