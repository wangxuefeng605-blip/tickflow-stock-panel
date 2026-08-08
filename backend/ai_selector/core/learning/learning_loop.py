from core.learning.learning_memory import LearningMemory
from core.learning.learning_feedback import LearningFeedback


class LearningLoop:

    def __init__(self):

        self.memory = LearningMemory()
        self.feedback = LearningFeedback()


    def learn(self, data):

        self.memory.save(data)

        self.feedback.record(data)

        return {
            "learned": True,
            "data": data
        }