"""
Reward Tracker

Stage29 Meta Learning Engine
"""


class RewardTracker:


    def __init__(self):

        self.records = []


    def record(
        self,
        reward
    ):

        self.records.append(
            reward
        )


    def history(
        self
    ):

        return self.records