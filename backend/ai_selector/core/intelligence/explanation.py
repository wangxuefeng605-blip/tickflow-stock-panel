class AIExplanationEngine:


    def explain(
        self,
        factors,
        context,
        score
    ):

        signals=[]


        if factors.get("momentum",0) > 0.5:
            signals.append(
                "Strong momentum"
            )


        if factors.get("trend",0) > 0.5:
            signals.append(
                "Positive trend"
            )


        if factors.get("volatility",1) < 0.2:
            signals.append(
                "Low volatility"
            )


        return {

            "market_state":
                context.market_state,

            "confidence":
                context.confidence,

            "score":
                score,

            "signals":
                signals,

            "summary":
                self._summary(signals)

        }



    def _summary(
        self,
        signals
    ):

        if not signals:
            return "No strong signal"

        return (
            ", ".join(signals)
            +
            " supporting ranking"
        )