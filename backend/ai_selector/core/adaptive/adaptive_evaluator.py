"""
Adaptive Evaluator

Stage36 Adaptive Intelligence
"""


class AdaptiveEvaluator:


    def evaluate(
        self,
        performance
    ):


        if performance >= 0.8:

            level = "EXCELLENT"

            should_adjust = False


        elif performance >= 0.5:

            level = "NORMAL"

            should_adjust = False


        else:

            level = "WEAK"

            should_adjust = True



        return {

            "performance":
                performance,

            "level":
                level,

            "should_adjust":
                should_adjust
        }