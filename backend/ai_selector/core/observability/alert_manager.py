"""
Alert Manager

Stage24 Production Observability
"""


from datetime import datetime


class AlertManager:

    def __init__(self):
        self.alerts = []


    def check(
        self,
        metric,
        value,
        threshold
    ):

        if value >= threshold:

            alert = {
                "metric": metric,
                "value": value,
                "threshold": threshold,
                "time": datetime.now().isoformat(),
            }

            self.alerts.append(alert)

            return alert

        return None


    def history(self):

        return self.alerts