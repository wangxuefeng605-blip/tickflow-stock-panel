from core.learning.outcome import OutcomeTracker
from core.learning import FeedbackAnalyzer


class DecisionFeedback:


    def __init__(
        self,
        tracker=None,
        analyzer=None
    ):

        self.tracker = (
            tracker
            or OutcomeTracker()
        )

        self.analyzer = (
            analyzer
            or FeedbackAnalyzer()
        )


    def evaluate(
        self,
        code,
        result
    ):


        outcome = self.tracker.update_result(
            code,
            result
        )


        if outcome is None:

            return None


        feedback = self.analyzer.analyze(
            result
        )


        return feedback