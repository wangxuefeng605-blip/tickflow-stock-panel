from .state import LearningState


class LearningStateManager:


    def __init__(self):

        self.state = LearningState()



    def get_state(
        self
    ):

        return self.state



    def update_reward(
        self,
        reward
    ):

        self.state.add_reward(
            reward
        )



    def update_weight(
        self,
        factor,
        value
    ):

        self.state.update_weight(
            factor,
            value
        )



    def snapshot(
        self
    ):

        return self.state.snapshot()