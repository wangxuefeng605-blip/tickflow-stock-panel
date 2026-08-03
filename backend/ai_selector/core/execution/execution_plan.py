class ExecutionPlan:

    def __init__(
        self,
        code,
        action=None,
        confidence=0,
        side=None,
        status="CREATED"
    ):

        self.code = code

        # 兼容 action / side 两套命名
        self.action = action or side
        self.side = self.action

        self.confidence = confidence
        self.status = status