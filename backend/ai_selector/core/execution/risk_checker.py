class RiskChecker:


    def check(
        self,
        decision
    ):

        confidence = decision.get(
            "confidence",
            0
        )


        risk = decision.get(
            "risk",
            1
        )


        if confidence >= 0.7 and risk <= 0.3:
            return True


        return False