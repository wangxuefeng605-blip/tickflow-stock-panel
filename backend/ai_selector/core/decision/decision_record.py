from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class DecisionRecord:

    code: str

    action: str

    score: float

    confidence: float = 0

    market_state: str = "UNKNOWN"

    signals: list = field(
        default_factory=list
    )

    weights: dict = field(
        default_factory=dict
    )

    timestamp: str = field(
        default_factory=lambda:
            datetime.now().isoformat()
    )


    def to_dict(self):

        return {

            "code": self.code,

            "action": self.action,

            "score": self.score,

            "confidence": self.confidence,

            "market_state": self.market_state,

            "signals": self.signals,

            "weights": self.weights,

            "timestamp": self.timestamp

        }