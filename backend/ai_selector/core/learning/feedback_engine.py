class FeedbackEngine:


    def __init__(self):

        self.history = []


    def record(
        self,
        result
    ):

        self.history.append(
            result
        )


    def learn(self):

        return {
            "samples": len(self.history),
            "status": "ready"
        }