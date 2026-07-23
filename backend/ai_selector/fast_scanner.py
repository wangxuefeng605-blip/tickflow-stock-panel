import os
import csv
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from threading import Lock
from tqdm import tqdm

from core.stock_pool import get_stock_pool
from core.scanner.engine import ScannerEngine

from checkpoint import CheckpointManager
from retry_manager import RetryManager

from history_cache import load_history


def run_fast_scan(
    limit=None
):

    stocks = get_stock_pool()

    if limit:
        stocks = stocks[:limit]

    print(
        f"Stock Pool Size: {len(stocks)}"
    )

    engine = ScannerEngine(
        stocks,
        workers=8
    )

    return engine.run()


if __name__ == "__main__":

    run_fast_scan(
        limit=100
    )
RESULT_FILE = "tests/acceptance/reports/scanner_result.csv"
MAX_RETRY = 3
MAX_WORKERS = 8

lock = Lock()


def init_result_file():
    os.makedirs(os.path.dirname(RESULT_FILE), exist_ok=True)

    if not os.path.exists(RESULT_FILE):
        with open(RESULT_FILE, "w", encoding="utf-8-sig", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([
                "code",
                "alpha_score",
                "momentum",
                "trend",
                "volatility",
                "liquidity",
                "value",
                "quality",
                "growth"
            ])


def append_result(row):
    with lock:
        with open(RESULT_FILE, "a", encoding="utf-8-sig", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=row.keys())
            writer.writerow(row)


def scan_one(code):

    code = str(code)

    history = load_history(code)
    if history is None or len(history) < 30:
        raise Exception("历史行情不足")

    factor = load_factor(code)
    if factor is None:
        factor = calculate_factors(history)
        if factor:
            save_factor(code, factor)

    if not factor:
        raise Exception("因子计算失败")

    score = stock_score(factor)

    return {
        "code": code,
        "alpha_score": score,
        **factor
    }


def run_fast_scan(stocks=None):
    init_result_file()

    if stocks is None:
        stocks = get_stock_pool()

    total_pool = len(stocks)

    checkpoint = CheckpointManager(stocks)
    checkpoint.load()

    retry_mgr = RetryManager()

    todo = checkpoint.get_remaining()

    print("=" * 40)
    print("AI Scanner v17.2 Stage 1 Stable")
    print("=" * 40)
    print(f"股票池总数：{total_pool}")
    print(f"待扫描数量：{len(todo)}")

    start = time.time()
    success = 0
    failed = 0

    success_results = []
    
    with ThreadPoolExecutor(
        max_workers=MAX_WORKERS
    ) as executor:

        futures = {
            executor.submit(scan_one, code): code
            for code in todo
        }

        with tqdm(
            total=len(futures),
            desc="扫描中",
            unit="stock"
        ) as pbar:

            for future in as_completed(futures):

                code = futures[future]

                try:
                    result = future.result()

                    append_result(result)

                    checkpoint.mark_completed(code)

                    success += 1

                except Exception as e:

                    checkpoint.mark_failed(code)

                    retry_mgr.add_failed(
                        code,
                        str(e)
                    )

                    failed += 1

                pbar.update(1)


            for future in pbar:

                code = futures[future]

                try:

                    result = future.result()

                    append_result(result)

                    checkpoint.mark_completed(code)

                    success += 1


                except Exception as e:

                    checkpoint.mark_failed(code)

                    retry_mgr.add_failed(
                        code,
                        str(e)
                    )

                    failed += 1      


            if (success + failed) % 50 == 0:

                checkpoint.save()


            elapsed = time.time() - start

            speed = (
                success + failed
            ) / elapsed if elapsed > 0 else 0


            remain = (
                len(todo)
                -
                (success + failed)
            )


            eta = (
                remain / speed
                if speed > 0
                else 0
            )


            pbar.set_postfix(
                {
                    "success": success,
                    "failed": failed,
                    "speed": f"{speed:.1f}/s",
                    "ETA": f"{int(eta)}s"
                }
            )

    # 第二轮重试
    retry_codes = retry_mgr.get_failed_codes()

    if retry_codes:
        print(f"\n启动失败重试：{len(retry_codes)} 只")

        for code in retry_codes:

            for i in range(MAX_RETRY):

                try:
                    result = scan_one(code)

                    append_result(result)

                    checkpoint.mark_completed(code)

                    success += 1
                    failed -= 1

                    break

                except Exception as e:

                    print(
                        f"\nSCAN FAILED {code}: {e}"
                    )

                    retry_mgr.add_failed(
                        code,
                        str(e),
                        i + 1
                    )

                    time.sleep(1)

    total_time = time.time() - start
    speed = (success + failed) / total_time if total_time > 0 else 0

    print("\n" + "=" * 40)
    print("扫描完成")
    print("=" * 40)
    print(f"成功：{success}")
    print(f"失败：{failed}")
    print(f"耗时：{total_time:.2f}s")
    print(f"速度：{speed:.2f} stocks/s")
    print(f"结果文件：{RESULT_FILE}")
    print("=" * 40)

    return success_results

if __name__ == "__main__":
    run_fast_scan()