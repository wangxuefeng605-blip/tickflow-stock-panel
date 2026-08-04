class RetryFeedback:


    def process(
        self,
        retry_result
    ):

        if retry_result is None:
            retry_result = {}


        return {

            "feedback_received": True,

            "retry_completed": retry_result.get(
                "retry_completed",
                False
            ),

            "retry_count": retry_result.get(
                "retry_count",
                0
            )

        }