class AIRuntimeGovernor:


    def evaluate(
        self,
        runtime_state
    ):

        success_rate = runtime_state.get(
            "success_rate",
            0
        )

        retry_count = runtime_state.get(
            "retry_count",
            0
        )


        if success_rate >= 0.95 and retry_count < 5:

            return {

                "decision": "AGGRESSIVE",

                "workers": 8,

                "confidence": 0.9

            }


        return {

            "decision": "CONSERVATIVE",

            "workers": 2,

            "confidence": 0.7

        }