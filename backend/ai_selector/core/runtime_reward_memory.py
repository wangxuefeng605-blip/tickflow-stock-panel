class RuntimeRewardMemory:


    def __init__(self):

        self.history = []


    def record(self, reward):

        self.history.append(
            reward
        )

        return {
            "stored": True,
            "count": len(self.history)
        }


    def latest(self):

        if not self.history:

            return None

        return self.history[-1]