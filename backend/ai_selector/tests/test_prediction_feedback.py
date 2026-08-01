from core.learning import evaluate_prediction


def test_prediction_success():

    result = evaluate_prediction(
        entry=100,
        future=110
    )

    assert result["return"] == 0.1
    assert result["success"] is True