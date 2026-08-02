from core.scanner.engine import ScannerEngine
from core.learning.learning_runtime_orchestrator import (
    LearningRuntimeOrchestrator
)


def test_scanner_learning_runtime_integration():

    stocks = [
        "000001",
        "000002"
    ]


    engine = ScannerEngine(
        stocks,
        workers=1
    )


    assert hasattr(
        engine,
        "learning_runtime"
    )


    assert isinstance(
        engine.learning_runtime,
        LearningRuntimeOrchestrator
    )