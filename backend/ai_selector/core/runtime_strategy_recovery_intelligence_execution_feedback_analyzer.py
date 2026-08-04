class RuntimeStrategyRecoveryIntelligenceExecutionFeedbackAnalyzer:
    """
    Analyzes recovery execution feedback.
    """

    def __init__(self):

        self.history = []


    def analyze(self, runtime):

        if runtime.get("health"):

            result = {
                "success_rate": 1.0,
                "strategy_score": 1.0,
                "failure_reason": None,
                "learning_feedback": "positive"
            }

        else:

            alerts = runtime.get(
                "alerts",
                []
            )

            result = {
                "success_rate": 0.0,
                "strategy_score": 0.0,
                "failure_reason": (
                    alerts[0]
                    if alerts
                    else "unknown"
                ),
                "learning_feedback": "negative"
            }


        self.history.append(result)

        return result


    def get_history(self):

        return self.history