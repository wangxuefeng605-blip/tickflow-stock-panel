"""
Adaptive Recovery Strategy

Stage26 Self-Healing Intelligence
"""


class AdaptiveRecoveryStrategy:


    def __init__(self):

        self.history = {}



    def decide(
        self,
        failure
    ):

        failure_type = failure.get(
            "type",
            "UNKNOWN_ERROR"
        )


        if failure_type not in self.history:

            self.history[failure_type] = {
                "success": 0,
                "failure": 0
            }


        stats = self.history[
            failure_type
        ]


        retry = self.calculate_retry(
            stats
        )


        return {
            "failure_type":
                failure_type,

            "retry":
                retry,

            "action":
                failure.get(
                    "action",
                    "RETRY"
                )
        }



    def calculate_retry(
        self,
        stats
    ):

        total = (
            stats["success"]
            +
            stats["failure"]
        )


        if total == 0:
            return 3


        success_rate = (
            stats["success"]
            /
            total
        )


        if success_rate < 0.5:
            return 5


        return 3



    def record_result(
        self,
        failure_type,
        success
    ):

        if failure_type not in self.history:

            self.history[failure_type] = {
                "success":0,
                "failure":0
            }


        if success:

            self.history[
                failure_type
            ]["success"] += 1

        else:

            self.history[
                failure_type
            ]["failure"] += 1