class RuntimeHealthMonitor:


    def check(
        self,
        runtime_state
    ):

        if runtime_state is None:
            runtime_state = {}


        healthy = runtime_state.get(
            "runtime_healthy",
            False
        )


        return {

            "health_checked": True,

            "runtime_healthy": healthy,

            "status":
                "READY"
                if healthy
                else "DEGRADED"

        }