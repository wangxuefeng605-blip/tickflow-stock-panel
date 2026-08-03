from core.learning.prediction.prediction_store import (
    PredictionStore
)


def test_prediction_store():

    store = PredictionStore()


    path = store.save(
        [
            {
                "code":"000001",
                "score":90
            }
        ],
        market_state="BULL",
        weights={
            "momentum":0.35
        }
    )


    assert path.exists()


    records = store.load_all()


    assert len(records) > 0


    item = records[-1]


    assert (
        item["stocks"][0]["code"]
        ==
        "000001"
    )