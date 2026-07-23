"""
Scanner Engine V3
"""

from __future__ import annotations

import time

from concurrent.futures import (
    ThreadPoolExecutor,
    as_completed,
)

from typing import Iterable

from core.scanner.worker import ScanWorker
from core.scanner.performance import perf


class ScannerEngine:

    def __init__(
        self,
        stocks: Iterable[str],
        workers: int = 8,
    ):

        self.stocks = list(stocks)

        self.workers = workers

        self.start_time = None

    # ---------------------------------

    def initialize(self):

        self.start_time = time.time()

        print("=" * 40)
        print(" AI Scanner v17.2 Stage 1 ")
        print("=" * 40)

        print(f"Stocks : {len(self.stocks)}")
        print(f"Workers: {self.workers}")

        print("=" * 40)
        print()

    # ---------------------------------

    def run(self):

        self.initialize()

        perf.reset()

        print("ScannerEngine initialized.")
        print()
        print("Start scanning...")
        print()

        results = []

        with ThreadPoolExecutor(
            max_workers=self.workers
        ) as executor:

            futures = {

                executor.submit(
                    ScanWorker(code).scan
                ): code

                for code in self.stocks

            }

            for future in as_completed(futures):

                try:

                    result = future.result()

                    if result is not None:

                        results.append(result)

                except Exception as e:

                    code = futures[future]

                    print(f"{code} worker failed: {e}")

        print()
        print(f"Finished: {len(results)}")
        print()

        print("Results:")

        for item in results:

            print(item)

        print()

        perf.report()

        self.shutdown()

        return results

    # ---------------------------------

    def shutdown(self):

        elapsed = 0

        if self.start_time is not None:

            elapsed = time.time() - self.start_time

        print()
        print("=" * 40)
        print("ScannerEngine shutdown")
        print(f"Elapsed : {elapsed:.2f}s")
        print("=" * 40)