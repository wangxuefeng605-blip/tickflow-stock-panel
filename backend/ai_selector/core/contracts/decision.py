from dataclasses import dataclass


@dataclass
class DecisionContract:

    code:str
    action:str
    confidence:float
    score:float