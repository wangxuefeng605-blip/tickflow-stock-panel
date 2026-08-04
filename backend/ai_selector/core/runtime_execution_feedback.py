class RuntimeExecutionFeedback:


    def record(
        self,
        result
    ):

        return {

            "execution_success":
                result.get(
                    "execution_completed",
                    False
                ),

            "tasks_completed":
                len(
                    result.get(
                        "plan",
                        {}
                    ).get(
                        "tasks",
                        []
                    )
                ),

            "feedback_ready": True

        }