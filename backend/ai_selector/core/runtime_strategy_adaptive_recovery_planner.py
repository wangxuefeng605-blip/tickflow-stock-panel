class RuntimeStrategyAdaptiveRecoveryPlanner:
    """
    Adaptive recovery planner.
    Select best recovery action according to historical results.
    """

    def __init__(self):
        self.history = []


    def plan(self, context):

        recovery_history = context.get(
            "history",
            []
        )


        if not recovery_history:

            result = {
                "selected_action": "fallback",
                "confidence": 0.5
            }

        else:

            scores = {}

            for item in recovery_history:

                action = item.get(
                    "action"
                )

                success = item.get(
                    "success",
                    False
                )

                if action not in scores:
                    scores[action] = {
                        "success": 0,
                        "total": 0
                    }


                scores[action]["total"] += 1

                if success:
                    scores[action]["success"] += 1


            best_action = None
            best_score = -1


            for action, data in scores.items():

                score = (
                    data["success"]
                    /
                    data["total"]
                )

                if score > best_score:

                    best_score = score
                    best_action = action


            result = {
                "selected_action": best_action,
                "confidence": best_score
            }


        self.history.append(result)

        return result



    def planner_history(self):

        return self.history