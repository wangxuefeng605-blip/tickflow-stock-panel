"""
Learning Decision Engine

Decide whether learning adjustment
should be applied.
"""


class LearningDecisionEngine:


    def __init__(
        self,
        min_win_rate=0.55,
        min_return=0
    ):

        self.min_win_rate = min_win_rate
        self.min_return = min_return



    def decide(
        self,
        summary
    ):

        win_rate = summary.get(
            "win_rate",
            0
        )

        avg_return = summary.get(
            "average_return",
            0
        )


        if (
            win_rate >= self.min_win_rate
            and
            avg_return > self.min_return
        ):

            return {

                "decision":
                    "accept",

                "reason":
                    "positive performance",

                "win_rate":
                    win_rate,

                "average_return":
                    avg_return

            }


        return {

            "decision":
                "hold",

            "reason":
                "insufficient performance",

            "win_rate":
                win_rate,

            "average_return":
                avg_return

        }



if __name__ == "__main__":


    engine = LearningDecisionEngine()


    print(
        engine.decide(
            {
                "win_rate":0.6,
                "average_return":0.0256
            }
        )
    )