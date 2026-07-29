from dataclasses import dataclass


@dataclass
class TradeRecord:

    code: str

    entry_price: float

    exit_price: float

    quantity: int


@dataclass
class BacktestResult:

    total_return: float

    win_rate: float

    trades: int