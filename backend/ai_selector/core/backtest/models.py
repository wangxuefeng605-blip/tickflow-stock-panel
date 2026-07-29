from dataclasses import dataclass


@dataclass
class BacktestRequest:

    strategy: str

    start_date: str

    end_date: str

    capital: float


@dataclass
class TradeRecord:

    code: str

    action: str

    price: float

    quantity: int


@dataclass
class BacktestResult:

    total_return: float

    max_drawdown: float

    trades: list