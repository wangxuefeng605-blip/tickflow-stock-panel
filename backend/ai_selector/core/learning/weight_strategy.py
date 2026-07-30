class WeightStrategy:


    def reward_direction(
        self,
        reward
    ):

        if reward > 0:
            return "increase"

        if reward < 0:
            return "decrease"

        return "hold"