"""
Meta Learning Controller

Stage29 Meta Learning Engine
"""


from .learning_memory import (
    LearningMemoryManager
)

from .reward_tracker import (
    RewardTracker
)

from .learning_feedback_processor import (
    LearningFeedbackProcessor
)



class MetaLearningController:


    def __init__(self):

        self.memory = LearningMemoryManager()

        self.reward = RewardTracker()

        self.processor = LearningFeedbackProcessor()



    def learn(
        self,
        feedback,
        weights
    ):


        self.memory.save(
            feedback
        )


        self.reward.record(
            feedback
        )


        return self.processor.process(
            feedback,
            weights
        )