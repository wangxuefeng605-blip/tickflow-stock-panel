class ScannerLearningRuntimeAdapter:


    def __init__(self):

        self.pipeline = LearningPipelineAssembly()



    def process(self, stock):

        return self.pipeline.execute(stock)