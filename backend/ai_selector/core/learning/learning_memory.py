class LearningMemory:

    def __init__(self):
        self.storage = []


    def save(self, data):

        self.storage.append(data)

        return data


    def get_all(self):

        return self.storage

    def store(self, data):
        """
        Store learning feedback.

        Compatibility interface for AutonomousLearner.
        """

        if data is None:
            return False

        if hasattr(self, "save"):
            self.save(data)
            return True

        if hasattr(self, "append"):
            self.append(data)
            return True

        if hasattr(self, "memory"):
            self.memory.append(data)
            return True

        return False