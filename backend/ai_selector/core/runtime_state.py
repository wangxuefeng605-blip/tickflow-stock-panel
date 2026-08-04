class RuntimeStateAggregator:


    def build(
        self,
        health=None,
        metrics=None,
        healing=None
    ):

        health = health or {}

        metrics = metrics or {}

        healing = healing or {}


        total = metrics.get(
            "total_runs",
            0
        )

        success = metrics.get(
            "success_runs",
            0
        )


        success_rate = 0

        if total > 0:
            success_rate = success / total


        return {

            "runtime_status":
                "READY"
                if health.get("runtime_healthy")
                else "DEGRADED",

            "health":
                health.get(
                    "status",
                    "UNKNOWN"
                ),

            "total_runs": total,

            "success_rate": success_rate,

            "retry_count":
                metrics.get(
                    "retry_count",
                    0
                ),

            "self_healing":
                healing.get(
                    "self_healing_completed",
                    False
                )

        }