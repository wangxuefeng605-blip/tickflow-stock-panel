import pandas as pd

from core.history_quality import validate_history


def make_history(days):

    return pd.DataFrame(
        {
            "date": range(days),
            "open": range(days),
            "close": range(days),
            "high": range(days),
            "low": range(days),
            "amount": range(days),
        }
    )


def test_history_ok():

    df = make_history(200)

    result = validate_history(df)

    assert result["valid"] is True



def test_history_short():

    df = make_history(20)

    result = validate_history(df)

    assert result["valid"] is False

    assert result["reason"] == "history_too_short"



def test_history_empty():

    result = validate_history(None)

    assert result["valid"] is False