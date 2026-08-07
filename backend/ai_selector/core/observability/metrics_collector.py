"""
Runtime Metrics Collector

Stage24 Production Observability
"""


from datetime import datetime


class MetricsCollector:

    def __init__(self):
        self.metrics = {
            "scanner_latency": 0,
            "ranking_time": 0,
            "learning_accuracy": 0,
            "recovery_count": 0,
            "error_count": 0,
        }

        self.timestamp = None


    def record(
        self,
        name: str,
        value
    ):

        if name in self.metrics:
            self.metrics[name] = value

        self.timestamp = datetime.now().isoformat()


    def increment(
        self,
        name: str,
        amount=1
    ):

        if name in self.metrics:
            self.metrics[name] += amount

        self.timestamp = datetime.now().isoformat()


    def snapshot(self):

        return {
            "metrics": self.metrics,
            "timestamp": self.timestamp,
        }