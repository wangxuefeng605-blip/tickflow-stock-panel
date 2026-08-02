import os
import csv
import time
from scanner.performance import PerformanceTracker

from concurrent.futures import ThreadPoolExecutor, as_completed
from threading import Lock

from tqdm import tqdm


from core.stock_pool import get_stock_pool

from checkpoint import CheckpointManager
from retry_manager import RetryManager


from history_cache import load_history
from core.factor_cache import (
    get_factor,
    save_factor,
    factor_cache_report
)
from stock_factor import get_stock_factor
from score import stock_score
from core.learning.learning_runtime_orchestrator import (
    LearningRuntimeOrchestrator
)


class ScannerEngine:


    def __init__(
        self,
        stocks,
        workers=8,
        context=None
    ):

        self.context = context

        self.stocks = list(stocks)

        self.workers = workers

        self.start_time = None

        self.performance = PerformanceTracker()

        self.learning_runtime = (
            LearningRuntimeOrchestrator()
        )

        
    def scan_one(self, code):
     
     
        code = str(code)


        start = time.time()

        history = load_history(code)

        self.performance.record(
            "history",
            time.time() - start
        )     

        if history is None or len(history) < 30:
            raise Exception(
                "历史行情不足"
            )


        start = time.time()

        factor = get_stock_factor(code)

        self.performance.record(
            "factor",
            time.time() - start
        )

        if factor is None:
            raise Exception(
                "因子计算失败"
            )


        start = time.time()

        score = stock_score(
             factor
        )

        self.performance.record(
            "score",
            time.time() - start
        )


        return {
            "code": code,
            "alpha_score": score,
            **factor,
        }



    def scan_batch(self, codes):

        results = []

        failed_items = []


        with ThreadPoolExecutor(
            max_workers=self.workers
        ) as executor:


            futures = {

                executor.submit(
                    self.scan_one,
                    code
                ): code

                for code in codes

            }


            for future in as_completed(futures):

                code = futures[future]

                try:

                    result = future.result()

                    results.append(
                        result
                    )


                except Exception as e:

                    failed_items.append(
                        (
                            code,
                            str(e)
                        )
                    )


        self.performance.report()

        factor_cache_report()


        try:

            results = self.learning_runtime.after_scan(
                results
          )

        except Exception as e:

            print(
                 f"Learning runtime failed: {e}"
            )


        return results, failed_items