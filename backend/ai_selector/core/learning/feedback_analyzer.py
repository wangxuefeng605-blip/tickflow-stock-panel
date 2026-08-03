from pathlib import Path
from core.learning.prediction.prediction_store import (
    PredictionStore
)
from core.learning.outcome.outcome_tracker import (
    OutcomeTracker
)


class FeedbackAnalyzer:


    def __init__(self):

        self.prediction_store = PredictionStore()

        self.outcome_tracker = OutcomeTracker()



    def analyze(
    self,
    result
    ):

        predictions = (
            self.prediction_store.load_all()
        )

        outcomes = (
            self.outcome_tracker.load_all()
        )


        outcome_map = {}

        for item in outcomes:

            code = item.get(
                "code"
            )

            outcome_map[code] = (
                item.get(
                    "result",
                    {}
                )
            )


        result = {

            "total": 0,

            "success": 0,

            "failure": 0,

            "success_rate": 0,

            "signals": {}

        }


        for prediction in predictions:

            for stock in prediction.get(
                "stocks",
                []
            ):

                code = stock.get(
                    "code"
                )

                if code not in outcome_map:
                    continue


                result["total"] += 1


                outcome = outcome_map[code]


                if outcome.get(
                    "success",
                    False
                ):

                    result["success"] += 1

                else:

                    result["failure"] += 1



        if result["total"]:

            result["success_rate"] = (
                result["success"]
                /
                result["total"]
            )


        return result