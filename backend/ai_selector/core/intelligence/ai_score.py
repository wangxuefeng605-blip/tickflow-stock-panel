class AIScore:


    def calculate(
        self,
        factors,
        weights
    ):

        score=0


        for key,w in weights.items():

            score += (
                factors.get(key,0)
                *
                w
            )


        return round(score,4)