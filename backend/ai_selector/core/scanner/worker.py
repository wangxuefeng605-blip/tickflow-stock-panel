"""
AI Scanner V3
Single Stock Worker
"""

from __future__ import annotations

import time

from core.history_cache import get_history
from core.stock_factor import calculate_factors
from core.score import alpha_score

from core.history_quality import validate_history
from core.failed_stock import record_failed

from core.scanner.performance import perf


class ScanWorker:

    def __init__(self, code: str):

        self.code = str(code).zfill(6)


    def scan(self):

        t0 = time.time()

        history = get_history(self.code)

        perf.record(
            "history",
            time.time() - t0
        )

        quality = validate_history(history)

        if not quality["valid"]:

           record_failed(
               code=self.code,
               stage="history",
               reason=quality["reason"],
               days=quality.get("days", 0)
           )

           return None


           t1 = time.time(
               
          )

        factors = calculate_factors(history)

        perf.record(
    "factor",
    time.time() - t1
)


        t2 = time.time()

        score = alpha_score(factors)

        perf.record(
            "score",
            time.time() - t2
        )


        return {
            "code": self.code,
            "score": score
        }