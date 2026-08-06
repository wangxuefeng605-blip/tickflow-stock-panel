"""
Portfolio Performance Evaluator

Evaluate historical AI recommendations.
"""


class PerformanceEvaluator:

    def evaluate(self, feedbacks):
        """
        Evaluate portfolio feedback list.

        feedback example:

        {
            "code": "000001",
            "score": 90,
            "return": 0.08
        }
        """

        if not feedbacks:
            return {
                "total": 0,
                "success": 0,
                "success_rate": 0,
                "avg_return": 0,
                "avg_score": 0,
            }

        total = len(feedbacks)

        success = 0
        total_return = 0
        total_score = 0

        for item in feedbacks:

            ret = item.get(
                "return",
                0
            )

            score = item.get(
                "score",
                0
            )

            total_return += ret
            total_score += score

            if ret > 0:
                success += 1

        return {
            "total": total,
            "success": success,
            "success_rate": success / total,
            "avg_return": total_return / total,
            "avg_score": total_score / total,
        }