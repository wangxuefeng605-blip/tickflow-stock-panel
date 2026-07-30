from .ranking_adapter import LearningRankingAdapter


class LearningRankingBridge:

    def __init__(self):

        self.adapter = LearningRankingAdapter()


    def process(
        self,
        ranking_result,
        learning_state
    ):

        feedback = {
            "adjustments":
                learning_state.get(
                    "weights",
                    {}
                )
        }


        result = self.adapter.apply_learning(
            {
                "weights": ranking_result.get(
                    "weights",
                    {}
                )
            },
            feedback
        )


        return {
            "learning_applied": True,
            "ranking": result
        }