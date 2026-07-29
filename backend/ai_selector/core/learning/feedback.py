from dataclasses import dataclass


@dataclass
class FeedbackEvent:

    strategy: str

    score: float

    adjustment: float



class FeedbackEngine:


    def generate(
        self,
        signal
    ):

        adjustment = (
            signal.score
        )

        return FeedbackEvent(
            strategy=signal.strategy,
            score=signal.score,
            adjustment=adjustment
        )