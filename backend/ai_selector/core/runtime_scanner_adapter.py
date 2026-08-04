class RuntimeScannerAdapter:


    def __init__(self):

        self.runtime_config = None


    def bind(self, config):

        self.runtime_config = config

        return {
            "bound": True,
            "strategy": config["strategy"]
        }


    def get_strategy(self):

        return self.runtime_config