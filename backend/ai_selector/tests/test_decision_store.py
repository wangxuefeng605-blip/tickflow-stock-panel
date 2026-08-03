from core.decision import (
    DecisionStore,
    DecisionRecord
)


def test_decision_store():

    store = DecisionStore()


    record = DecisionRecord(

        code="603580",

        action="BUY",

        score=0.72,

        confidence=0.85,

        market_state="BULL",

        signals=[
            "Strong momentum"
        ]

    )


    store.save(
        record
    )


    records = store.load_all()


    assert len(records) >= 1

    assert records[0]["code"]=="603580"