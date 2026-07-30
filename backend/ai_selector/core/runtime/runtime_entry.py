from core.runtime.runtime_api import RuntimeAPI


class RuntimeEntry:


    def __init__(self):

        self.api = RuntimeAPI()



    def execute(
        self,
        stock
    ):

        result = self.api.execute(
            stock
        )


        return {
            **result,
            "entry_completed": True
        }