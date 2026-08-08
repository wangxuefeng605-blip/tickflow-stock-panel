"""
Evolution Strategy Mutation

Stage53.4
Generate candidate strategies
"""


class EvolutionStrategy:


    def mutate(
        self,
        weights
    ):

        candidates = []


        # candidate 1
        c1 = weights.copy()

        c1["momentum"] += 0.05

        candidates.append(
            self.normalize(c1)
        )


        # candidate 2
        c2 = weights.copy()

        c2["trend"] += 0.05

        candidates.append(
            self.normalize(c2)
        )


        # candidate 3
        c3 = weights.copy()

        c3["risk"] += 0.05

        candidates.append(
            self.normalize(c3)
        )


        return candidates



    def normalize(
        self,
        weights
    ):

        total = sum(
            weights.values()
        )

        result = {
            k:round(v / total, 4)
            for k,v in weights.items()
        }


        diff = round(
            1 - sum(result.values()),
            4
        )


        if diff != 0:

            key = max(
                result,
                key=result.get
            )

            result[key] = round(
                result[key] + diff,
                4
            )


        return result