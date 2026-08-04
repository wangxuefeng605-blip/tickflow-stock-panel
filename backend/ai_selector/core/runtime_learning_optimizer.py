from .runtime_decision_feedback import RuntimeDecisionFeedback


class RuntimeLearningOptimizer:


    def __init__(self):

        self.feedback = RuntimeDecisionFeedback()



    def optimize(self):

        data = []

        latest = self.feedback.latest()

        if latest:
            data.append(latest)


        if not data:

            return {
                "preferred_mode":"SAFE",
                "confidence":0
            }


        success = sum(
            1 for x in data
            if x.get("success")
        )


        confidence = success / len(data)


        mode = "AGGRESSIVE"

        if confidence < 0.5:
            mode = "SAFE"


        return {

            "preferred_mode": mode,

            "confidence": confidence

        }