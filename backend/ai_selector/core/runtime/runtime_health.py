"""
Runtime Health Monitor

Stage23 Reliability + Stage34 Autonomous Runtime
"""
from datetime import datetime


class RuntimeHealth:


    def __init__(self):

        self.status = {}

        self.errors = {}

        self.run_completed = False

        self.last_run = None


    def update(
        self,
        component,
        state
    ):

        self.status[component] = state



    def get(
        self,
        component
    ):

        return self.status.get(component)



    def snapshot(self):

        return self.status.copy()



    # Stage23 compatibility

    def record_error(
        self,
        component,
        error
    ):

        self.status[component] = "ERROR"

        self.errors[component] = str(error)



    def mark_run_complete(self):

        self.run_completed = True

        self.last_run = datetime.now().isoformat()


    def report(self):

        degraded = (
            len(self.errors) > 0
            or any(
                value == "ERROR"
                for value in self.status.values()
            )
        )


        overall = (
            "DEGRADED"
            if degraded
            else "HEALTHY"
        )


        return {
            "status": overall,
            "components": self.status.copy(),
            "errors": self.errors.copy(),
            "completed": self.run_completed,
            "last_run": self.last_run
        }