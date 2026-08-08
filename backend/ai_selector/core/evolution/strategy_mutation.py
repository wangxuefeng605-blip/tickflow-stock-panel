class StrategyMutation:

    def mutate(self, strategy_result):

        score = strategy_result.get(
            "score",
            0
        )

        if score >= 0.9:
            mutation = "increase_weight"
        elif score >= 0.8:
            mutation = "keep"
        else:
            mutation = "decrease_weight"

        return {
            "strategy": strategy_result.get(
                "strategy"
            ),
            "mutation": mutation,
            "confidence": score
        }