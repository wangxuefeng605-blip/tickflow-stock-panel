"""
Learning Weight Adapter

Apply learning signals to AI ranking weights.
"""


class WeightAdapter:


    def apply(
        self,
        weights,
        signals,
        max_change=0.05
    ):
        """
        Adjust ranking weights.

        weights example:

        {
            "momentum":0.35,
            "trend":0.30,
            "quality":0.15,
            "liquidity":0.10,
            "risk":0.10
        }

        signals example:

        {
            "momentum":0.03,
            "risk":0.02
        }
        """

        new_weights = weights.copy()


        for factor, delta in signals.items():

            if factor not in new_weights:
                continue


            # limit adjustment

            if delta > max_change:
                delta = max_change

            if delta < -max_change:
                delta = -max_change


            new_weights[factor] += delta


        # normalize

        total = sum(
            new_weights.values()
        )


        if total > 0:

            for key in new_weights:
                new_weights[key] /= total


        return new_weights