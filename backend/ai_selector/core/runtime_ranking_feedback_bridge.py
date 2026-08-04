class RuntimeRankingFeedbackBridge:


    def feedback(self, ranking):

        return {
            "updated": True,
            "score": ranking.get(
                "score",
                0
            ),
            "rank": ranking.get(
                "rank",
                0
            )
        }