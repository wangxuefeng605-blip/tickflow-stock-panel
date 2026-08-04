class RuntimeStrategyRecoveryDecisionExecutionFeedbackCollector:
    """
    Collect recovery execution feedback.
    """

    def __init__(self):
        self.history = []


    def collect(self, execution):

        policy = execution.get(
            "policy"
        )

        result = execution.get(
            "status",
            "UNKNOWN"
        )


        if result == "SUCCESS":

            feedback = "POSITIVE"

        elif result == "FAILED":

            feedback = "NEGATIVE"

        else:

            feedback = "NEUTRAL"


        record = {
            "policy": policy,
            "result": result,
            "feedback": feedback
        }


        self.history.append(
            record
        )


        return record


    def get_history(self):

        return self.history