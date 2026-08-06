from .scanner_learning_hook import ScannerLearningHook
from .ranking_learning_hook import RankingLearningHook
from .learning_runtime_bridge import LearningRuntimeBridge
from .feedback_engine import FeedbackLearningEngine
from .prediction_lifecycle import PredictionLifecycle
from .feedback_engine import FeedbackLearningEngine
from .feedback_result import FeedbackResult

class LearningPipeline:


    def __init__(self):

        self.scanner_hook = ScannerLearningHook()

        self.ranking_hook = RankingLearningHook()

        self.runtime = LearningRuntimeBridge()


        self.lifecycle = PredictionLifecycle()

        self.feedback = FeedbackLearningEngine()

        self.feedback_engine = FeedbackLearningEngine()

    def run(
        self,
        scan_result
    ):


        scanned = self.scanner_hook.after_scan(
            scan_result
        )


        ranked = self.ranking_hook.after_rank(
            scanned
        )


        return ranked

    def process_feedback(
        self,
        feedbacks,
        weights=None
    ):

        results = []

        for item in feedbacks:

            reward = 1 if item.get(
                "success",
                False
            ) else 0

            results.append(
                {
                    "code": item.get("code"),
                    "reward": reward
                }
            )


        if weights is None:
            return results


        update = (
            self.feedback_engine
            .update_weights(
                weights,
                feedbacks
            )
        )


        return FeedbackResult(
            feedback=results,
            weights=update["weights"],
            performance=update["performance"],
            learning=update["learning"]
        )