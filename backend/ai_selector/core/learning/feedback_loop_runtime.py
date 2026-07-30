class FeedbackLoopRuntime:

    def process(
        self,
        trade_result
    ):
        reward = self.calculate_reward(
            trade_result
        )

        self.state_manager.update_reward(
            reward
        )

        self.optimizer.update(
            weights,
            feedback
        )

        persistence.save(
            state
        )