from datetime import datetime


class LearningMemory:


    def __init__(self):

        self.records = []



    def remember(
        self,
        event
    ):

        record = {
            "timestamp": datetime.now().isoformat(),
            **event
        }

        self.records.append(
            record
        )

        return record



    def recent(
        self,
        limit=10
    ):

        return self.records[-limit:]



    def history(
        self
    ):

        return self.records