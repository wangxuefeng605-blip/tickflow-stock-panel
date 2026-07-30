from .state_manager import LearningStateManager
from .weight_optimizer import WeightOptimizer
from .persistence import LearningPersistence


class FeedbackLoopRuntime:


    def __init__(self):

        self.state_manager = LearningStateManager()

        self.optimizer = WeightOptimizer()

        self.persistence = LearningPersistence()



    def calculate_reward(
        self,
        trade_result
    ):

        profit = trade_result.get(
            "profit",
            0
        )

        return profit / 100



    def process(
        self,
        trade_result
    ):

        reward = self.calculate_reward(
            trade_result
        )

        self.state_manager.update_reward(
            reward
        )

        state = self.state_manager.snapshot()

        self.persistence.save(
            state
        )

        return state