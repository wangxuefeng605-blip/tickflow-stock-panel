class WeightAdjuster:


    def adjust(
        self,
        feedback
    ):

        signals = feedback.get(
            "signals",
            {}
        )


        result = {}


        for factor, value in signals.items():


            if value > 0.6:

                result[factor] = 0.02


            elif value < 0.4:

                result[factor] = -0.02


            else:

                result[factor] = 0



        return result