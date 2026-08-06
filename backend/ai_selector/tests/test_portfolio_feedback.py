from core.learning.portfolio_feedback import (
    create_feedback_record,
    save_feedback
)


def test_create_feedback():

    item = {

        "code":"000820",

        "score":4.62,

        "alpha_score":0.52
    }


    result = create_feedback_record(
        item
    )


    assert result["code"] == "000820"

    assert result["status"] == "PENDING"



def test_save_feedback():

    path = save_feedback(
        [
            {
                "code":"000820"
            }
        ]
    )


    assert path.exists()