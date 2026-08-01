from dataclasses import dataclass



@dataclass
class LearningFeedback:

    source: str

    signal: dict



@dataclass
class FeedbackEvent:

    strategy: str

    score: float

    adjustment: float

    return_rate: float = 0

    max_drawdown: float = 0

    win_rate: float = 0

    source: str = "learning"



class FeedbackEngine:


    def __init__(self):

        self.events = []


    def generate(self, signal):

        event = FeedbackEvent(

            strategy=signal.strategy,

            score=signal.score,

            adjustment=signal.score,

            return_rate=signal.return_rate,

            max_drawdown=signal.max_drawdown,

            win_rate=signal.win_rate

        )


        self.events.append(event)

        return event



class Feedback:

    def __init__(
        self,
        reward,
        factor
    ):

        self.reward = reward

        self.factor = factor

        self.adjustment = reward * 0.1



def evaluate_prediction(
    entry,
    future
):
    """
    Evaluate prediction result.
    """

    if entry == 0:

        return {
            "entry": entry,
            "future": future,
            "return": 0,
            "success": False,
            "direction": "UNKNOWN"
        }


    change = (
        future - entry
    ) / entry


    return {

        "entry": entry,

        "future": future,

        "return": change,

        "success": change > 0,

        "direction":
            "UP"
            if change > 0
            else "DOWN"

    }