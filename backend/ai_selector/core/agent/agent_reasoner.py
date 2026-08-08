class AgentReasoner:

    def reason(self, context):

        score = context.get(
            "score",
            0
        )

        if score >= 0.7:

            return {
                "decision":"BUY",
                "confidence":score,
                "reason":"strong signal"
            }


        return {
            "decision":"WAIT",
            "confidence":score,
            "reason":"weak signal"
        }