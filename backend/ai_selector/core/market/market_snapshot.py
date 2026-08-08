from dataclasses import dataclass
from datetime import datetime


@dataclass
class MarketSnapshot:

    code: str

    price: float

    change_pct: float

    volume: float

    timestamp: datetime