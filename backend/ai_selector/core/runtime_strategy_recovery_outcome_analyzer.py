class RuntimeStrategyRecoveryOutcomeAnalyzer:
    """
    Analyze autonomous recovery execution outcomes.
    """

    def __init__(self):
        self.history = []


    def analyze(self, result):

        status = result.get(
            "status"
        )

        action = result.get(
            "action"
        )


        if status == "success":

            analysis = {
                "action": action,
                "success": True,
                "score": 1.0,
                "recommendation": "keep"
            }

        else:

            analysis = {
                "action": action,
                "success": False,
                "score": 0.0,
                "recommendation": "retry"
            }


        self.history.append(
            analysis
        )

        return analysis



    def analysis_history(self):

        return self.history