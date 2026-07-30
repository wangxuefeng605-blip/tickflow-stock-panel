from core.runtime.runtime_bootstrap import create_runtime


class RuntimeBridge:


    def __init__(self):

        self.runtime = create_runtime()



    def execute(
        self,
        stock
    ):

        result = self.runtime.execute(
            stock
        )


        return {
            **result,
            "bridge_completed": True
        }