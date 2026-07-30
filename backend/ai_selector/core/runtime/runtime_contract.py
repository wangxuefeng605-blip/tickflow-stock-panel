class RuntimeRequest:

    def __init__(
        self,
        code,
        features=None
    ):
        self.code = code
        self.features = features or {}