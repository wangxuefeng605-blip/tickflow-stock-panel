class StrategyOptimizer:

    def __init__(self):
        self.history = []


    def optimize(self, strategy_result):

        score = strategy_result.get(
            "score",
            0
        )

        if score >= 0.8:
            status = "optimized"
        else:
            status = "needs_improvement"


        result = {
            "strategy": strategy_result.get(
                "strategy"
            ),
            "score": score,
            "status": status
        }


        self.history.append(result)

        return result


    def get_history(self):

        return self.history