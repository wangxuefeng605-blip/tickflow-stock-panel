from dataclasses import dataclass
from enum import Enum


class StrategyType(Enum):

    MOMENTUM = "momentum"

    DEFENSIVE = "defensive"

    BALANCED = "balanced"



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