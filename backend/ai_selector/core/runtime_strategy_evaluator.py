class RuntimeStrategyEvaluator:


    def evaluate(self, strategy):

        score = 0


        if strategy:
            score = 1


        return {

            "strategy_score": score,

            "accepted": score > 0

        }