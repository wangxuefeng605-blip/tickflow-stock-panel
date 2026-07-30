from core.runtime.runtime_entry import RuntimeEntry


class RuntimeFacade:


    def __init__(self):

        self.entry = RuntimeEntry()



    def execute(
        self,
        stock
    ):

        result = self.entry.execute(
            stock
        )


        return {
            **result,
            "facade_completed": True
        }