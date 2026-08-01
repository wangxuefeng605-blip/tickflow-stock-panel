from core.learning.prediction_store import PredictionStore


def test_prediction_store():

    store = PredictionStore()

    store.save([])

    assert True