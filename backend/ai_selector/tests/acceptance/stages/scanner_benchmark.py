import time
import traceback


def run_scanner_benchmark(limit=10):

    result = {}

    start = time.perf_counter()

    try:

        from fast_scanner import run_fast_scan
        from stock_pool import get_stock_pool
        from checkpoint import CheckpointManager


        stocks = get_stock_pool()


        if limit:
           stocks = stocks[:limit]


        # 清除旧扫描状态，保证真正执行扫描
        checkpoint = CheckpointManager(stocks)
        checkpoint.clear()


        data = run_fast_scan(
            stocks
        )


        elapsed = time.perf_counter() - start


        if isinstance(data, int):
            stocks_count = data
        else:
            stocks_count = len(data)


        result["scanner"] = {
    "status": "PASS",
    "stocks": stocks_count,
    "seconds": round(elapsed, 3)
}


    except Exception as e:

        result["scanner"] = {
            "status": "FAIL",
            "error": str(e),
            "traceback": traceback.format_exc()
        }


    return result
 