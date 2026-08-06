"""
Prediction feedback compatibility layer
"""


def evaluate_prediction(
    entry=None,
    future=None,
    result=None
):
    """
    Evaluate prediction accuracy.

    Legacy API:

        evaluate_prediction(
            entry=100,
            future=110
        )

    Returns:

        {
            "success": True,
            "reward": 1,
            "return": 0.1
        }
    """


    if result is not None:

        future_return = result.get(
            "return",
            0
        )

        success = future_return > 0


        return {

            "success": success,

            "reward": 1 if success else 0,

            "return": future_return

        }


    if entry is None or future is None:

        return {

            "success": False,

            "reward": 0,

            "return": 0

        }


    if entry == 0:

        return {

            "success": False,

            "reward": 0,

            "return": 0

        }


    rate = (
        future - entry
    ) / entry


    success = rate > 0


    return {

        "success": success,

        "reward": 1 if success else 0,

        "return": rate

    }