from core.intelligence.context_builder import ContextBuilder
from core.scanner.engine import ScannerEngine


def test_scanner_dynamic_ai_flow():

    context = ContextBuilder().build()

    engine = ScannerEngine(
        [
            "000001",
            "000002"
        ],
        workers=1,
        context=context
    )

    result = engine.run()

    assert result is not None