class OutcomeEvaluator:


    def evaluate(
        self,
        outcome
    ):

        if outcome.get(
            "success"
        ):

            return {
                "reward":1,
                "signal":"positive"
            }


        return {
            "reward":-1,
            "signal":"negative"
        }