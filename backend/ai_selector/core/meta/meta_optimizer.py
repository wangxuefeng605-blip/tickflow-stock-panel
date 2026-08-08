"""
Meta Optimizer

Optimize parameters based on meta evaluation.
"""


class MetaOptimizer:


    def optimize(
        self,
        parameters,
        score
    ):

        updated = dict(parameters)


        if score > 0:

            for key in updated:
                updated[key] += 0.01


        return {

            "parameters": updated,

            "optimized":
                score > 0
        }