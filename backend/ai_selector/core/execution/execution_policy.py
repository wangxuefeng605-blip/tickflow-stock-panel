def allow_execution(decision):


    if hasattr(
        decision,
        "confidence"
    ):

        confidence = decision.confidence


    else:

        confidence = decision.get(
            "confidence",
            0
        )


    return confidence > 0.5