class RuntimeStrategyHealthMonitor:
    """
    Runtime strategy health monitoring.

    Responsibilities:
    - calculate health score
    - detect degradation
    - report strategy status
    """

    def __init__(self):

        self.history = []


    def evaluate(self, metrics):

        execution = metrics.get(
            "execution_success_rate",
            0
        )

        reward = metrics.get(
            "reward_score",
            0
        )

        stability = metrics.get(
            "stability",
            0
        )


        health_score = (
            execution * 0.4
            +
            reward * 0.4
            +
            stability * 0.2
        )


        status = "healthy"


        if health_score < 0.5:

            status = "degraded"


        result = {

            "health_score": round(
                health_score,
                4
            ),

            "status": status
        }


        self.history.append(result)


        return result



    def detect_anomaly(self):

        if len(self.history) < 2:

            return {
                "anomaly": False
            }


        current = (
            self.history[-1]
            ["health_score"]
        )

        previous = (
            self.history[-2]
            ["health_score"]
        )


        if current < previous * 0.7:

            return {
                "anomaly": True,
                "reason": "health_drop"
            }


        return {
            "anomaly": False
        }



    def report(self):

        if not self.history:

            return {
                "status": "unknown"
            }


        return self.history[-1]