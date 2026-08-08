from core.optimization.strategy_benchmark import (
    StrategyBenchmark
)

from core.optimization.strategy_optimizer import (
    StrategyOptimizer
)

from core.optimization.strategy_ranker import (
    StrategyRanker
)

from core.optimization.auto_promotion_engine import (
    AutoPromotionEngine
)


class OptimizationLoop:

    def __init__(self):

        self.benchmark = StrategyBenchmark()
        self.optimizer = StrategyOptimizer()
        self.ranker = StrategyRanker()
        self.promoter = AutoPromotionEngine()


    def run(self, strategies):

        optimized = []

        for item in strategies:

            result = self.optimizer.optimize(item)

            optimized.append(result)


        ranked = self.ranker.rank(
            optimized
        )


        promoted = self.promoter.promote(
            ranked
        )


        return promoted