"""
Runtime Dashboard

Stage24 Production Observability
"""


class RuntimeDashboard:

    def __init__(
        self,
        snapshot,
        metrics,
        analyzer,
        alerts
    ):

        self.snapshot = snapshot
        self.metrics = metrics
        self.analyzer = analyzer
        self.alerts = alerts


    def generate(self):

        performance = (
            self.analyzer.analyze(
                self.metrics
            )
        )

        return {
            "runtime":
                (
                    "HEALTHY"
                    if not self.alerts
                    else "DEGRADED"
                ),

            "performance":
                performance,

            "alerts":
                self.alerts,

            "components":
                self.snapshot,
        }