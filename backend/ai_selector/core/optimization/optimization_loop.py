from core.optimization.strategy_optimizer import StrategyOptimizer


class OptimizationLoop:

    def __init__(self):
        self.optimizer = StrategyOptimizer()


    def run(self, strategies):

        if isinstance(strategies, dict):
            strategies = [
                {
                    "strategy": "default",
                    "score": strategies.get(
                        "avg_score",
                        0
                    )
                }
            ]


        results = []

        for item in strategies:

            optimized = self.optimizer.optimize(
                item
            )

            results.append(
                {
                    **item,
                    **optimized
                }
            )


        results.sort(
            key=lambda x:x.get(
                "score",
                0
            ),
            reverse=True
        )


        winner = results[0]

        winner["rank"] = 1

        return winner