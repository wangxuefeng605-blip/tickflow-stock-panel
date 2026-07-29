class Simulator:


    def simulate(
        self,
        signals
    ):

        trades=[]

        for item in signals:

            trades.append(
                {
                    "code":item["code"],
                    "return":item.get(
                        "return",
                        0
                    )
                }
            )


        return trades