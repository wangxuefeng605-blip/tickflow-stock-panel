class FeedbackCollector:

    def __init__(self):
        self.records = []


    def record(
        self,
        code,
        score,
        decision,
        result
    ):

        item = {
            "code": code,
            "score": score,
            "decision": decision,
            "result": result
        }

        self.records.append(item)

        return item


    def all(self):

        return self.records