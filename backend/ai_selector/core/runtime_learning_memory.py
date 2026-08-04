class RuntimeLearningMemory:


    def __init__(self):

        self.history = []



    def store(self, feedback):

        self.history.append(
            feedback
        )


        return {

            "stored": True,

            "total_records":
                len(self.history)

        }



    def summary(self):

        return {

            "records":
                len(self.history)

        }