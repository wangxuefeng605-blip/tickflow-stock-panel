@dataclass
class DecisionResult:

    code:str

    action:str

    confidence:float

    allocation:float

    reasons:list