"""
Learning package exports
"""


# =========================
# Stage21 Portfolio Feedback
# =========================

from .portfolio_feedback import *
from .performance_evaluator import *
from .learning_signal import *
from .weight_adapter import *

from .feedback_engine import (
    FeedbackLearningEngine
)

from .feedback_provider import (
    FeedbackProvider
)

from .daily_feedback_runner import (
    DailyFeedbackRunner
)


# =========================
# Legacy Compatibility
# =========================

try:
    from .learning_engine import *
except ImportError:
    pass


try:
    from .learning_pipeline import *
except ImportError:
    pass


try:
    from .feedback_analyzer import (
        FeedbackAnalyzer
    )
except ImportError:
    pass


try:
    from .prediction_feedback import *
except ImportError:
    pass


try:
    from .ranking_learning_hook import (
        RankingLearningHook
    )
except ImportError:
    pass


try:
    from .scanner_learning_hook import (
        ScannerLearningHook
    )
except ImportError:
    pass



class FeedbackEngine(
    FeedbackLearningEngine
):
    """
    Backward compatible wrapper.
    """

    def __init__(self):

        super().__init__()

        self.records = []


    def record(
        self,
        feedback
    ):

        self.records.append(
            feedback
        )


    def get_records(self):

        return self.records


    def learn(self):

        if not self.records:

            return {
                "samples":0
            }


        total_profit = sum(
            x.get(
                "profit",
                0
            )
            for x in self.records
        )


        avg_score = sum(
            x.get(
                "score",
                0
            )
            for x in self.records
        ) / len(self.records)


        return {

            "samples":len(self.records),

            "count":len(self.records),

            "avg_score":avg_score,

            "total_profit":total_profit

        }