class PolicyState:

    def __init__(
        self,
        version="v1",
        weights=None,
        score=0.0,
        active=True
    ):

        self.version = version

        self.weights = weights or {
            "momentum": 0.35,
            "trend": 0.30,
            "risk": 0.10
        }

        self.score = score
        self.active = active


    def update_score(self, score):

        self.score = score


    def activate(self):

        self.active = True


    def deactivate(self):

        self.active = False


    def snapshot(self):

        return {
            "version": self.version,
            "weights": self.weights,
            "score": self.score,
            "active": self.active
        }