from dataclasses import dataclass


@dataclass
class RuntimeRequest:

    code: str
    features: dict


@dataclass
class RuntimeResponse:

    code: str
    result: dict