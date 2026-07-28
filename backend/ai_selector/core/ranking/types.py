from dataclasses import dataclass, field


@dataclass
class RankingResult:

    code: str

    score: float

    ai_score: float = 0.0

    rank: int = 0

    confidence: float = 0.0

    market_state: str = "UNKNOWN"

    signals: list[str] = field(
        default_factory=list
    )

    risks: list[str] = field(
        default_factory=list
    )

    factors: dict = field(
        default_factory=dict
    )

    ranking_reason: str = ""

    explanation: dict = field(
        default_factory=dict
    )