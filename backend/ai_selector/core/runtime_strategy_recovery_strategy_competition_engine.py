class RuntimeStrategyRecoveryStrategyCompetitionEngine:
    """
    Recovery strategy competition engine.
    """

    def __init__(self):

        self.records = []
        self.scores = {}


    def compete(
        self,
        strategy_results
    ):
        """
        strategy_results:

        {
            "restore": 0.9,
            "fallback": 0.6
        }
        """

        round_result = {}

        for strategy, score in strategy_results.items():

            self.scores[strategy] = (
                self.scores.get(strategy, 0)
                + score
            )

            round_result[strategy] = score


        self.records.append(
            round_result
        )

        return round_result



    def champion(self):

        if not self.scores:

            return None


        return max(
            self.scores,
            key=self.scores.get
        )



    def ranking(self):

        return sorted(
            self.scores.items(),
            key=lambda x:x[1],
            reverse=True
        )



    def history(self):

        return self.records