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


        return {

    "signals": signals,

    "market_state": market_state,

    "confidence": confidence,

    "score": score,

    "explanation": {

        "summary": explanation,

        "signals": signals,

        "market_state": market_state,

        "confidence": confidence,

        "score": score

    }

}