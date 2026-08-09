class RealtimeDecisionEngine:

    def decide(self, item):

        score = item["score"]

        if score >= 80:
            action = "BUY"

        elif score >= 50:
            action = "WATCH"

        else:
            action = "DROP"


        return {
            "code": item["code"],
            "score": score,
            "action": action
        }