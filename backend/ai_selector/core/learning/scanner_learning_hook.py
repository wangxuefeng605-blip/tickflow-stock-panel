from .learning_runtime_bridge import LearningRuntimeBridge


class ScannerLearningHook:

    def __init__(self):
        self.events = []
        self.bridge = LearningRuntimeBridge()


    def record(self, result):

        self.events.append(result)

        return result


    def apply(self, scan_result):

        return scan_result


    def after_scan(self, result):

        self.record(result)

        return result