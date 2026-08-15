from core.feedback.storage import (
    FeedbackStorage
)


def test_feedback_storage():

    storage = FeedbackStorage()


    storage.save(
        {
            "code":"000001",
            "result":True
        }
    )


    records = storage.load()


    assert len(records) > 0

    assert (
        records[-1]["code"]
        ==
        "000001"
    )