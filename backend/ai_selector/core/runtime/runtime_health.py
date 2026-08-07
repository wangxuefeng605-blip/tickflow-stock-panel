"""
Runtime Health Monitor

Stage23 Production Reliability Layer
"""

from datetime import datetime


class RuntimeHealth:
    """
    Runtime component health tracker
    """

    def __init__(self):
        self.status = {
            "scanner": "UNKNOWN",
            "ranking": "UNKNOWN",
            "learning": "UNKNOWN",
            "cache": "UNKNOWN",
        }

        self.last_run = None
        self.errors = []

    def update(self, component: str, state: str):
        """
        Update component status
        """

        if component in self.status:
            self.status[component] = state

    def record_error(self, component: str, error):
        """
        Record runtime error
        """

        self.errors.append(
            {
                "component": component,
                "error": str(error),
                "time": datetime.now().isoformat(),
            }
        )

        self.update(component, "ERROR")

    def mark_run_complete(self):
        self.last_run = datetime.now().isoformat()

    def is_healthy(self):
        """
        Check overall runtime health
        """

        return (
            all(
                value == "OK"
                for value in self.status.values()
            )
            and not self.errors
        )

    def report(self):
        """
        Generate health report
        """

        return {
            "status": (
                "HEALTHY"
                if self.is_healthy()
                else "DEGRADED"
            ),
            "components": self.status,
            "last_run": self.last_run,
            "errors": self.errors,
        }