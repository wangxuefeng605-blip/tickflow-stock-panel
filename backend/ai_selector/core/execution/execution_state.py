class ExecutionState:

    def __init__(self):

        self.history = []


    def update(
        self,
        plan
    ):

        self.history.append(plan)



class ExecutionTracker(ExecutionState):

    pass