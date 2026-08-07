"""
Meta Learning Memory

Stage29 Meta Learning Engine
"""


class LearningMemory:

    def __init__(self):
        self.records = []


    def save(
        self,
        record
    ):
        self.records.append(
            record
        )

        return True


    def all(
        self
    ):
        return self.records


    def best(
        self
    ):
        if not self.records:
            return None

        return max(
            self.records,
            key=lambda x: x.get(
                "improvement",
                0
            )
        )