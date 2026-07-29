from dataclasses import dataclass


@dataclass
class AIDecision:

    code: str

    action: str

    confidence: float

    score: float

    reason: str