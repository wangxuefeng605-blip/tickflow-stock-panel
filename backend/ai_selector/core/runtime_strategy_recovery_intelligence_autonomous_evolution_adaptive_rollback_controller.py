class RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveRollbackController:
    """
    Controls autonomous evolution rollback and recovery.
    """

    def __init__(self):

        self.checkpoints = []
        self.history = []


    def save_checkpoint(self, strategy):

        self.checkpoints.append(
            strategy
        )


        self.history.append(
            {
                "action": "checkpoint",
                "strategy": strategy
            }
        )


        return strategy



    def rollback(self):

        if not self.checkpoints:

            return None


        strategy = self.checkpoints[-1]


        result = {

            "recovered": strategy,

            "status": "rollback_completed"

        }


        self.history.append(
            {
                "action": "rollback",
                "strategy": strategy
            }
        )


        return result



    def get_best_checkpoint(self):

        if not self.checkpoints:

            return None


        return self.checkpoints[-1]



    def get_history(self):

        return self.history