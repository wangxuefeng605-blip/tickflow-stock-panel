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

        return self.engine.execute(
            decision
        )