class RankingFeedback:


    def __init__(self):

        self.records = []


    def record_prediction(
        self,
        ranking,
        date
    ):

        record = {
            "date": date,
            "ranking": ranking
        }

        self.records.append(
            record
        )

        return record



    def evaluate(
        self,
        future_results
    ):

        rewards = []

        for item in future_results:

            reward = 1 if item.get(
                "return",
                0
            ) > 0 else 0


            rewards.append(
                {
                    "code": item.get("code"),
                    "reward": reward
                }
            )


        return rewards