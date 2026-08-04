class RuntimeLearningFeedbackProcessor:


    def process(self, feedback):

        score = feedback.get(
            "score",
            0
        )

        reward = 1 if score >= 80 else 0


        return {
            "processed": True,
            "reward": reward,
            "score": score
        }