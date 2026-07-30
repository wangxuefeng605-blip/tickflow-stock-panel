from dataclasses import dataclass


@dataclass
class RuntimeRequest:

    code: str
    features: dict