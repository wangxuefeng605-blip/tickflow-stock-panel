from .state import LearningState


class LearningStateManager:


    def __init__(
        self,
        persistence=None
    ):

        self.persistence = persistence

        self.state = LearningState()


    def load(self):

        if self.persistence is None:
            return


        data = self.persistence.load()


        if not data:
            return


        self.state.version = data.get(
            "version",
            1
        )

        self.state.rewards = data.get(
            "rewards",
            []
        )

        self.state.weights = data.get(
            "weights",
            {}
        )

        self.state.optimizer_state = data.get(
            "optimizer_state",
            {}
        )


    def save(self):

        if self.persistence is None:
            return


        self.persistence.save(
            self.state.snapshot()
        )


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