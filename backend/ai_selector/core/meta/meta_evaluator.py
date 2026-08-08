"""
Meta Evaluator

Evaluate whether adaptation itself is effective.
"""


class MetaEvaluator:


    def evaluate(
        self,
        before,
        after
    ):

        improvement = round(
            after - before,
            6
        )


        return {

            "improvement":
                improvement,

            "should_keep":
                improvement > 0,

            "score":
                improvement
        }