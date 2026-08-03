from dataclasses import dataclass


@dataclass
class RankingResult:

    code: str

    score: float

    rank: int = 0

    ranking_reason: str = ""

    alpha_score: float = 0

    factors: dict = None

    signals: list = None

    market_state: str = "UNKNOWN"

    confidence: float = 0

    explanation: dict = None

    reason: str = ""