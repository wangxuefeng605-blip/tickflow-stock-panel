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

from core.intelligence.explainer import AIExplainer
from core.intelligence.confidence import calculate_confidence

class ScanWorker:


    def __init__(
        self,
        code,
        context=None
    ):

        print(
            "INIT WORKER CONTEXT:",
            context
        )
        
        self.code=str(code).zfill(6)

        self.context=context

        self.explainer = AIExplainer()


    


    def scan(self):

        print(
            "WORKER CONTEXT:",
            self.context
        )
        
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


        confidence = calculate_confidence(
            factors
        )

        if self.context:

           self.context.confidence = confidence


        if self.context:

            weights = self.context.weights

        else:

            weights = None


        with perf.timer("score"):

            score = alpha_score(
                factors,
                context=self.context
            )


        explanation = (
            self.explainer.explain(
                factors,
                self.context,
                score
            )
       )

        print(
            "WORKER AI:",
            {
               "market_state": explanation.get(
                    "market_state"
                ),
                "confidence": explanation.get(
                    "confidence"
                ),
                "signals": explanation.get(
                    "signals"
                )
            }
        )

        
        return {

            "code": self.code,

            "score": score,

            "factors": factors,

            "signals": explanation.get(
                "signals",
                 []
          ),

           "market_state": explanation.get(
               "market_state",
               "UNKNOWN"
            ),

            "confidence": explanation.get(
                "confidence",
                0
            ),

            "explanation": explanation

        }