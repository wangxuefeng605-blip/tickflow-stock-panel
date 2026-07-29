class PortfolioEngine:


    def evaluate(
        self,
        stock
    ):


        score = stock.get(
            "score",
            0
        )


        confidence = stock.get(
            "confidence",
            0
        )


        if score > 0.35 and confidence > 0.6:

            action="BUY"

        elif score > 0.2:

            action="HOLD"

        else:

            action="AVOID"


        risk="MEDIUM"


        if confidence < 0.5:
            risk="HIGH"


        return {

            "code":stock["code"],

            "action":action,

            "risk":risk,

            "confidence":confidence

        }