class AIExplainer:


    def explain(
        self,
        factors,
        context,
        score=0
    ):


        signals=[]


        momentum = factors.get(
            "momentum",
            0
        )


        trend = factors.get(
            "trend",
            0
        )


        if momentum > 0.7:

            signals.append(
                "Strong momentum"
            )


        elif momentum > 0:

            signals.append(
                "Positive momentum"
            )


        if trend > 0:

            signals.append(
                "Trend confirmed"
            )



        if context:

            market_state = (
                context.market_state
            )

            confidence = (
                context.confidence
            )


        else:

            market_state="UNKNOWN"

            confidence=0



        explanation=f"""

Market State:
{market_state}


Confidence:
{confidence}


Score:
{score}


Signals:
{', '.join(signals)}

"""


        reason = []

        if market_state == "BULL":

            reason.append(
                "Market environment is bullish."
            )

        elif market_state == "BEAR":

            reason.append(
                "Market environment is weak."
            )

        else:

            reason.append(
                "Market direction is uncertain."
            )


        if "Strong momentum" in signals:

            reason.append(
                "Stock shows strong momentum."
            )

        elif "Positive momentum" in signals:

            reason.append(
                "Stock maintains positive momentum."
            )


        if "Trend confirmed" in signals:

            reason.append(
                "Trend confirmation is positive."
            )


        reason.append(
            f"Confidence level: {confidence:.0%}."
        )


        reason.append(
            f"Alpha score: {score:.4f}."
        )


        summary = "\n".join(reason)


        return {

           "signals": signals,

            "market_state": market_state,

            "confidence": confidence,

            "score": score,

            "reason": summary,

            "explanation": {

                "summary": summary,

                "reason": summary,

                "signals": signals,

                "market_state": market_state

            }

        }