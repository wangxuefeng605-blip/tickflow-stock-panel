"""
Feedback Evaluator

Stage54:
Feedback Learning Integration
"""


class FeedbackEvaluator:


    def evaluate(self, records):

        if not records:
            return {
                "count":0,
                "success":0,
                "accuracy":0,
                "score":0,
                "average_score":0
            }


        success = sum(
            1
            for r in records
            if (
                r.get("result") is True
                or
                r.get("actual_result")
                in (
                    "WIN",
                    "SUCCESS",
                    "PROFIT"
                )
            )
        )


        total_score = sum(
            float(
                r.get(
                    "score",
                    0
                )
            )
            for r in records
        )


        count = len(records)


        accuracy = success / count


        return {

            "count":
                count,

            "success":
                success,

            "accuracy":
                accuracy,

            "score":
                accuracy,

            "average_score":
                total_score / count

        }