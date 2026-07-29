from dataclasses import dataclass, field


@dataclass
class AIFlowContext:


    def __init__(self):

        self.ranking = None

        self.decision = None

        self.portfolio = None

        self.strategy = None

        self.orders = None

        self.backtest = None

        self.learning = None
    
    orders: object = field(
        default_factory=list
    )