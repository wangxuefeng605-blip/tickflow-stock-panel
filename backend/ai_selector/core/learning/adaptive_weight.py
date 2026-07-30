class AdaptiveWeightEngine:


    def __init__(self):

        self.weights = {
            "momentum":0.3,
            "trend":0.3,
            "value":0.2,
            "quality":0.2
        }



    def adjust(
        self,
        factor,
        reward
    ):


        if factor not in self.weights:
            self.weights[factor]=0.2


        if reward < 0:

            self.weights[factor] *= 0.5


        elif reward > 0:

            self.weights[factor] *= 1.1



        self.weights[factor] = min(
            max(
                self.weights[factor],
                0.05
            ),
            1.0
        )


        return self.weights