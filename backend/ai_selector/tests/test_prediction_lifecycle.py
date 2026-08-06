from core.learning import PredictionLifecycle
from types import SimpleNamespace


def test_prediction_lifecycle():

    lifecycle = PredictionLifecycle()


    results = [
        SimpleNamespace(
            code="000001",
            score=95
        )
    ]


    paths = lifecycle.record_top10(
        results,
        "2026-08-07"
    )


    assert len(paths)>0