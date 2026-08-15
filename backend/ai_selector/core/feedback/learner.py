class FeedbackLearner:

    def __init__(self, storage, evaluator):
        self.storage = storage
        self.evaluator = evaluator

    def learn(self):
        records = self.storage.load()

        result = self.evaluator.evaluate(records)

        return {
            "samples": result["count"],
            "score": result["score"],
            "status": "READY"
            if result["count"] > 0
            else "EMPTY"
        }