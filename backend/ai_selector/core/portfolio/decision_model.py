from dataclasses import dataclass


@dataclass
class PortfolioDecision:

    action:str

    allocation:float

    confidence:float

    reason:str