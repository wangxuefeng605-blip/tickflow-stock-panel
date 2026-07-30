class LearningDecisionPipeline:

    def run(
        self,
        stock,
        learning_state,
        context
    ):

        adjusted = apply_learning()

        decision = engine.decide(
            adjusted,
            context
        )

        return decision