from .learning_runtime_bridge import LearningRuntimeBridge


class RankingLearningHook:

    def __init__(self):

        self.events = []

        self.bridge = LearningRuntimeBridge()


    def record(self, result):

        self.events.append(result)

        return result


    def after_rank(self, result):

        self.record(result)

        return result