class ExecutionPlan:

    def __init__(
        self,
        code,
        side,
        status="CREATED"
    ):
        self.code = code
        self.side = side
        self.status = status