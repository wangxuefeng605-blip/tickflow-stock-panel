class AutonomyState:
    """
    Autonomous evolution runtime state
    """

    def __init__(self):
        self.cycle = 0
        self.status = "INIT"

        self.learning_score = 0.0
        self.adaptation_score = 0.0
        self.evolution_score = 0.0

        self.generation = 0

    def update(
        self,
        learning_score=None,
        adaptation_score=None,
        evolution_score=None
    ):
        if learning_score is not None:
            self.learning_score = learning_score

        if adaptation_score is not None:
            self.adaptation_score = adaptation_score

        if evolution_score is not None:
            self.evolution_score = evolution_score

    def next_cycle(self):
        self.cycle += 1
        self.status = "RUNNING"

    def complete(self):
        self.status = "SUCCESS"

    def snapshot(self):

        return {
            "cycle": self.cycle,
            "status": self.status,
            "learning_score": self.learning_score,
            "adaptation_score": self.adaptation_score,
            "evolution_score": self.evolution_score,
            "generation": self.generation
        }