import os
import csv
import time
from threading import Lock

from core.stock_pool import get_stock_pool

from core.scanner.engine import ScannerEngine
from scanner.factor_warmup import warmup_factors


RESULT_FILE = "tests/acceptance/reports/scanner_result.csv"

MAX_WORKERS = 8

lock = Lock()


def init_result_file():

    folder = os.path.dirname(RESULT_FILE)

    if folder:
        os.makedirs(
            folder,
            exist_ok=True
        )

    if not os.path.exists(RESULT_FILE):

        with open(
            RESULT_FILE,
            "w",
            encoding="utf-8-sig",
            newline=""
        ) as f:

            writer = csv.writer(f)

            writer.writerow(
                [
                    "code",
                    "alpha_score",
                    "momentum",
                    "trend",
                    "volatility",
                    "liquidity",
                    "value",
                    "quality",
                    "growth"
                ]
            )



def append_result(result):

    with lock:

        with open(
            RESULT_FILE,
            "a",
            encoding="utf-8-sig",
            newline=""
        ) as f:

            writer = csv.DictWriter(
                f,
                fieldnames=result.keys()
            )

            writer.writerow(result)



def run_fast_scan(
    stocks=None,
    limit=None
):

    print("=" * 50)
    print("AI Scanner v17.2")
    print("=" * 50)


    init_result_file()


    if stocks is None:

        stocks = get_stock_pool()


    if limit:

        stocks = stocks[:limit]


    total = len(stocks)


    print(
        f"股票池: {total}"
    )


    if total == 0:

        print(
            "股票池为空"
        )

        return []



    start = time.time()


    print(
        "Factor warmup..."
    )


    warmup_factors(
        stocks
    )


    print(
        "Starting scanner..."
    )


    engine = ScannerEngine(
        stocks,
        workers=MAX_WORKERS
    )


    results = []

    failed = []



    try:

        results, failed = engine.scan_batch(stocks)


    except Exception as e:

        print(
            "Scanner Error:",
            e
        )

        return []



    success = 0


    for item in results:

        try:

            append_result(
                item
            )

            success += 1


        except Exception as e:

            print(
                "Write result error:",
                e
            )



    elapsed = time.time() - start


    print()
    print("=" * 50)

    print(
        "Scanner Finished"
    )

    print(
        f"成功: {success}"
    )

    print(
        f"失敗: {len(failed)}"
    )

    print(
        f"耗時: {elapsed:.2f}s"
    )


    if elapsed > 0:

        print(
            f"速度: {(success+len(failed))/elapsed:.2f} stocks/s"
        )


    print(
        f"結果: {RESULT_FILE}"
    )

    print("=" * 50)



    return results



if __name__ == "__main__":


    run_fast_scan(
        limit=100
    )