class RealtimeExecutor:

    def __init__(self):
        pass


    def execute(self, decision):

        return {
            "action": decision["action"],
            "status": "EXECUTED"
        }