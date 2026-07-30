from .decision_loop import LearningDecisionLoop


class LearningDecisionPipeline:


    def __init__(self):

        self.loop = LearningDecisionLoop()



    def process(
        self,
        result
    ):

        return self.loop.process(
            result
        )



    def run(
        self,
        stock,
        learning_state,
        context
    ):

        return self.process(
            stock
        )