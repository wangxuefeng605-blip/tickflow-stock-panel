class RuntimeStrategyAlertManager:
    """
    Runtime strategy alert management.

    Responsibilities:
    - convert anomaly events to alerts
    - classify severity
    - store alert history
    """

    def __init__(self):
        self.alerts = []


    def create_alert(self, event):

        event_type = event.get(
            "type"
        )

        level = "info"


        if event_type == "reward_drift":

            level = "warning"


        elif event_type == "execution_failure_spike":

            failure_rate = event.get(
                "failure_rate",
                0
            )

            if failure_rate >= 0.8:
                level = "critical"
            else:
                level = "warning"


        elif event_type == "behavior_deviation":

            level = "warning"


        alert = {

            "level": level,

            "type": event_type,

            "event": event
        }


        self.alerts.append(alert)


        return alert



    def latest(self):

        if not self.alerts:

            return None


        return self.alerts[-1]



    def history(self):

        return self.alerts