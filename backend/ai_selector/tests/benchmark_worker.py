import time

from scanner.engine import ScannerEngine


STOCKS = [
    "000001",
    "000002",
    "000006",
    "000007",
    "000008",
    "000009",
    "000011",
    "000012",
    "000014",
    "000017",
]


def benchmark(workers):

    engine = ScannerEngine(
        max_workers=workers
    )

    start = time.time()

    results, failed = engine.scan_batch(
        STOCKS
    )

    elapsed = time.time() - start

    speed = len(results) / elapsed if elapsed else 0

    print("=" * 40)

    print(
        f"workers : {workers}"
    )

    print(
        f"time    : {elapsed:.3f}s"
    )

    print(
        f"success : {len(results)}"
    )

    print(
        f"failed  : {len(failed)}"
    )

    print(
        f"speed   : {speed:.2f} stocks/s"
    )


if __name__ == "__main__":

    for workers in [
        2,
        4,
        8,
        16,
        32,
    ]:

        benchmark(workers)