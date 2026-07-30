from .memory_manager import LearningMemoryManager
from .adaptive_weight import AdaptiveWeightEngine


class LearningDecisionLoop:


    def __init__(self):

        self.memory = LearningMemoryManager()

        self.weight_engine = AdaptiveWeightEngine()



    def process(self, result):

        reward = result.get(
            "reward",
            0
        )


        factor = result.get(
            "factor",
            "momentum"
        )


        update = self.weight_engine.adjust(
            factor,
            reward
        )


        self.memory.save(
            {
                "factor": factor,
                "reward": reward,
                "update": update
            }
        )


        return {
            "learning_updated": True,
            "weights": update
        }