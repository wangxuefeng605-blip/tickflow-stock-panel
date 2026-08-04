class RuntimeStrategyAnomalyDetector:
    """
    Runtime strategy anomaly detection.

    Detect:
    - reward drift
    - execution failure spike
    - behavior deviation
    """

    def __init__(self):
        self.events = []


    def detect_reward_drift(
        self,
        rewards,
        threshold=0.3
    ):

        if len(rewards) < 2:
            return {
                "anomaly": False
            }


        start = rewards[0]
        end = rewards[-1]


        if start == 0:
            return {
                "anomaly": False
            }


        drop = (
            start - end
        ) / start


        if drop >= threshold:

            event = {
                "anomaly": True,
                "type": "reward_drift",
                "drop": round(drop, 4)
            }

            self.events.append(event)

            return event


        return {
            "anomaly": False
        }



    def detect_execution_failure(
        self,
        executions
    ):

        if len(executions) < 3:

            return {
                "anomaly": False
            }


        failures = sum(
            1 for x in executions
            if not x
        )


        rate = (
            failures /
            len(executions)
        )


        if rate >= 0.5:

            event = {
                "anomaly": True,
                "type": "execution_failure_spike",
                "failure_rate": rate
            }

            self.events.append(event)

            return event


        return {
            "anomaly": False
        }



    def detect_behavior_deviation(
        self,
        current,
        expected
    ):

        if current != expected:

            event = {
                "anomaly": True,
                "type": "behavior_deviation"
            }

            self.events.append(event)

            return event


        return {
            "anomaly": False
        }



    def report(self):

        return {
            "count": len(self.events),
            "events": self.events
        }