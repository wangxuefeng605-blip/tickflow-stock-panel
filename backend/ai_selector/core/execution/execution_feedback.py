"""
Execution Feedback

Stage31 Autonomous Execution Intelligence
"""


class ExecutionFeedback:


    def collect(
        self,
        execution
    ):

        price = execution.get(
            "price",
            0
        )

        exit_price = execution.get(
            "exit_price",
            price
        )


        reward = 0

        if price:

            reward = (
                exit_price - price
            ) / price


        status = "SUCCESS"

        if reward < 0:

            status = "LOSS"


        return {

            "symbol": execution.get(
                "symbol"
            ),

            "action": execution.get(
                "action"
            ),

            "reward": reward,

            "status": status
        }