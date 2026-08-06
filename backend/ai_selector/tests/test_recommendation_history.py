from core.recommendation_history import (
    save_daily_recommendation,
    load_history,
    get_latest
)


def test_history():

    data = [
        {
            "code":"000533",
            "score":3.93
        }
    ]


    path = save_daily_recommendation(
        data
    )


    assert path.exists()


    history = load_history()

    assert len(history) >= 1


    latest = get_latest()

    assert latest is not None