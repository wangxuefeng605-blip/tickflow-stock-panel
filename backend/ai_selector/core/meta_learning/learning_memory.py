"""
Learning Memory Manager

Stage29 Meta Learning Engine
"""


class LearningMemoryManager:


    def __init__(self):

        self.records = []



    def save(
        self,
        data
    ):

        self.records.append(
            data
        )



    def recent(
        self
    ):

        return self.records