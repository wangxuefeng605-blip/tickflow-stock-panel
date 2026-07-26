from dataclasses import dataclass


@dataclass
class RankingResult:

    code: str

    score: float

    rank: int = 0

    confidence: float = 0.0

    signals: list[str] = None

    risks: list[str] = None