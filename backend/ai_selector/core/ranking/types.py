from dataclasses import dataclass, field


@dataclass
class RankingResult:

    code: str

    score: float

    rank: int = 0

    factors: dict = field(
        default_factory=dict
    )


    signals: list = field(
        default_factory=list
    )

    market_state: str = "UNKNOWN"

    confidence: float = 0

    explanation: dict = field(
        default_factory=dict
    )

    reason: str = ""

    ranking_reason: str = ""