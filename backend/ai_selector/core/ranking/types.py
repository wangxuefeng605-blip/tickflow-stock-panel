from dataclasses import dataclass, field



from dataclasses import dataclass, field


from dataclasses import dataclass


@dataclass
class RankingResult:

    code: str

    score: float

    rank: int

    factors: dict

    signals: list = None

    market_state: str = "UNKNOWN"

    confidence: float = 0

    explanation: dict = None

    reason: str = ""