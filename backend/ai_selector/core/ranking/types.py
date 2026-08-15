from dataclasses import dataclass, field


@dataclass
class RankingResult:

    code: str

    score: float

    rank: int = 0

    ranking_reason: list = field(
        default_factory=list
    )

    alpha_score: float = 0.0

    final_score: float = 0.0

    factors: dict = field(
        default_factory=dict
    )

    signals: list = field(
        default_factory=list
    )

    market_state: str = "UNKNOWN"

    confidence: float = 0.0

    weights: dict = field(
        default_factory=dict
    )

    explanation: dict = field(
        default_factory=dict
    )

    reason: str = ""