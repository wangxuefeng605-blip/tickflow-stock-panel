from dataclasses import dataclass, field


@dataclass
class AIFlowContext:

    ranking = None

    decision = None

    strategy = None

    execution = None

    portfolio = None

    backtest = None


    orders: object = field(
        default_factory=list
    )