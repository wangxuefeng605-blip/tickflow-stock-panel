class StrategyRegistry:

    def __init__(self):

        self.active = None
        self.candidates = []
        self.history = []


    def register_candidate(
        self,
        policy
    ):

        self.candidates.append(
            policy
        )


    def activate(
        self,
        policy
    ):

        if self.active:
            self.history.append(
                self.active
            )

        self.active = policy


    def get_active(self):

        return self.active