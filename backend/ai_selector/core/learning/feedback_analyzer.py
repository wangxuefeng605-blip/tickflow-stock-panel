class FeedbackAnalyzer:


    def analyze(
        self,
        feedback
    ):

        future_return = feedback.get(
            "future_return",
            0
        )

        momentum = feedback.get(
            "momentum",
            0
        )


        return {

            "momentum": momentum,

            "future_return": future_return,

            "reward":
                future_return,

            "positive":
                future_return > 0

        }