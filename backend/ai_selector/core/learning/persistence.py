class LearningPersistence:


    def __init__(self):

        self._state = None



    def save(
        self,
        state
    ):

        self._state = state



    def load(
        self
    ):

        return self._state