class RuntimeStrategySelfHealingValidator:
    """
    Validate runtime strategy self healing result.
    """

    def __init__(self):
        self.history = []


    def validate(self, healing_result):

        status = healing_result.get(
            "status"
        )

        if status == "healed":

            result = {
                "valid": True,
                "health": "healthy",
                "confidence": 1.0
            }

        elif status == "rollback":

            result = {
                "valid": False,
                "health": "degraded",
                "confidence": 0.0
            }

        else:

            result = {
                "valid": False,
                "health": "unknown",
                "confidence": 0.5
            }


        self.history.append(result)

        return result



    def validation_history(self):

        return self.history