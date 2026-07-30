from core.learning.runtime import LearningRuntime


class LearningPipeline:


    def __init__(self):

        self.runtime = LearningRuntime()



    def update(
        self,
        feedback,
        weights
    ):

        return self.runtime.process(
            feedback=feedback,
            weights=weights
        )