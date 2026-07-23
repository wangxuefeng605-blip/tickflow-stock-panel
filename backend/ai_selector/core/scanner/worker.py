"""
AI Scanner V3
Single Stock Worker
"""

from __future__ import annotations

from core.history_cache import get_history
from core.stock_factor import calculate_factors
from core.score import alpha_score

from core.scanner.performance import perf


class ScanWorker:
    """
    单股票扫描
    """

    def __init__(self, code: str):

        self.code = str(code).zfill(6)

    def scan(self):

        code = self.code

        try:

            # -------------------------
            # History
            # -------------------------

            with perf.timer("history"):

                history = get_history(code)

            if history is None:
                return None

            # -------------------------
            # Factor
            # -------------------------

            with perf.timer("factor"):

                factors = calculate_factors(history)

            # -------------------------
            # Score
            # -------------------------

            with perf.timer("score"):

                score = alpha_score(factors)

            return {
                "code": code,
                "score": round(float(score), 4),
            }

        except Exception as e:

            print(f"{code} scan failed: {e}")

            return None