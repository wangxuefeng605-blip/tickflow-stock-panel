from core.learning.feedback_engine import FeedbackEngine
from core.learning.learning_memory import LearningMemory


class AutonomousLearner:

    def __init__(self):
        self.feedback = FeedbackEngine()
        self.memory = LearningMemory()


    def learn(self, result):

        feedback = self.feedback.evaluate(result)

        self.memory.store(feedback)

        return feedback