from dataclasses import dataclass, field



from dataclasses import dataclass, field


@dataclass
class RankingResult:

    code: str

    score: float

    rank: int = 0

    ranking_score: float = 0.0

    ai_score: float = 0.0

    confidence: float = 0.0

    weight: float = 1.0

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


    ranking_reason: list[str] = field(
        default_factory=list
    )


    explanation: dict = field(
        default_factory=dict
    )