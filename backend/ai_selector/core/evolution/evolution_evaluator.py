"""
Evolution Evaluator

Stage28 Self Evolution Layer
"""


class EvolutionEvaluator:


    def evaluate(
        self,
        old_strategy,
        new_strategy
    ):

        old_score = old_strategy.get(
            "score",
            0
        )

        new_score = new_strategy.get(
            "score",
            0
        )


        return {
            "accepted": new_score > old_score,
            "improvement": new_score - old_score,
            "score": new_score
        }



    def rank(
        self,
        strategies
    ):

        return sorted(
            strategies,
            key=lambda x:x.get(
                "score",
                0
            ),
            reverse=True
        )