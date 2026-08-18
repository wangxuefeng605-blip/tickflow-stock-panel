import os
import csv
import time
from scanner.performance import PerformanceTracker

from concurrent.futures import ThreadPoolExecutor, as_completed
from threading import Lock

from tqdm import tqdm
from core.scanner.worker import ScanWorker

from core.stock_pool import get_stock_pool

from checkpoint import CheckpointManager
from retry_manager import RetryManager
from core.learning.runtime_weight_provider import (
    RuntimeWeightProvider
)



from core.history_cache import get_history
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
        context=None,
        weights=None
    ):

        self.context = context

        self.stocks = list(stocks)

        self.workers = workers

        self.start_time = None

        self.performance = PerformanceTracker()

        self.learning_runtime = (
            LearningRuntimeOrchestrator()
        )
        self.weight_provider = (
            RuntimeWeightProvider()
        )

        self.weight_provider = (
            RuntimeWeightProvider()
        )

        if weights is not None:
            self.weight_provider.update(
                weights
            )
        
    def scan_one(self, code):

        from core.scanner.worker import ScanWorker

        worker = ScanWorker(
            code,
            self.context
        )

        result = worker.scan()

        if result is None:
            return None

        return {
            "code": result["code"],
            "alpha_score": result["score"],
            **result.get("factors", {})
        }



    def scan_batch(self, codes):

        results = []

        failed_items = []


        with ThreadPoolExecutor(
            max_workers=self.workers
        ) as executor:


            futures = {

                executor.submit(
                    ScanWorker(
                        code,
                        self.context
                    ).scan
                ): code

                for code in codes
            }


            for future in as_completed(futures):

                code = futures[future]

                try:

                    result = future.result()

                    if result:

                       if "score" in result and "alpha_score" not in result:
                           result["alpha_score"] = result["score"]

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

            learned_results = self.learning_runtime.after_scan(
                results
            )

            if learned_results is not None:
               results = learned_results


        except Exception as e:

            print(
                f"Learning runtime failed: {e}"
            )

        return results, failed_items
         
    def run(self):

        results, failed_items = self.scan_batch(
            self.stocks
        )

        return results