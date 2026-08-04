from .runtime_learning_memory import RuntimeLearningMemory
from .runtime_learning_optimizer import RuntimeLearningOptimizer


class RuntimeLearningPipeline:


    def __init__(self):

        self.memory = RuntimeLearningMemory()

        self.optimizer = RuntimeLearningOptimizer()



    def process(self, feedback):

        stored = self.memory.store(
            feedback
        )


        decision = self.optimizer.optimize()


        return {

            "memory": stored,

            "optimization": decision,

            "learning_completed": True

        }