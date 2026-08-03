class DecisionLearningBridge:


    def __init__(
        self,
        weight_provider
    ):

        self.weight_provider = weight_provider



    def apply(
        self,
        feedback
    ):


        if feedback.get(
            "success"
        ):

            current = (
                self.weight_provider.get_weights()
            )


            self.weight_provider.update(
                {
                    "momentum":
                        current.get(
                            "momentum",
                            1
                        )
                        +
                        0.05,


                    "trend":
                        current.get(
                            "trend",
                            1
                        )
                        +
                        0.02
                }
            )


        return (
            self.weight_provider.get_weights()
        )