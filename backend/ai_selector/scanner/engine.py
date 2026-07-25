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

    def scan_one(self, code):

        code = str(code)

        history = load_history(code)

        if history is None or len(history) < 30:
            raise Exception("历史行情不足")

        factor = get_stock_factor(code)

        if factor is None:
            raise Exception("因子计算失败")

        score = stock_score(factor)

        return {
            "code": code,
            "alpha_score": score,
            **factor,
        }


    def scan_batch(self, codes):

        results = []

        with ThreadPoolExecutor(max_workers=8) as executor:

            futures = {
                executor.submit(self.scan_one, code): code
                for code in codes
            }

            for future in as_completed(futures):
                results.append(future.result())

        return results