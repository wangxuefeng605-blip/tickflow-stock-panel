import os
import csv
import time

from concurrent.futures import ThreadPoolExecutor, as_completed
from threading import Lock

from tqdm import tqdm


from core.stock_pool import get_stock_pool

from checkpoint import CheckpointManager
from retry_manager import RetryManager


from history_cache import load_history
from factor_cache import load_factor, save_factor

from stock_factor import get_stock_factor
from score import stock_score

class ScannerEngine:


    def scan_batch(self, codes):

        results = []

        failed_items = []

        with ThreadPoolExecutor(
             max_workers=8
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

                     if result is None:
                         raise Exception(
                             "scan result empty"
                        )

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


        return (
            results,
            failed_items
    )