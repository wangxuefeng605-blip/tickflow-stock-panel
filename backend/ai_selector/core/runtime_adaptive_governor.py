from .runtime_learning_optimizer import RuntimeLearningOptimizer
from .runtime_strategy_adapter import RuntimeStrategyAdapter


class RuntimeAdaptiveGovernor:


    def __init__(self):

        self.optimizer = RuntimeLearningOptimizer()

        self.adapter = RuntimeStrategyAdapter()



    def decide(self):

        learning = self.optimizer.optimize()

        strategy = self.adapter.adapt(
            learning
        )


        strategy["runtime_mode"] = (
            learning["preferred_mode"]
        )


        return strategy