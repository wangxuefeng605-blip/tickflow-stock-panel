class LearningOrchestratorHook:

    def after_execution(self, result):
        return {
            **result,
            "learning_updated": True
        }

    def after_backtest(self, result):
        return {
            **result,
            "learning_updated": True
        }

    def update_ranking(self):
        return True