class FeedbackMemory:


    def __init__(self):

        self.memory=[]


    def save(self, evaluation):

        self.memory.append(
            evaluation
        )


    def latest(self):

        if not self.memory:
            return None

        return self.memory[-1]