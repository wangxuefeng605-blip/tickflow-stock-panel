from .memory import LearningMemory



class LearningMemoryManager:


    def __init__(self):

        self.memory = LearningMemory()



    def save(
        self,
        event
    ):

        return self.memory.remember(
            event
        )



    def recent(
        self,
        limit=10
    ):

        return self.memory.recent(
            limit
        )



    def all(
        self
    ):

        return self.memory.history()