class RuntimeStrategyRewardEvaluator:


    def evaluate(self, rewards):

        if not rewards:

            return {
                "score":0,
                "keep":False
            }


        avg = sum(
            rewards
        ) / len(rewards)


        return {
            "score":avg,
            "keep":avg > 0.5
        }