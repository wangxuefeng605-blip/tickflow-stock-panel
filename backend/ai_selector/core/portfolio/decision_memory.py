class DecisionMemory:


    def __init__(self):

        self.history=[]



    def save(self,decision):

        self.history.append(
            decision
        )


    def all(self):

        return self.history