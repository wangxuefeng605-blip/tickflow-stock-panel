from dataclasses import dataclass, field


@dataclass
class BacktestRequest:

    strategy: str = "AI"

    start_date: str = ""

    end_date: str = ""

    capital: float = 0



@dataclass
class TradeRecord:

    code: str

    action: str

    price: float

    quantity: int



@dataclass
class BacktestResult:

    total_return: float = 0

    max_drawdown: float = 0

    trades: list = field(
        default_factory=list
    )

    strategy: str = "AI"

    equity_curve: list = field(
        default_factory=list
    )

    return_rate: float = 0


    def __getitem__(
        self,
        key
    ):

        return getattr(
            self,
            key
        )