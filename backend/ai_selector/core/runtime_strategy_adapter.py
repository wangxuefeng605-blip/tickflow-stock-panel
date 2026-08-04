class RuntimeStrategyAdapter:


    def adapt(
        self,
        learning_result
    ):

        mode = learning_result.get(
            "preferred_mode",
            "SAFE"
        )


        confidence = learning_result.get(
            "confidence",
            0
        )


        if mode == "AGGRESSIVE" and confidence >= 0.5:

            return {

                "workers":8,

                "retry_enabled":True,

                "scan_depth":"FULL"

            }


        return {

            "workers":2,

            "retry_enabled":True,

            "scan_depth":"SAFE"

        }