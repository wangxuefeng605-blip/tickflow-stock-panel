"""
AI Scanner V3
Single Stock Worker
"""

from core.history_cache import get_history
from core.stock_factor import calculate_factors
from core.score import alpha_score

from core.failed_stock import record_failed
from core.history_quality import validate_history

from core.scanner.performance import perf
from core.intelligence.context import AIContext

class ScanWorker:


    def __init__(
        self,
        code,
        context=None
    ):

        self.code = str(code).zfill(6)

        self.context = context


    def scan(self):

        with perf.timer("history"):

            history = get_history(self.code)


        quality = validate_history(history)


        if not quality["valid"]:

            record_failed(
                self.code,
                "history",
                quality["reason"],
                quality.get("days",0)
            )

            return None


        with perf.timer("factor"):

            factors = calculate_factors(history)


        with perf.timer("score"):

            score = alpha_score(
                factors,
                self.context.weights
            )


        return {
            "code": self.code,
            "score": score
        }