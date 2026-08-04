class RuntimeStrategyAutoResponseEngine:
    """
    Runtime strategy automatic response engine.

    Converts alerts into operational actions.
    """

    def __init__(self):
        self.responses = []


    def handle(self, alert):

        level = alert.get(
            "level"
        )

        alert_type = alert.get(
            "type"
        )


        action = "ignore"


        if level == "warning":

            if alert_type == "reward_drift":
                action = "adjust_parameters"

            elif alert_type == "behavior_deviation":
                action = "recalibrate_strategy"



        elif level == "critical":

            if alert_type == "execution_failure_spike":
                action = "fallback_strategy"

            else:
                action = "emergency_stop"



        response = {

            "action": action,

            "source": alert_type,

            "level": level
        }


        self.responses.append(
            response
        )


        return response



    def history(self):

        return self.responses