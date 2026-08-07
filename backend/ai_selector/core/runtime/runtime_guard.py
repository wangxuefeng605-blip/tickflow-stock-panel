"""
Runtime Guard

Stage23 Production Reliability
"""

from core.runtime.runtime_health import RuntimeHealth


class RuntimeGuard:

    def __init__(self):
        self.health = RuntimeHealth()


    def run(self, component, func, fallback=None):

        try:

            result = func()

            self.health.update(
                component,
                "OK"
            )

            return result


        except Exception as e:

            self.health.record_error(
                component,
                e
            )

            return fallback


    def report(self):

        return self.health.report()