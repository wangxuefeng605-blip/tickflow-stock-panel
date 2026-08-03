from pathlib import Path
from core.learning.prediction.prediction_store import (
    PredictionStore
)
from core.learning.outcome.outcome_tracker import (
    OutcomeTracker
)


class FeedbackAnalyzer:


    def analyze(
        self,
        result=None
    ):


        if result is None:

            return {

                "success_rate":0,

                "total":0,

                "success_count":0

            }


        success = result.get(
            "success",
            result.get(
                "return",
                0
            ) > 0
        )


        reward = 1 if success else 0


        return {

            "success":success,

            "reward":reward,

            "confidence":1 if success else 0

        }