"""
Healing Feedback Learning

Stage26 Self-Healing Intelligence
"""


class HealingFeedback:


    def __init__(self):

        self.records = []



    def record(
        self,
        failure,
        decision,
        success
    ):

        self.records.append(
            {
                "failure": failure,
                "decision": decision,
                "success": success
            }
        )



    def success_rate(self):

        if not self.records:
            return 0


        success = sum(
            1
            for r in self.records
            if r["success"]
        )


        return (
            success
            /
            len(self.records)
        )



    def recommend(self):

        rate = self.success_rate()


        if rate >= 0.8:

            return {
                "mode":
                    "KEEP"
            }


        return {
            "mode":
                "ADAPT"
        }