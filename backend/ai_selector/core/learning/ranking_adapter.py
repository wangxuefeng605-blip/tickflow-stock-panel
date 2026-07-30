class LearningRankingAdapter:

    def apply(
        self,
        factors,
        weights
    ):
        return {
            key: value * weights.get(key, 1)
            for key, value in factors.items()
        }