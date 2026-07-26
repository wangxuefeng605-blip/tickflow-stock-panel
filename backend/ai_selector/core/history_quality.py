"""
History Quality Gate

Validate stock history before factor calculation.
"""

MIN_HISTORY_DAYS = 120


def validate_history(df):
    """
    Validate historical kline data.

    return:
        {
            "valid": True/False,
            "reason": str,
            "days": int
        }
    """

    if df is None:
        return {
            "valid": False,
            "reason": "empty",
            "days": 0
        }


    days = len(df)


    if days < MIN_HISTORY_DAYS:
        return {
            "valid": False,
            "reason": "too_short",
            "days": days
        }


    return {
        "valid": True,
        "reason": "ok",
        "days": days
    }