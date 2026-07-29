from dataclasses import dataclass


@dataclass
class ExecutionOrder:

    code: str

    action: str

    quantity: int

    confidence: float

    reason: str