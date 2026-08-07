"""
Decision Context

Stage30 Autonomous Decision Intelligence
"""


class DecisionContext:


    def __init__(
        self,
        data
    ):

        self.market = data.get(
            "market",
            "UNKNOWN"
        )


        self.confidence = data.get(
            "confidence",
            0
        )


        self.metadata = data