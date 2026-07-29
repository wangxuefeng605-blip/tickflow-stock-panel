from dataclasses import dataclass, field


@dataclass
class AIFlowContext:


    ranking: object = None


    decision: object = None


    strategy: object = None


    orders: object = field(
        default_factory=list
    )