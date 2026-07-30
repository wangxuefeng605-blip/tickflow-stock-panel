class LearningState:

    def __init__(self):

        self.version = 1

        self.rewards = []

        self.weights = {
            "momentum": 0.2
        }

        self.optimizer_state = {}


    def add_reward(
        self,
        reward
    ):

        self.rewards.append(
            reward
        )


    def update_weight(
        self,
        factor,
        value
    ):

        self.weights[factor] = value


    def snapshot(self):

        return {
            "version": self.version,
            "rewards": self.rewards,
            "weights": self.weights,
            "optimizer_state": self.optimizer_state
        }