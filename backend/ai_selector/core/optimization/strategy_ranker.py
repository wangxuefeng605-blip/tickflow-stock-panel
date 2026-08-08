class StrategyRanker:

    def rank(self, strategies):

        ranked = sorted(
            strategies,
            key=lambda x: x.get("score", 0),
            reverse=True
        )

        result = []

        for index, item in enumerate(
            ranked,
            start=1
        ):
            result.append(
                {
                    "rank": index,
                    "strategy": item["strategy"],
                    "score": item["score"]
                }
            )

        return result