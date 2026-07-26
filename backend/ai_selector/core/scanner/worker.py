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

        history = load_history(self.code)


        quality = validate_history(history)


        if not quality["valid"]:

            record_failed(
                self.code,
                quality["reason"],
                quality["days"]
            )

            return None


        factor = get_stock_factor(history)


        score = stock_score(factor)


        return {
            "code":self.code,
            "score":score
        }