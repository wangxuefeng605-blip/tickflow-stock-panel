class PortfolioIntelligence:


    def analyze(
        self,
        performance,
        risk,
        attribution
    ):

        score = (
            performance.get("return",0)
            -
            risk.get("risk_score",0)
        )


        drivers = []

        for item in attribution:

            drivers.extend(
                item.get(
                    "drivers",
                    []
                )
            )


        learning_signal = {}

        for d in drivers:

            learning_signal[d] = (
                learning_signal.get(d,0)
                +
                0.01
            )


        risk_level = (
            "LOW"
            if risk.get("risk_score",0) < 0.3
            else "HIGH"
        )


        return {
          "portfolio_score": score,

          # compatibility
          "risk": risk_level,

          # new field
          "risk_level": risk_level,

          "top_drivers": drivers,
          "learning_signal": learning_signal
       }