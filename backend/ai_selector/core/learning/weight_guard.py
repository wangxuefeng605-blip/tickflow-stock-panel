"""
AI Learning Weight Guard

Protect weight update from extreme changes.
"""



class WeightGuard:


    def __init__(
        self,
        max_delta=0.05
    ):

        self.max_delta = max_delta



    def apply(
        self,
       current,
        proposed
    ):

        result = {}


        for key, old_value in current.items():

            new_value = proposed.get(
                key,
                old_value
            )


            delta = (
                new_value
                -
                old_value
            )


            if delta > self.max_delta:

                new_value = (
                    old_value
                    +
                    self.max_delta
                )


            elif delta < -self.max_delta:

               new_value = (
                    old_value
                    -
                    self.max_delta
                )


            result[key] = max(
                0,
                new_value
            )


        return self._rebalance(
            result,
            current
        )



    def normalize(
        self,
        weights
    ):

        total = sum(
            weights.values()
        )


        if total <= 0:

            return weights


        return {

            k:
            round(
                v / total,
                6
            )

            for k,v in weights.items()

        }

    def _rebalance(
        self,
        weights,
        current
    ):

        total = sum(
            weights.values()
        )


        diff = 1 - total


        if abs(diff) < 1e-6:
            return {
                k: round(v,6)
                for k,v in weights.items()
            }


        if diff > 0:

            # 需要增加权重
            for key in weights:

                room = (
                    current[key]
                    +
                    self.max_delta
                    -
                    weights[key]
                )


                if room <= 0:
                    continue


                add = min(
                    room,
                    diff
                )


                weights[key] += add

                diff -= add


                if diff <= 0:
                    break


        else:

            # 需要减少权重
            for key in weights:

                remove = min(
                    weights[key],
                    abs(diff)
                )


                weights[key] -= remove

                diff += remove


                if diff >= 0:
                    break


        return {
            k:round(v,6)
            for k,v in weights.items()
        }