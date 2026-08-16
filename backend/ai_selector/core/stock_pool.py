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

import os
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
        "301",
        "302",
        "303",
        "304",
        "305",
        "306",
        "307",
        "308",
        "309",
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
    """
    Fetch A-share stock pool.

    Rules:
    - Valid non-empty cache is preferred.
    - Never treat an empty cache as a valid stock pool.
    - Never write an empty remote result into cache.
    - Try multiple AkShare sources.
    - Return [] only when all sources fail.
    """

    cache_file = StockPoolConfig.CACHE_FILE

    # -------------------------------------------------
    # 1. Use valid local cache
    # -------------------------------------------------

    if cache_valid():
        try:
            codes = load_cache()

            codes = [
                normalize_code(code)
                for code in codes
                if validate_stock_code(code)
            ]

            if codes:
                print(
                    f"股票池缓存命中: {len(codes)}"
                )
                return codes

            print(
                "股票池缓存为空或无有效代码，忽略缓存"
            )

        except Exception as exc:
            print(
                f"股票池缓存读取失败: {exc}"
            )

    # -------------------------------------------------
    # 2. Remote sources
    # -------------------------------------------------

    sources = [
        (
            "stock_info_a_code_name",
            ak.stock_info_a_code_name,
        ),
        (
            "stock_zh_a_spot_em",
            ak.stock_zh_a_spot_em,
        ),
    ]

    for source_name, source in sources:

        try:
            print(
                f"Source: {source_name}"
            )

            df = source()

            if df is None or df.empty:
                print(
                    f"Source returned empty result: {source_name}"
                )
                continue

            if "code" not in df.columns:
                print(
                    f"Source missing code column: {source_name}"
                )
                continue

            codes = [
                normalize_code(code)
                for code in df["code"].astype(str).tolist()
                if validate_stock_code(code)
            ]

            # Remove duplicates while preserving order.
            codes = list(
                dict.fromkeys(codes)
            )

            if not codes:
                print(
                    f"Source produced no valid stock codes: {source_name}"
                )
                continue

            # -------------------------------------------------
            # 3. Save ONLY non-empty valid cache
            # -------------------------------------------------

            save_cache(codes)

            print(
                f"股票池生成完成: {len(codes)}"
            )

            return codes

        except Exception as exc:
            print(
                f"Source failed: {source_name}: {exc}"
            )

    # -------------------------------------------------
    # 4. All remote sources failed
    # -------------------------------------------------

    print(
        "所有股票池数据源均失败，返回空股票池"
    )

    return []


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
        and cache_valid()
    ):

        codes = load_cache()

        codes = filter_stock_pool(codes)

        if codes:
            print(
                f"股票池缓存命中: {len(codes)}"
            )
            return codes

        print(
            "缓存为空，重新生成股票池"
        )

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