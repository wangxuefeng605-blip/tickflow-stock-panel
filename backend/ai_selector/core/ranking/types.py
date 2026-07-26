from dataclasses import dataclass


@dataclass
class RankingResult:

    code: str

    score: float

    rank: int = 0

    confidence: float = 0.0

from dataclasses import dataclass, field


@dataclass
class RankingResult:

    code: str

    score: float

    rank: int = 0

    confidence: float = 0.0

    signals: list[str] = field(
        default_factory=list
    )

    risks: list[str] = field(
        default_factory=list
    )