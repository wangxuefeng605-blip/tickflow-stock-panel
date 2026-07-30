class LearningRankingAdapter:


    def apply_learning(
        self,
        ranking_state,
        feedback
    ):

        weights = ranking_state["weights"].copy()

        adjustments = feedback["adjustments"]

        for key, value in adjustments.items():

            weights[key] = (
                weights.get(key, 0)
                +
                value
            )


        return {
            "weights": weights,
            "learning_applied": True
        }



    def apply(
        self,
        factors,
        weights
    ):

        result = {}

        for key, value in factors.items():

            result[key] = (
                value *
                weights.get(key, 0)
            )

        return result