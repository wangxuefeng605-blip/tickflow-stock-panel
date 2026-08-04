from core.runtime.runtime_service import RuntimeService


class RuntimeAPI:

    def __init__(self):
        self.service = RuntimeService()


    def execute(self, stock):

        result = self.service.execute(stock)

        return {
            **result,
            "api_completed": True
        }