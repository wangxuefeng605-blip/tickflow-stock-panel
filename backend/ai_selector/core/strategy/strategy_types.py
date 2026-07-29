from dataclasses import dataclass


@dataclass
class StrategyConfig:

    name: str

    style: str

    max_positions: int

    risk_level: float


@dataclass
class StrategyDecision:

    action: str

    reason: str

    confidence: float
