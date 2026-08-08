class StrategyAdjuster:

    def adjust(self, feedback):

        strategy = {
            "momentum": 0.35,
            "trend": 0.30,
            "risk": 0.10
        }

        if feedback.get("feedback") == "positive":
            strategy["momentum"] += 0.05
            strategy["trend"] += 0.03

        else:
            strategy["risk"] += 0.05

        return strategy