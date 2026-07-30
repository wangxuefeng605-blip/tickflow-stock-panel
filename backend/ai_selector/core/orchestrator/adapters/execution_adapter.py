class ExecutionAdapter:


    def __init__(
        self,
        engine
    ):
        self.engine = engine



    def execute(
        self,
        decision
    ):

        if not isinstance(
            decision,
            list
        ):
            decision = [
                decision
            ]


        return self.engine.execute(
            decision
        )