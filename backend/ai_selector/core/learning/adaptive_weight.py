class AdaptiveWeightEngine:


    def __init__(self):

        self.weights = {
            "momentum": 0.2,
            "trend": 0.3,
            "quality": 0.5
        }


    def calculate_delta(
        self,
        reward
    ):

        if reward > 0:
            return 0.05

        if reward < 0:
            return -0.05

        return 0



    def adjust(
        self,
        factor,
        reward
    ):

        delta = self.calculate_delta(
            reward
        )


        current = self.weights.get(
            factor,
            0
        )


        new_weight = current + delta


        new_weight = max(
            0,
            min(
                1,
                new_weight
            )
        )


        self.weights[factor] = new_weight


        return {
            factor: new_weight
        }



    def get_weights(self):

        return self.weights