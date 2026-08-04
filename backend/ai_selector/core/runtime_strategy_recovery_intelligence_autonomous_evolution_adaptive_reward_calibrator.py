class RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveRewardCalibrator:
    """
    Calibrates rewards from execution feedback.
    """

    def __init__(self):

        self.history = []


    def calibrate(self, feedback):

        performance = feedback.get(
            "performance",
            0
        )

        signal = feedback.get(
            "improvement_signal"
        )


        reward = performance


        if signal == "increase":

            reward = min(
                reward + 0.1,
                1.0
            )


        elif signal == "adjust":

            reward = max(
                reward - 0.1,
                0
            )


        result = {

            "strategy": feedback.get(
                "strategy"
            ),

            "reward": round(
                reward,
                2
            ),

            "calibrated": True

        }


        self.history.append(
            result
        )


        return result



    def get_history(self):

        return self.history