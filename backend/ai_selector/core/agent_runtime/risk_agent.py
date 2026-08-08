class RiskAgent:

    def run(self, context):

        volatility = context.get(
            "volatility",
            0
        )

        if volatility > 0.5:
            level = "HIGH"

        elif volatility > 0.25:
            level = "MEDIUM"

        else:
            level = "LOW"


        return {
            "agent":"risk",
            "risk":level,
            "volatility":volatility
        }