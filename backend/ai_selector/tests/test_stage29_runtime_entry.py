from core.runtime.runtime_entry import RuntimeEntry


def test_runtime_entry():

    entry = RuntimeEntry()

    result = entry.execute(
        {
            "code": "000001",
            "momentum": 0.8
        }
    )

    assert result["runtime_completed"]
    assert result["entry_completed"]