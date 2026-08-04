class AdaptiveScannerController:


    def decide(
        self,
        runtime_state
    ):

        status = runtime_state.get(
            "runtime_status",
            "DEGRADED"
        )


        if status == "READY":

            return {

                "scanner_mode": "NORMAL",

                "workers": 8,

                "allow_retry": True

            }


        return {

            "scanner_mode": "SAFE",

            "workers": 2,

            "allow_retry": True

        }