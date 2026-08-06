from core.learning.scanner_learning_hook import ScannerLearningHook
from core.learning.ranking_learning_hook import RankingLearningHook
from core.learning.learning_runtime_bridge import LearningRuntimeBridge


class LearningPipeline:


    def __init__(self):

        self.scanner_hook = ScannerLearningHook()

        self.ranking_hook = RankingLearningHook()

        self.runtime = LearningRuntimeBridge()



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