class StrategyValidator:

    def __init__(
        self,
        min_score=0.5
    ):
        self.min_score = min_score


    def validate(
        self,
        policy
    ):

        return (
            policy.score >= self.min_score
        )