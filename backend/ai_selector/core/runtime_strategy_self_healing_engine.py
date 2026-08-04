class RuntimeStrategySelfHealingEngine:
    """
    Runtime strategy self healing engine.
    """

    def __init__(self):
        self.history = []


    def heal(self, recovery_request):

        action = recovery_request.get(
            "action"
        )

        success = recovery_request.get(
            "success",
            True
        )


        if success:

            result = {
                "status": "healed",
                "action": action
            }

        else:

            result = {
                "status": "rollback",
                "action": action
            }


        self.history.append(
            result
        )

        return result



    def healing_history(self):

        return self.history