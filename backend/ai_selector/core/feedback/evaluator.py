class FeedbackEvaluator:


    def evaluate(self, records):

        if not records:
            return {
                "score":0,
                "count":0
            }


        success = sum(
            1
            for r in records
            if r["result"]
        )


        return {
            "score":
                success / len(records),

            "count":
                len(records)
        }